# -*- mode: python ; coding: utf-8 -*-
# Use this file for deployment to production only
# 
# This file was created by running this command:
# > pyi-makespec --onefile src/main.py
# 
# Usage:
# > pyinstaller gestures-final.spec --noconfirm

import os

__appname__ = 'gestures'
__version__ = '1.4.1-rc2'
_name = f'{__appname__}-{__version__}'

block_cipher = None


a = Analysis(['src\\main.py'],
             pathex=[os.getcwd()],
             binaries=[],
             datas=[('images/g-key.ico', 'images')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name=_name,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='images/g-key.ico',
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
