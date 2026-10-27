import sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
F = '/tmp/claude-0/-home-user-Marketing/5ade1bab-adc4-553b-b36b-45df92f79b40/scratchpad/fonts/'
OUT = '/home/user/Marketing/content/mdk-financial-logo-concepts-2026-10/'
fonts = {k: TTFont(F+k+'.ttf') for k in ['mont800','mont600','mont500','play700']}

def text(s, font, size, x, y, fill, tracking=0, anchor='start'):
    f = fonts[font]; gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f['head'].unitsPerEm
    sc = size/upm; trk = tracking*size
    adv = sum(gs[cmap[ord(c)]].width*sc + trk for c in s) - trk
    if anchor == 'middle': x -= adv/2
    elif anchor == 'end': x -= adv
    pen = SVGPathPen(gs); cx = x
    for c in s:
        g = cmap[ord(c)]
        gs[g].draw(TransformPen(pen, (sc,0,0,-sc,cx,y)))
        cx += gs[g].width*sc + trk
    return f'<path fill="{fill}" d="{pen.getCommands()}"/>', adv

def svg(name, w, h, body, bg='#FFFFFF'):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n'
    if bg: s += f'<rect width="{w}" height="{h}" fill="{bg}"/>\n'
    s += body + '\n</svg>\n'
    open(OUT+name+'.svg','w').write(s)

def arrowhead(tipx, tipy, ang_deg, size, fill):
    import math
    a = math.radians(ang_deg)
    ux, uy = math.cos(a), math.sin(a); px, py = -uy, ux
    bx, by = tipx-ux*size, tipy-uy*size
    w = size*0.62
    return f'<polygon fill="{fill}" points="{tipx:.1f},{tipy:.1f} {bx+px*w:.1f},{by+py*w:.1f} {bx+ux*size*0.22:.1f},{by+uy*size*0.22:.1f} {bx-px*w:.1f},{by-py*w:.1f}"/>'

exec(open(sys.argv[1]).read())
