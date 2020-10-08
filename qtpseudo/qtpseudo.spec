# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

PYMEDPHYS_DIR = "/home/osboxes/PythonProjects/pymedphys4/pymedphys/"
a = Analysis(['qtpseudo.py'],
             pathex=['/home/osboxes/PythonProjects/qtpseudo1/qtpseudo/qtpseudo'],
             binaries=[],
             datas=[
                 (PYMEDPHYS_DIR + 'pymedphys/_imports/imports.py','pymedphys/_imports'),
                 (PYMEDPHYS_DIR +'pymedphys/_experimental/pseudonymisation/identifying_uids.json' ,'pymedphys/_experimental/pseudonymisation'),
                 (PYMEDPHYS_DIR +'pymedphys/_data/zenodo.json' ,'pymedphys/_data'),
                 (PYMEDPHYS_DIR +'pymedphys/_data/urls.json' ,'pymedphys/_data'),
                 (PYMEDPHYS_DIR +'pymedphys/_data/hashes.json' ,'pymedphys/_data'),
                 (PYMEDPHYS_DIR +'pymedphys/_dicom/constants/baseline_repeaters_dictionary.json' ,'pymedphys/_dicom/constants'),
                 (PYMEDPHYS_DIR +'pymedphys/_dicom/anonymise/identifying_keywords.json' ,'pymedphys/_dicom/anonymise'),
                 (PYMEDPHYS_DIR +'pymedphys/_trf/decode/config.json' ,'pymedphys/_trf/decode'),

                 ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=True)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [('v', None, 'OPTION')],
          name='qtpseudo',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          icon='./pseudonymise_icon.png' )
