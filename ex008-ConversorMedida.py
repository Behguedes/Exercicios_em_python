from calendar import day_name

m = float(input('Digite uma distância em metros: '))
cm = m * 100
mm = m * 1000
dm = mm / 10
hm = m / 100
km = m / 1000
input('A medida de {}m corresponde a \n{:.0f}cm \n{:.0f}mm \n{}dam \n{}hm \n{}km'.format(m, cm, mm, dm, hm, km))

