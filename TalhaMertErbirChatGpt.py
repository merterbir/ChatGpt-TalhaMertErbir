import openai

openai.api_key = "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"

def sifreTest():   
        print("------------------------------------------------------------------------------------------")
        print("Hangi şifrenin güçlü olduğunu sorgulamak için şifreleri virgül (,) ile ayırarak yazınız. Şifreler minimum 6 karakter olmalıdır.")
        print("------------------------------------------------------------------------------------------")
        sifreler2= input()
        sifreler = sifreler2.split(",")
        if len(sifreler)>1:
            bayrak = True
            for sifre in sifreler:
                if len(sifre) <6:
                    bayrak = False
                    yanlisSifre = sifre
                    break
            yeniSifreler =""
            for sifre in sifreler:
                yeniSifreler = yeniSifreler+sifre+" "

            if bayrak:
                result2 = openai.Completion.create(
                        model="text-davinci-003",
                        prompt="Bu şifrelerden hangisi daha güçlüdür? Neden? Şifreler:"+yeniSifreler,
                        max_tokens=1000  
                        )           
                print(result2["choices"][0]["text"])
            else:
                print(50*"\n")
                print(yanlisSifre+" Bu şifre 6 karakterden az lütfen şifreleri tekrar yazınız.")
                sifreTest()
        else:
                print(50*"\n")
                print("Şifreleri virgül ile ayırınız ve en az iki adet şifre giriniz.")
                sifreTest()


def start():           
    print("------------------------------")
    print("1- Şifre önerisi")
    print("2- Hangi şifre daha güçlü")
    print("------------------------------")
    deger = input()

    if deger == "1":
        
        deger1()
    if deger == "2":
        print(50*"\n")
        sifreTest()
    else:
        print("Yanlış bir seçim yaptınız. Lütfen tekrar bir seçim yapınız.")       
        start()

def deger1():
            
            print("------------------------------------------------------------------------------------------")
            print("1- Random Şifre oluştur")
            print("2- İçinde geçmesini istediğiniz kelime ile  şifre oluştur.")
            print("------------------------------------------------------------------------------------------")
            deger2= input()
            if deger2=="1":
                result = openai.Completion.create(
                    model="text-davinci-003",
                    prompt="Bana bir adet güçlü bir şifre oluştur açıklama yapmadan sadece şifreyi yazdır.",
                    max_tokens=500  
                    )           
                print(result["choices"][0]["text"]) 
                exit()
            elif deger2=="2":
                print(50*"\n")
                print("------------------------------------------------------------------------------------------")
                print("İçerisinde geçmesini istediğiniz kelimeyi yazınız")
                print("------------------------------------------------------------------------------------------")
                deger3= input()
                deger3=deger3.replace(" ","")
                result = openai.Completion.create(
                    model="text-davinci-003",
                    prompt="İçerisinde "+deger3+" geçen güçlü bir şifre önerisinde bulunur musun? Neden güçlü olduğunu tanımla.",
                    max_tokens=500  
                    )           
                print(result["choices"][0]["text"]) 
                exit()
            else:
                print("Yanlış bir seçim yaptınız. Lütfen tekrar bir seçim yapınız.")       
                deger1()
            
start()

