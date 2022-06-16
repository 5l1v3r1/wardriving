# wardriving

Python Wardriving aracı

Aracın kötü niyetli kullanılmasında şahsım sorumlu tutulamaz.

ssidBul.py TP-LINK TL WN722N aracılığıyla test edilmiştir.

konum.py için Selenium 3.11.0 ve Firefox 59.0.2 kullanılmıştır. Firefox geckodriver kodların olduğu dizinde bulunmaktadır.

SSID ve MAC isimleri ve konum bilgileri test ortamında oluşturulup değiştirilmiştir.

ssidBul.py ve konum.py eş zamanlı olarak çalıştırılmalıdır.

ssidBul.py örnek çıktısı:

20 March 2018 11:48PM|9c:b2:b2:11:12:13|ECFJ3M

20 March 2018 11:48PM|c0:25:e9:11:12:13|T7068

konum.py çalıştırılması esnasında konum bilgisine izin verilmesi hakkındaki ekran görüntüsü aşağıdaki şekildedir:

<img src="https://github.com/anil-yelken/wardriving/blob/main/geody1.JPG">

konum bilgisinin aldığına dair ekran görüntüsü aşağıdaki şekildedir:

<img src="https://github.com/anil-yelken/wardriving/blob/main/geody2.JPG">

konum.py örnek çıktısı:

lat=38.8333635|lon=34.759741899|20 March 2018 11:47PM

lat=38.8333635|lon=34.759741899|20 March 2018 11:48PM

lat=38.8333635|lon=34.759741899|20 March 2018 11:48PM

lat=38.8333635|lon=34.759741899|20 March 2018 11:48PM

lat=38.8333635|lon=34.759741899|20 March 2018 11:48PM

lat=38.8333635|lon=34.759741899|20 March 2018 11:49PM

lat=38.8333635|lon=34.759741899|20 March 2018 11:49PM

Yapılan veri toplama işlemlerinde sonra  wardriving.py çalıştırılması sonucu aşağıdaki çıktı elde edilmektedir:

lat=38.8333635|lon=34.759741899|20 March 2018 11:48PM|9c:b2:b2:11:12:13|ECFJ3M

lat=38.8333635|lon=34.759741899|20 March 2018 11:48PM|c0:25:e9:11:12:13|T7068
