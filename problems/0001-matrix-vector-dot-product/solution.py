def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if len(a[0]) != len(b):
        return -1
    
    sonuc = []
    for satir in a:
        toplam = sum(s * v for s, v in zip(satir, b))
        sonuc.append(toplam)
        
    return sonuc