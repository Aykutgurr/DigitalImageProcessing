# Gaussian ve Median Filtrelerinin Gürültü Giderme Başarımının Karşılaştırmalı Analizi

[cite_start]Bu proje, Sayısal Görüntü İşleme dersi vize ödevi [cite: 374-385] kapsamında hazırlanmıştır. [cite_start]Çalışmanın amacı, iki farklı gürültü tipine (Gaussian ve Tuz-Biber) maruz bırakılan iki farklı yapıdaki (hücresel  [cite_start]ve lifli ) görüntü veri seti üzerinde Gaussian ve Median filtrelerinin gürültü giderme performansını karşılaştırmaktır.

[cite_start]Projenin tüm detayları, bulguları  [cite_start]ve tartışmaları [cite: 15-17] [cite_start]`1.pdf`  rapor dosyasında yer almaktadır.

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
