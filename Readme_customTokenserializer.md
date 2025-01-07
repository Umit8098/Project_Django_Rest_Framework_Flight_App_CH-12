

```py
REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'users.serializers.CustomTokenSerializer',
}
```

- şimdi test edelim, postmanden login olalım ve bize ne verisi dönecek bakalım;

- TOKEN_SERIALIZER ı bir türlü override edemedim! 
- token verisinin yanında user verisi dönmüyor!
- kendi TokenSerializer class ını çalıştırıyor!
- benim override ettiğim CustomTokenSerializer ı çalıştırmıyor! Neden? -> 
- dj-rest-auth==2.2.6  paketini bu versiyonu ile çalıştırdığımda bu işlemleri yapabiliyorum. 
- Ancak bir üst versiyonu olan  dj-rest-auth==3.0.0   yüklediğimde bu işlem çalışmıyor. Paketi eski versiyonuna geri çevirdim, artık çalışıyor.

```py
- pip uninstall dj-rest-auth==4.0.1
- pip install dj-rest-auth==2.2.6
```

- Sebebi ise sonraki paket güncellemesinde settings.py da yazdığımız "REST_AUTH_SERIALIZERS"  değişken ismi "REST_AUTH" olarak güncellenmiş. Değişken ismini yenisi ile değiştirirsek çalışıyor. 