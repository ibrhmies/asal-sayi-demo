#girilen bir sayının asal sayı olup olmadığını kontrol ediniz

x = int(input("Sayı giriniz: "))
index = 0
for i in range(1,x+1):
    if(x % i == 0):
        index+=1
if (index > 2):
    print(f"Girdiğiniz {x} sayısı asal değildir.")        
elif(index == 2):
    print(f"Girdiğiniz {x} sayısı asaldır")        
else:
    print(f"Girdiğiniz {x} sayısı asal değildir.")