f1, b1, m1 = map(int, input() .split())
fp, bp, mp = map(int, input() .split())
monas = 0
if f1 <= fp:
    faltouf = (f1-fp)
    monas += faltouf
if b1 <= bp:
    faltoub = (b1-bp)
    monas += faltoub
if m1 <= mp:
    faltoum = (m1-mp)
    monas += faltoum

monas = monas*(-1)
print(monas)