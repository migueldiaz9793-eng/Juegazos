# Genera el icono de la gallina en todas las densidades de Android. Uso: python3 make_icons.py android/app/src/main/res
import sys, os
from PIL import Image, ImageDraw
res = sys.argv[1]
def chicken(size, bg=None, pad=0.0):
    S = 1024
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if bg: d.rounded_rectangle((0, 0, S - 1, S - 1), radius=int(S * .22), fill=bg)
    k = 1 - pad * 2; o = S * pad
    P = lambda x, y: (o + x * k, o + y * k)
    def ell(x0, y0, x1, y1, **kw): d.ellipse((*P(x0, y0), *P(x1, y1)), **kw)
    ell(250, 330, 780, 900, fill='#ffcc33', outline='#a07800', width=10)   # cuerpo
    for cx in (400, 510, 620): ell(cx - 60, 190, cx + 60, 330, fill='#e02020', outline='#8f1010', width=8)  # cresta
    ell(300, 260, 740, 700, fill='#ffcc33', outline='#a07800', width=10)   # cabeza
    d.polygon([P(500, 470), P(720, 520), P(500, 590)], fill='#ff9f1a', outline='#b36b00')  # pico
    ell(430, 600, 540, 760, fill='#e02020')                                  # barbilla
    for ex in (410,):  ell(ex, 400, ex + 70, 470, fill='white', outline='black', width=6); ell(ex + 28, 420, ex + 58, 452, fill='black')
    ell(560, 400, 630, 470, fill='white', outline='black', width=6); ell(588, 420, 618, 452, fill='black')
    return im.resize((size, size), Image.LANCZOS)
dens = {'mdpi': 1, 'hdpi': 1.5, 'xhdpi': 2, 'xxhdpi': 3, 'xxxhdpi': 4}
for n, f in dens.items():
    p = os.path.join(res, 'mipmap-' + n)
    if not os.path.isdir(p): continue
    chicken(round(48 * f), bg='#2a1a4e').save(os.path.join(p, 'ic_launcher.png'))
    chicken(round(48 * f), bg='#2a1a4e').save(os.path.join(p, 'ic_launcher_round.png'))
    chicken(round(108 * f), pad=.2).save(os.path.join(p, 'ic_launcher_foreground.png'))
bgp = os.path.join(res, 'values', 'ic_launcher_background.xml')
open(bgp, 'w').write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#2A1A4E</color>\n</resources>\n')
print('iconos generados')
