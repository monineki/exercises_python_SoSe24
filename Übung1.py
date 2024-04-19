def cagr_berechnung(AK, EK, t):
    AK_abs = abs(AK)
    t_abs = abs(t)
    CAGR = ((EK/AK)**(1/t))-1
    return CAGR

print(cagr_berechnung(100, 700, 30))


AK = 120
t = 30
CAGR = cagr_berechnung(100, 700, 30)
EK = AK * ( 1 + CAGR)**t

print(EK)