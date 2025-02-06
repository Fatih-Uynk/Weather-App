import requests  # HTTP istekleri ile API'den veri çekmemezi sağlar
                # request modülü aynı zamanda JSON dönüşümü de sağlar

API_KEY = input("Lütfen API anahtarınızı girin :")


def hava_durumu_getir(sehir):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={API_KEY}&lang=tr&units=metric"

    response = requests.get(url)  # request.get(url) fonksiyonu ile API'ye "get" isteği gönderiliyor
                                  # API'den dönen yanıt response değişkenine atanıyor

    if response.status_code == 200:  # 200 -> başarılı bir isteği temsil ediyor, 404 veya başka bir hata kodu alındığında şehir bulunamamış olabilir.
        veri = response.json()  # API'den dönen yanıt JSON formatında olduğu için response.json() ile bir Python sözlüğüne çevrilir.
                                # veri değişkeni bu JSON verisini saklıyor
        sehir_adi = veri["name"] #API'den gelen şehir adını alır
        sicaklik = veri["main"]["temp"]#Hava sıcaklığını alır
        durum = veri["weather"][0]["description"] #Hava durumu açıklamasını alır

        print(f"{sehir_adi} için hava durumu:")
        print(f"Sıcaklık: {sicaklik}°C")
        print(f"Durum: {durum.capitalize()}")
    else:
        print("Şehir bulunamadı, lütfen doğru girdiğinizden emin olun.")


# Kullanıcıdan şehir bilgisi al
sehir_adi = input("Hava durumunu öğrenmek istediğiniz şehri girin: ")
hava_durumu_getir(sehir_adi)
