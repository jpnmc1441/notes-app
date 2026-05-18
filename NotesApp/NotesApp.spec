# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for the Notes app Windows build.
# Build with:  pyinstaller NotesApp.spec

from PyInstaller.utils.hooks import collect_submodules

hidden = (
    collect_submodules('flask')
    + collect_submodules('jinja2')
    + collect_submodules('werkzeug')
    + collect_submodules('click')
    + collect_submodules('itsdangerous')
)

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('templates', 'templates'),   # bundle the Jinja2 templates
    ],
    hiddenimports=hidden,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'unittest', 'email', 'xml', 'pydoc'],
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
