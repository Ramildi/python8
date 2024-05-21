def yerleri_tap(xallar):
    yerlər = ['1-ci', '2-ci', '3-cü', '4-cü', '5-ci']
    
    xal_yer = list(zip(xallar, yerlər))

    sıralanmış_xal_yer = sorted(xal_yer, key=lambda x: x[0], reverse=True)

    tapılan_yer = [pair[1] for pair in sıralanmış_xal_yer]
    
    return tapılan_yer

xallar = [5, 3, 4, 2, 1]

print(yerleri_tap(xallar))
