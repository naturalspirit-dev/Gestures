# -*- mode: python ; coding: utf-8 -*-
# Use this file for development only
# Usage:
# > pyinstaller gestures-debug.spec --noconfirm
# or add --upx-dir=<path to UPX> if you want to compress the executable

import os

__appname__ = 'gestures'
__version__ = '2.0.2-beta'
_name = f'{__appname__}-{__version__}'

block_cipher = None

a = Analysis(['src\\main.py'],
             pathex=[os.getcwd()],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name=_name,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name=_name)
