import math
# ---------- Concept 1: Ascent (burgundy / charcoal) ----------
BUR, CHR, GRY = '#7A1F2B', '#3D3F45', '#8A8D93'
sw = 30
b = []
ox, oy = 112, 120   # mark origin; cap height 200
# M: rising-chart M (right peak higher than left), filled
M = [(0,215),(0,95),(30,95),(70,148),(110,30),(140,30),(140,215),(110,215),(110,112),(80,190),(58,190),(30,152),(30,215)]
b.append('<polygon fill="%s" points="%s"/>' % (CHR, ' '.join(f'{ox+x},{oy+y}' for x,y in M)))
# D
dx = ox+185
b.append(f'<path fill="none" stroke="{BUR}" stroke-width="{sw}" d="M{dx+15},{oy+15} V{oy+200} H{dx+60} A92.5,92.5 0 0 0 {dx+60},{oy+15} Z"/>')
# K stem + leg
kx = dx+190
b.append(f'<line stroke="{BUR}" stroke-width="{sw}" x1="{kx+30}" y1="{oy+110}" x2="{kx+120}" y2="{oy+215}"/>')
# K upper arm = growth arrow
tipx, tipy = kx+175, oy-45
ang = math.degrees(math.atan2(tipy-(oy+125), tipx-(kx+15)))
ux, uy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
b.append(f'<defs><linearGradient id="g1" gradientUnits="userSpaceOnUse" x1="490" y1="250" x2="660" y2="70"><stop offset="0" stop-color="{CHR}"/><stop offset="1" stop-color="{GRY}"/></linearGradient></defs>')
b.append(f'<line stroke="url(#g1)" stroke-width="{sw}" x1="{kx+15}" y1="{oy+125}" x2="{tipx-ux*48:.1f}" y2="{tipy-uy*48:.1f}"/>')
b.append(arrowhead(tipx, tipy, ang, 70, GRY))
b.append(f'<line stroke="{BUR}" stroke-width="{sw}" x1="{kx+15}" y1="{oy}" x2="{kx+15}" y2="{oy+215}"/>')
p, w = text('FINANCIAL SERVICES', 'mont800', 44, 400, 445, CHR, tracking=0.12, anchor='middle'); b.append(p)
b.append(f'<rect x="150" y="470" width="500" height="4" fill="{BUR}"/>')
svg('concept-1-ascent', 800, 560, '\n'.join(b))

# ---------- Concept 2: Pie-Chart D (purple / gold) ----------
PUR, GLD = '#5B3BAF', '#C9922E'
b = []
ox, oy = 95, 70; H = 200
# M (filled, slab geometric)
M = [(0,H),(0,0),(42,0),(85,95),(128,0),(170,0),(170,H),(130,H),(130,85),(100,152),(70,152),(40,85),(40,H)]
b.append('<polygon fill="%s" points="%s"/>' % (PUR, ' '.join(f'{ox+x},{oy+y}' for x,y in M)))
# D as a pie chart with an exploded gold slice
dx = ox+195; cx, cy, r = dx+45, oy+100, 100
a0, a1 = -62, -8
pt = lambda a: (cx+r*math.cos(math.radians(a)), cy+r*math.sin(math.radians(a)))
x1,y1 = pt(a1)
x0,y0 = pt(a0)
b.append(f'<path fill="{PUR}" d="M{cx},{cy} L{x1:.1f},{y1:.1f} A{r},{r} 0 0 1 {cx},{cy+r} H{dx} V{oy} H{cx} A{r},{r} 0 0 1 {x0:.1f},{y0:.1f} Z"/>')
mid = math.radians((a0+a1)/2); off = 14
x0,y0 = pt(a0)
b.append(f'<path fill="{GLD}" transform="translate({off*math.cos(mid):.1f},{off*math.sin(mid):.1f})" d="M{cx},{cy} L{x0:.1f},{y0:.1f} A{r},{r} 0 0 1 {x1:.1f},{y1:.1f} Z"/>')
# K: stem + leg purple, arm = gold arrow
kx = dx+175
b.append(f'<rect fill="{PUR}" x="{kx}" y="{oy}" width="40" height="{H}"/>')
b.append(f'<polygon fill="{PUR}" points="{kx+40},{oy+105} {kx+70},{oy+82} {kx+160},{oy+H} {kx+110},{oy+H}"/>')
sx, sy = kx+30, oy+120; tipx, tipy = kx+185, oy-40
ang = math.degrees(math.atan2(tipy-sy, tipx-sx)); ux, uy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
b.append(f'<line stroke="{GLD}" stroke-width="36" x1="{sx}" y1="{sy}" x2="{tipx-ux*55:.1f}" y2="{tipy-uy*55:.1f}"/>')
b.append(arrowhead(tipx, tipy, ang, 82, GLD))
p, w = text('FINANCIAL SERVICES', 'play700', 58, 400, 375, GLD, tracking=0.04, anchor='middle'); b.append(p)
p, w = text('YOUR FINANCIAL GROWTH BEGINS HERE', 'mont600', 19, 400, 418, PUR, tracking=0.32, anchor='middle'); b.append(p)
svg('concept-2-pie-chart-d', 800, 480, '\n'.join(b))

