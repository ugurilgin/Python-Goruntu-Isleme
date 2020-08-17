# Python-Goruntu-Isleme
![logo](/SS/logo.png)

Python'daki Görüntü İşleme Araçlarının En Çok Kullanılanlarının Yer Aldığı Bir Masaüstü Uygulamadır.
* İşlenmek istenen görüntüler program klasöründen farklı bir klasörde bulunmalıdır
## Installation Guide
* 1-) Python 3 ü aşağıdaki linkten indirmelisiniz.
- https://www.python.org/downloads/
* 2-) Visual Studio Code Uygulamasını aşağıdaki linkten indirmelisiniz.
 - https://code.visualstudio.com
* 3-) Yolov3 data setinini aşağıdaki linkten indirmelisiniz.
- https://pjreddie.com/media/files/yolov3.weights
* İndirilen data setini program klasöründeki data klasörünün içine kopyalamanız gerekmektedir.
* 3-) Aşağıdaki komutlar yardımıyla  cmd ekranı üzerinden python kütüphanelerini indirmelisiniz.
~~~javascript
* pip install Pillow==2.2.2
* pip install opencv-python
* pip install numpy
* pip install matplotlib
* pip install pytesseract
~~~
* 4-) Proje klasöründe bulunan teseract-OCR uygulamasının kurulması gerekmektedir.
* 5-) Teseract.exe dosyasının ProgramFiles taki dosya yolunun program içerisindeki OCR/Teserract Path  kısmındaki file dialog penceresinden seçilme işlemi gerçekleştikten sonra kaydet butonuna basılıp dosya yolunun kaydedilmesi gerekmektedir.

* Programın çalıştırılması için klasörün içerisindeki commandline (cmd veya terminal ) açılır. Ve aşağıdaki komut kullanılır.
~~~javascript
* python3 main.py
~~~
* Veya visual code üzerinden main.py dosyası çalıştırılır.
## Kullanma Kılavuzu
* Program ilk açılışta sizi görsel bir arayüz ile karşılar. Bu Arayüz üzerinden işlem yapmak istediğiniz pencereyi görüntüleyebilirsiniz.
* ![logo](/SS/1.png)
* Face Detection Butonuna tıklanılarak .Yüz tanıma işlemlerinin yapılmasını sağlayan pencere açılır.Bu pencere üzerinden Resimden yüz algılama,Videodan yüz algılama,Webcam üzerinden yüz algılama işlemlerini gerçekleştirebilirsiniz.
* ![logo](/SS/2.png)
* ![logo](/SS/3.png)
* Object Detection Butonuna tıklanılarak .Nesne tanıma işlemlerinin yapılmasını sağlayan pencere açılır.Bu pencere üzerinden Resimden nesne algılama,Videodan nesne algılama,Webcam üzerinden nesne algılama işlemlerini gerçekleştirebilirsiniz.
* ![logo](/SS/4.png)
* ![logo](/SS/5.png)
* OCR butonuna tıklanarak.Seçilen resimdeki karakter algılanıp text biçimine dönüştürülür.Teseract-OCR konumunu kaydetmelisiniz.
* ![logo](/SS/6.png)
* Edge Detection Butonuna tıklanılarak .Köşe tanıma işlemlerinin yapılmasını sağlayan pencere açılır.Bu pencere üzerinden Resimden köşe algılama,Videodan köşe algılama,Webcam üzerinden köşe algılama işlemlerini gerçekleştirebilirsiniz.
* ![logo](/SS/7.png)
* ![logo](/SS/8.png)
* Image Gradient Butonuna tıklanılarak .Laplace ,SobelX ve SobelY algoritmaları kullanılarak resimde işlemler gerçekleştirilir.
* ![logo](/SS/9.png)
* ![logo](/SS/10.png)
* ![logo](/SS/11.png)
* Convexity Detect butonuna tıklanarak dış bükey barından görüntüler işlenir.
* ![logo](/SS/12.png)
* Smoothing Image butonuna tıklanarak resim üzerinde bulanıklaştırma işlemleri gerçekleştirilir .Gaussian ve Median algoritmaları kullanılarak resimde bulanıklaştırma örnekleri gerçekleştirilir.

* ![logo](/SS/13.png)
* Image  Pyramids butonuna tıklanarak iki resim birleştirilip birleşme yeri yumuşatılır ve tek bir görüntü gibi görünmesi sağlanır.

* ![logo](/SS/14.png)
## Hazırlayanlar
Uğur ILGIN
