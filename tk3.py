s = int(input('продолжительность: '))
if s/60<1:
    print(str(s) + ' сек!')
elif s/60<60:
    m = s//60
    s = s % 60
    print(str(m) + ' мин ' + str(s) + ' сек!')
elif 1<=s/3600<24:
    h = s // 3600
    m = (s % 3600) // 60
    s = (s % 3600) % 60
    print(str(h) + ' час ' + str(m) + ' мин ' + str(s) + ' сек!')
else:
    d = s // 86400
    h = (s % 86400) // 3600
    s = s - ((d * 86400) + (h * 3600))
    m = s // 60
    s = s % 60
    print(str(d) + ' дн ' + str(h) + ' час ' + str(m) + ' мин ' + str(s) + ' сек!')