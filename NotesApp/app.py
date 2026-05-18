import os
import sys
import json
import uuid
import re
import html
import webbrowser
import threading
from datetime import datetime, timezone
from flask import Flask, request, jsonify, render_template, abort


def _resource(rel):
    """Resolve a bundled resource path for both normal Python and frozen exe."""
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel)


def _notes_dir():
    """Return (and create) the notes storage directory.

    When running as a frozen Windows exe the notes live in
    %APPDATA%\\Notes\\notes so they survive updates and avoid
    writing into Program Files (which requires elevation).
    """
    if getattr(sys, 'frozen', False) and os.name == 'nt':
        path = os.path.join(os.environ['APPDATA'], 'Notes', 'notes')
    else:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'notes')
    os.makedirs(path, exist_ok=True)
    return path


app = Flask(__name__, template_folder=_resource('templates'))
NOTES_DIR = _notes_dir()


def note_path(note_id):
    return os.path.join(NOTES_DIR, f"{note_id}.json")


def read_note(note_id):
    path = note_path(note_id)
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_note(note):
    with open(note_path(note['id']), 'w', encoding='utf-8') as f:
        json.dump(note, f, ensure_ascii=False, indent=2)


def strip_html(content):
    text = re.sub(r'<[^>]+>', ' ', content or '')
    text = html.unescape(text)
    return ' '.join(text.split())


def all_notes():
    notes = []
    for filename in os.listdir(NOTES_DIR):
        if filename.endswith('.json'):
            note = read_note(filename[:-5])
            if note:
                notes.append(note)
    notes.sort(key=lambda n: n.get('updated_at', ''), reverse=True)
    return notes


def note_summary(note):
    return {
        'id': note['id'],
        'title': note['title'],
        'preview': strip_html(note.get('body', ''))[:120],
        'created_at': note['created_at'],
        'updated_at': note['updated_at'],
    }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/notes', methods=['GET'])
def list_notes():
    return jsonify([note_summary(n) for n in all_notes()])


@app.route('/api/notes', methods=['POST'])
def create_note():
    now = datetime.now(timezone.utc).isoformat()
    note = {
        'id': str(uuid.uuid4()),
        'title': 'New Note',
        'body': '',
        'created_at': now,
        'updated_at': now,
    }
    write_note(note)
    return jsonify(note), 201


@app.route('/api/notes/<note_id>', methods=['GET'])
def get_note(note_id):
    note = read_note(note_id)
    if not note:
        abort(404)
    return jsonify(note)


@app.route('/api/notes/<note_id>', methods=['PUT'])
def update_note(note_id):
    note = read_note(note_id)
    if not note:
        abort(404)
    data = request.get_json()
    note['title'] = data.get('title', note['title'])
    note['body'] = data.get('body', note['body'])
    note['updated_at'] = datetime.now(timezone.utc).isoformat()
    write_note(note)
    return jsonify(note)


@app.route('/api/notes/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    path = note_path(note_id)
    if not os.path.exists(path):
        abort(404)
    os.remove(path)
    return '', 204


@app.route('/api/search')
def search_notes():
    q = request.args.get('q', '').lower().strip()
    if not q:
        return jsonify([note_summary(n) for n in all_notes()])
    results = []
    for note in all_notes():
        title_hit = q in note.get('title', '').lower()
        body_hit = q in strip_html(note.get('body', '')).lower()
        if title_hit or body_hit:
            results.append(note_summary(note))
    return jsonify(results)


def open_browser():
    webbrowser.open('http://127.0.0.1:5000')


if __name__ == '__main__':
    threading.Timer(1.2, open_browser).start()
    app.run(debug=False, port=5000, use_reloader=False)
