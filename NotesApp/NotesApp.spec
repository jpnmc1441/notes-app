# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for the Notes app Windows build.
# Build with:  pyinstaller NotesApp.spec

from PyInstaller.utils.hooks import collect_submodules, collect_all

hidden = (
    collect_submodules('flask')
    + collect_submodules('jinja2')
    + collect_submodules('werkzeug')
    + collect_submodules('click')
    + collect_submodules('itsdangerous')
    + [
        # xml stack (required by plistlib and pkg_resources)
        'xml',
        'xml.etree',
        'xml.etree.ElementTree',
        'xml.parsers',
        'xml.parsers.expat',
        'plistlib',
        'pkg_resources',
        'pkg_resources.py2_warn',
        # email stack
        'email',
        'email.mime',
        'email.mime.text',
        'email.mime.multipart',
        'email.generator',
        'email.header',
        'email.utils',
        # logging
        'logging',
        'logging.handlers',
        # concurrency / networking
        'queue',
        'threading',
        'socketserver',
        'http',
        'http.server',
        'http.client',
        'urllib',
        'urllib.parse',
        'urllib.request',
        # data / crypto
        'json',
        'uuid',
        'hashlib',
        'hmac',
        'secrets',
        'sqlite3',
    ]
)

flask_datas,   flask_binaries,   flask_hidden   = collect_all('flask')
wz_datas,      wz_binaries,      wz_hidden      = collect_all('werkzeug')
jinja2_datas,  jinja2_binaries,  jinja2_hidden  = collect_all('jinja2')
click_datas,   click_binaries,   click_hidden   = collect_all('click')
its_datas,     its_binaries,     its_hidden     = collect_all('itsdangerous')

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=(
        flask_binaries + wz_binaries + jinja2_binaries
        + click_binaries + its_binaries
    ),
    datas=(
        [('templates', 'templates')]
        + flask_datas + wz_datas + jinja2_datas
        + click_datas + its_datas
    ),
    hiddenimports=(
        hidden + flask_hidden + wz_hidden + jinja2_hidden
        + click_hidden + its_hidden
    ),
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter'],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='NotesApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,          # no terminal window
    icon='assets/icon.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='NotesApp',        # output folder: dist/NotesApp/
)
