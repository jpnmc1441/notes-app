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
        'xml',
        'xml.etree',
        'xml.etree.ElementTree',
        'xml.parsers',
        'xml.parsers.expat',
        'plistlib',
        'pkg_resources',
        'pkg_resources.py2_warn',
    ]
)

flask_datas,   flask_binaries,   flask_hidden   = collect_all('flask')
wz_datas,      wz_binaries,      wz_hidden      = collect_all('werkzeug')
jinja2_datas,  jinja2_binaries,  jinja2_hidden  = collect_all('jinja2')

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[] + flask_binaries + wz_binaries + jinja2_binaries,
    datas=[
        ('templates', 'templates'),   # bundle the Jinja2 templates
    ] + flask_datas + wz_datas + jinja2_datas,
    hiddenimports=hidden + flask_hidden + wz_hidden + jinja2_hidden,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'unittest', 'email', 'pydoc'],
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