# ---------- Concept 3: Bar-Chart Letters (navy / green) ----------
NAV, NAV2, GRN = '#0F2A4A', '#2F5C8F', '#1FA36B'
b = []
top, H = 90, 210; bot = top+H; mid = top+H/2; bw, gap = 18, 9; P = bw+gap; x = 160
def bar(x, y0, y1, c): b.append(f'<rect fill="{c}" x="{x:.1f}" y="{y0:.1f}" width="{bw}" height="{y1-y0:.1f}" rx="4"/>')
# M: outer stems full height; inner bars trace the V
bar(x, top, bot, NAV2); x += P
for (a, z) in [(0, .40), (.30, .74), (0, .40)]:
    bar(x, top+a*H, top+z*H, NAV2); x += P
bar(x, top, bot, NAV2); x += P + 26
# D: stem + bars split around a semicircular counter
bar(x, top, bot, NAV); sx = x + bw; x += P
R, r = H/2, H/2-44
for i in range(4):
    xc = x + bw/2 - sx + 6
    ho = math.sqrt(max(R*R - xc*xc, 0)); hi = math.sqrt(max(r*r - xc*xc, 0))
    if hi > 0: bar(x, mid-ho, mid-hi, NAV); bar(x, mid+hi, mid+ho, NAV)
    else: bar(x, mid-ho, mid+ho, NAV)
    x += P
x += 26
# K: stem, then rising green arm (growth) and navy leg
bar(x, top, bot, NAV); x += P
seg = 44
for i in range(5):
    t = (i+0.5)/5
    if i == 0: bar(x, mid-seg/2-6, mid+seg/2+6, NAV)
    else:
        bar(x, mid - t*(H/2+20) - seg/2, mid - t*(H/2+20) + seg/2, GRN)
        bar(x, mid + t*H/2 - seg/2 + 10, min(mid + t*H/2 + seg/2 + 10, bot), NAV)
    x += P
lastx = x - P
lt = mid - (4.5/5)*(H/2+20) - seg/2
b.append(f'<polygon fill="{GRN}" points="{lastx+bw/2},{lt-38} {lastx-10},{lt-6} {lastx+bw+10},{lt-6}"/>')
print('bar mark spans 160 ..', x - gap)
p, w = text('MDK', 'mont800', 56, 400, 400, NAV, tracking=0.3, anchor='middle'); b.append(p)
p, w = text('FINANCIAL SERVICES', 'mont600', 22, 400, 438, GRN, tracking=0.38, anchor='middle'); b.append(p)
svg('concept-3-bar-chart-letters', 800, 490, '\n'.join(b))

# ---------- Concept 4: Crest monogram (black / gold) ----------
INK, GOLD, GOLD2 = '#14171C', '#C8A04A', '#E6C878'
b = []
b.append(f'<defs><linearGradient id="gg" gradientUnits="userSpaceOnUse" x1="250" y1="60" x2="550" y2="400"><stop offset="0" stop-color="{GOLD2}"/><stop offset="1" stop-color="{GOLD}"/></linearGradient></defs>')
cx = 400
shield = f'M{cx},40 L{cx+150},85 V215 C{cx+150},310 {cx+80},360 {cx},395 C{cx-80},360 {cx-150},310 {cx-150},215 V85 Z'
b.append(f'<path fill="{INK}" d="{shield}"/>')
b.append(f'<path fill="none" stroke="url(#gg)" stroke-width="6" transform="translate({cx} 215) scale(0.92) translate({-cx} -215)" d="{shield}"/>')
b.append('<g transform="translate(400 222) scale(0.8) translate(-408 -222)">')
# ligature: M's right stem doubles as D's stem (one continuous stroke)
s = 15; top, bot = 165, 285; h = bot-top
mx = cx-122
b.append(f'<path fill="none" stroke="url(#gg)" stroke-width="{s}" stroke-linejoin="miter" stroke-miterlimit="2" d="M{mx},{bot} V{top} L{mx+36},{top+78} L{mx+72},{top} H{mx+88} A{h/2},{h/2} 0 0 1 {mx+88},{bot} H{mx+72} V{top}"/>')
kx = mx+178
sx, sy = kx, top+68; tipx, tipy = kx+88, top-42
ang = math.degrees(math.atan2(tipy-sy, tipx-sx)); ux, uy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
b.append(f'<line stroke="url(#gg)" stroke-width="{s}" x1="{kx+5}" y1="{top+62}" x2="{kx+58}" y2="{bot}"/>')
b.append(f'<line stroke="url(#gg)" stroke-width="{s}" x1="{sx}" y1="{sy}" x2="{tipx-ux*28:.1f}" y2="{tipy-uy*28:.1f}"/>')
b.append(arrowhead(tipx, tipy, ang, 38, GOLD2))
b.append(f'<line stroke="url(#gg)" stroke-width="{s}" x1="{kx}" y1="{top}" x2="{kx}" y2="{bot}"/>')
b.append('</g>')
p, w = text('MDK', 'play700', 64, cx, 480, INK, tracking=0.18, anchor='middle'); b.append(p)
p, w = text('FINANCIAL SERVICES', 'mont600', 22, cx, 520, GOLD, tracking=0.38, anchor='middle'); b.append(p)
svg('concept-4-crest-monogram', 800, 570, '\n'.join(b))
