# Ajusta Info.plist de iOS: solo horizontal y barra de estado oculta. Uso: python3 scripts/ios-patch.py
import plistlib, pathlib, sys
p = pathlib.Path('ios/App/App/Info.plist')
if not p.exists(): sys.exit('No existe ' + str(p) + '. Ejecuta antes: npx cap add ios')
d = plistlib.loads(p.read_bytes())
land = ['UIInterfaceOrientationLandscapeLeft', 'UIInterfaceOrientationLandscapeRight']
d['UISupportedInterfaceOrientations'] = land
d['UISupportedInterfaceOrientations~ipad'] = land
d['UIStatusBarHidden'] = True
d['UIViewControllerBasedStatusBarAppearance'] = False
d['UIRequiresFullScreen'] = True
p.write_bytes(plistlib.dumps(d))
print('Info.plist actualizado (horizontal + pantalla completa)')
