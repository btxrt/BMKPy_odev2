
yakıtTipi=input("yakıt tipiniz nedir?: ")
mesafe=float(input("aldığınız mesafe nedir?:"))

benzinFiyat=39.35
dizelFiyat=41.71
lpgFiyat=20.28

print("yakıt masrafınız:")

if(yakıtTipi=="benzin"):
    print(mesafe*benzinFiyat)
    
    elif(yakıtTipi=="dizel"):
    print(mesafe*dizelFiyat)
    
    elif(yakıtTipi=="lpg"):
    print(mesafe*lpgFiyat)
    
    else:
    print("bi sorun oluştu üzgünüz")




