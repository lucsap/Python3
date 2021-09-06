a, b, c = input().split(' ')

def age (dias):
    dias = dias
    anos = dias // 360
    meses = (((dias / 360) - (dias // 360) * 360) // 30
    dyas = ((((dias / 360) - (dias // 360) * 360) / 30) - (((dias / 360) - (dias // 360) * 360) // 30)) *30
    print(f'{anos} ano(s), {meses} mes(es) e {dyas} dia(s)')

age_a = age(a)
age_b = age(b)
age_c = age(c)




