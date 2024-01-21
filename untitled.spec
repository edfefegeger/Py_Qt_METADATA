# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Program Files/Git/полный/путь/к/вашему/файлу/untitled.py'],
    pathex=[],
    binaries=[],
    datas=[('form.ui', '.'), ('IMG_8222.JPG', '.'), ('untitled.pyproject', '.'), ('untitled.spec', '.'), ('widget.py', '.'), ('untitled.pyproject.user', '.'), ('untitled.pyproject.user.8693d08', '.'), ('widget.spec', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='untitled',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
