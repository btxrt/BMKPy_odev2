
vize1=float(input("1. vize notunuz nedir?"))
vize2=float(input("2. vize notunuz nedir?"))
final=float(input("final notunuz nedir?"))

notOrtalaması=(vize1*0.3+vize2*0.3+final*0.4)

print("harf notunuz= ")

if(100>=notOrtalaması>=90):
    print("AA")

elif(90>notOrtalaması>=80):
    print("BA")

elif(80>notOrtalaması>=70):
    print("BB")

elif(70>notOrtalaması>=60):
    print("CB")

elif(60>notOrtalaması>=50):
    print("CC")

elif(50>notOrtalaması>=40):
    print("DC")

else:
    print("DD")



