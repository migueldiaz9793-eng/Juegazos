# Genera el icono de Android a partir de icon.png (en la raíz del repo o en scripts/).
# Uso: python3 make_icons.py android/app/src/main/res
import sys, os
from PIL import Image, ImageDraw, ImageFilter
res = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
src = next((p for p in (os.path.join(os.getcwd(), 'icon.png'), os.path.join(here, 'icon.png'), os.path.join(here, '..', 'icon.png')) if os.path.exists(p)), None)
if not src: sys.exit('No se encontro icon.png')
base = Image.open(src).convert('RGB')
m = min(base.size); base = base.crop(((base.width - m) // 2, 0, (base.width - m) // 2 + m, m))

def legacy(size, round_=False):
    im = base.resize((size, size), Image.LANCZOS).convert('RGBA')
    mask = Image.new('L', (size * 4, size * 4), 0)
    d = ImageDraw.Draw(mask)
    if round_: d.ellipse((0, 0, size * 4 - 1, size * 4 - 1), fill=255)
    else: d.rounded_rectangle((0, 0, size * 4 - 1, size * 4 - 1), radius=int(size * 4 * .18), fill=255)
    im.putalpha(mask.resize((size, size), Image.LANCZOS))
    return im

def adaptive(size):
    # Lienzo completo: fondo desenfocado + imagen nitida al 80 % (queda dentro de la zona segura de Android)
    bg = base.resize((size, size), Image.LANCZOS).filter(ImageFilter.GaussianBlur(size * .04))
    fg = base.resize((round(size * .8), round(size * .8)), Image.LANCZOS)
    bg.paste(fg, ((size - fg.width) // 2, (size - fg.height) // 2))
    return bg.convert('RGBA')

dens = {'mdpi': 1, 'hdpi': 1.5, 'xhdpi': 2, 'xxhdpi': 3, 'xxxhdpi': 4}
for n, f in dens.items():
    p = os.path.join(res, 'mipmap-' + n)
    if not os.path.isdir(p): continue
    legacy(round(48 * f)).save(os.path.join(p, 'ic_launcher.png'))
    legacy(round(48 * f), True).save(os.path.join(p, 'ic_launcher_round.png'))
    adaptive(round(108 * f)).save(os.path.join(p, 'ic_launcher_foreground.png'))
open(os.path.join(res, 'values', 'ic_launcher_background.xml'), 'w').write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#2A1A4E</color>\n</resources>\n')
print('iconos generados desde', src)
