d1= {'H':12,'M':40,'S':55}
d2= {'H':13,'M':30,'S':55}

def add_time(d1,d2):
    sec_tot = (d1['S'] + d2['S'])
    sec_rem = sec_tot %60
    sec_pass =sec_tot - sec_rem
    print(sec_pass//60)


print(add_time(d1,d2))