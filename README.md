# Gaussian ve Median Filtrelerinin Gürültü Giderme Başarımının Karşılaştırmalı Analizi

## 📊 Temel Bulgular

Proje sonucunda elde edilen en önemli bulgular şunlardır:

* [cite_start]**Median Filtresi**, "Tuz-Biber" gürültüsünü temizlemede (özellikle hücresel dokuda **0.968 SSIM**  skoruyla) Gaussian filtresine göre ezici bir üstünlük sağlamıştır.
* [cite_start]**Gaussian Filtresi**, "Gaussian Gürültü" ve "Lifli Doku"  [cite_start]senaryosunda (0.794 SSIM ) en iyi sonucu vermiştir.
* Filtre performansı, görüntü yapısına bağlıdır. [cite_start]Gaussian filtresi, hassas hücresel yapıları  [cite_start]bulanıklaştırarak yapısal benzerliği (0.345 SSIM ) ciddi şekilde bozmuştur.

## 📁 Proje Yapısı

* `main.py`: Ana Python betiği. [cite_start]Veri setlerini okur, gürültü ekler, filtreleri uygular ve metrikleri  hesaplayıp konsola yazdırır.
* [cite_start]`1.pdf`: Projenin tüm detaylarını içeren vize raporu .
* `.gitignore`: Python'a özgü gereksiz dosyaları (örn: `__pycache__`) görmezden gelir.

## 💾 Veri Seti

[cite_start]Bu projede kullanılan "NuSec and MiDeSec (Dataset)"  veri seti, Kaggle üzerinden temin edilmiştir. [cite_start]Kodun çalışması için bu veri setinin indirilmesi ve `dataset1/`  [cite_start]ve `dataset2/`  klasörlerine ayrılması gerekmektedir.

* [cite_start]**Veri Seti Kaynağı:** [https://www.kaggle.com/datasets/sonianmty/nusec-and-midesec](https://www.kaggle.com/datasets/sonianmty/nusec-and-midesec) 

## 🛠️ Gereksinimler

Projenin çalıştırılması için aşağıdaki Python kütüphaneleri gereklidir:

* `opencv-python`
* `scikit-image`
* `numpy`
* `matplotlib` (Görselleştirme için)

Bu kütüphaneleri `pip` kullanarak yükleyebilirsiniz:
```bash
pip install opencv-python scikit-image numpy matplotlib
