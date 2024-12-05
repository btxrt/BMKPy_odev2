
vize1=float(input("1. vize notunuz nedir?"))
vize2=float(input("2. vize notunuz nedir?"))
final=float(input("final notunuz nedir?"))

notOrtalaması=(vize1*0.3+vize2*0.3+final*0.4)

print("harf notunuz= ")

if(100>=notOrtalaması>=90):
    print("AA")

elif(89>=notOrtalaması>=80):
    print("BA")

elif(79>=notOrtalaması>=70):
    print("BB")

elif(69>=notOrtalaması>=60):
    print("CB")

elif(59>=notOrtalaması>=60):
    print("CC")

elif(49>=notOrtalaması>=40):
    print("DC")

else:
    print("başarısız")



