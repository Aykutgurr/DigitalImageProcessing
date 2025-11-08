# Gaussian ve Median Filtrelerinin Gürültü Giderme Performansının Karşılaştırılması

Bu proje, Sayısal Görüntü İşleme dersi vize ödevi kapsamında hazırlanmıştır. Çalışmanın amacı, iki farklı gürültü tipine (Gaussian ve Tuz-Biber) maruz bırakılan iki farklı doku tipi (hücresel ve lifli) üzerinde **Gaussian** ve **Median** filtrelerinin gürültü giderme performansını karşılaştırmaktır.

Projenin detayları, bulguları ve tartışmaları [`1.pdf`](1.pdf) rapor dosyasında yer almaktadır.

---

## 📊 Temel Bulgular

Proje sonucunda elde edilen en önemli bulgular:

* **Median Filtresi**, "Tuz-Biber" gürültüsünü temizlemede özellikle hücresel dokuda (**0.968 SSIM**) Gaussian filtresine göre belirgin bir üstünlük sağlamıştır.
* **Gaussian Filtresi**, "Gaussian Gürültü" ve "Lifli Doku" senaryosunda (**0.794 SSIM**) en iyi sonucu vermiştir.
* Filtre performansı, görüntü yapısına bağlı olarak değişmektedir. Gaussian filtresi, hassas hücresel yapıları bulanıklaştırarak yapısal benzerliği (**0.345 SSIM**) ciddi şekilde bozmuştur.

---

## 📁 Proje Dosya Yapısı

* `main.py`: Ana Python betiği. Veri setlerini okur, gürültü ekler, filtreleri uygular ve metrikleri hesaplayıp konsola yazdırır.
* `1.pdf`: Projenin detaylarını ve bulgularını içeren vize raporu.
* `.gitignore`: Python'a özgü gereksiz dosyaları (örn: `__pycache__`) görmezden gelir.

---

## 💾 Veri Seti

Projede kullanılan **NuSec ve MiDeSec** veri seti Kaggle üzerinden temin edilmiştir. Kodun çalışabilmesi için veri setinin indirilip `dataset1/` ve `dataset2/` klasörlerine ayrılması gerekmektedir.

* **Veri Seti Kaynağı:** [NuSec and MiDeSec (Kaggle)](https://www.kaggle.com/datasets/sonianmty/nusec-and-midesec)

---

## 🛠️ Gereksinimler

Projenin çalıştırılması için aşağıdaki Python kütüphaneleri gereklidir:

* `opencv-python`
* `scikit-image`
* `numpy`
* `matplotlib` (görselleştirme için)

Kütüphaneleri yüklemek için:

```bash
pip install opencv-python scikit-image numpy matplotlib
