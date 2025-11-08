import cv2
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import mean_squared_error as mse
import os
import glob

# ----------------------------------------------------------------------------
# 1. GÜRÜLTÜ EKLEME FONKSİYONLARI
# ----------------------------------------------------------------------------

def add_gaussian_noise(image, mean=0, var=0.01):
    image_float = image.astype(np.float32) / 255.0
    gauss = np.random.normal(mean, var**0.5, image_float.shape)
    noisy = np.clip(image_float + gauss, 0, 1)
    return (noisy * 255).astype(np.uint8)

def add_salt_and_pepper_noise(image, amount=0.05):
    noisy_image = np.copy(image)
    row, col = noisy_image.shape[:2]
    ch = 1 if image.ndim == 2 else image.shape[2]
    num_salt = int(np.ceil(amount * row * col * 0.5))
    num_pepper = int(np.ceil(amount * row * col * 0.5))

    # Tuz (beyaz)
    coords = [np.random.randint(0, i - 1, num_salt) for i in (row, col)]
    if ch == 1:
        noisy_image[coords[0], coords[1]] = 255
    else:
        noisy_image[coords[0], coords[1], :] = 255

    # Biber (siyah)
    coords = [np.random.randint(0, i - 1, num_pepper) for i in (row, col)]
    if ch == 1:
        noisy_image[coords[0], coords[1]] = 0
    else:
        noisy_image[coords[0], coords[1], :] = 0

    return noisy_image

# ----------------------------------------------------------------------------
# 2. METRİK HESAPLAMA
# ----------------------------------------------------------------------------

def calculate_metrics(image_clean, image_processed):
    is_color = image_clean.ndim == 3
    psnr_value = psnr(image_clean, image_processed, data_range=255)
    ssim_value = ssim(image_clean, image_processed, data_range=255, channel_axis=2 if is_color else None)
    mse_value = mse(image_clean, image_processed)
    rmse_value = np.sqrt(mse_value)
    return psnr_value, ssim_value, rmse_value

# ----------------------------------------------------------------------------
# 3. VERİ SETİ İŞLEME (HIZLANDIRILMIŞ)
# ----------------------------------------------------------------------------

def process_dataset(folder_path, dataset_name, resize_to=(512, 512)):
    print(f"\n--- VERİ SETİ İŞLENİYOR: {dataset_name} ---")

    image_files = glob.glob(os.path.join(folder_path, '*.tif*'))
    if not image_files:
        print(f"HATA: '{folder_path}' içinde hiç .tif dosyası bulunamadı.")
        return None

    metrics_gg, metrics_gm, metrics_sg, metrics_sm = [], [], [], []

    for image_file in image_files:
        try:
            clean_image = cv2.imread(image_file, cv2.IMREAD_UNCHANGED)
            if clean_image is None:
                print(f"Uyarı: {image_file} yüklenemedi, atlanıyor.")
                continue

            # 💨 HIZ İÇİN GÖRÜNTÜ KÜÇÜLTÜLÜYOR
            clean_image = cv2.resize(clean_image, resize_to)

            # Gürültüler
            noisy_gauss = add_gaussian_noise(clean_image)
            noisy_sp = add_salt_and_pepper_noise(clean_image)

            # Filtreler
            filtered_gg = cv2.GaussianBlur(noisy_gauss, (5, 5), 0)
            filtered_gm = cv2.medianBlur(noisy_gauss, 5)
            filtered_sg = cv2.GaussianBlur(noisy_sp, (5, 5), 0)
            filtered_sm = cv2.medianBlur(noisy_sp, 5)

            # Metrikler
            metrics_gg.append(calculate_metrics(clean_image, filtered_gg))
            metrics_gm.append(calculate_metrics(clean_image, filtered_gm))
            metrics_sg.append(calculate_metrics(clean_image, filtered_sg))
            metrics_sm.append(calculate_metrics(clean_image, filtered_sm))

        except Exception as e:
            print(f"Hata: '{image_file}' işlenemedi -> {e}")

    if not metrics_gg:
        print("HATA: Hiçbir görüntü işlenemedi.")
        return None

    avg_metrics_gg = np.mean(metrics_gg, axis=0)
    avg_metrics_gm = np.mean(metrics_gm, axis=0)
    avg_metrics_sg = np.mean(metrics_sg, axis=0)
    avg_metrics_sm = np.mean(metrics_sm, axis=0)

    print(f"{len(metrics_gg)} görüntü işlendi ✅")
    return [
        (dataset_name, "Gaussian Gürültü", "Gaussian Filtre", *avg_metrics_gg),
        (dataset_name, "Gaussian Gürültü", "Median Filtre", *avg_metrics_gm),
        (dataset_name, "Tuz-Biber Gürültü", "Gaussian Filtre", *avg_metrics_sg),
        (dataset_name, "Tuz-Biber Gürültü", "Median Filtre", *avg_metrics_sm)
    ]

# ----------------------------------------------------------------------------
# 4. ANA PROGRAM
# ----------------------------------------------------------------------------

dataset1_path = "dataset1"
dataset2_path = "dataset2"
report_table_data = []

for path, name in [(dataset1_path, "Veri Seti 1 (Hücresel)"),
                   (dataset2_path, "Veri Seti 2 (Lifli)")]:
    results = process_dataset(path, name, resize_to=(512, 512))
    if results:
        report_table_data.extend(results)

print("\n" + "="*80)
print("             Raporun Bulgular Tablosu için ORTALAMA Sonuçlar")
print("="*80)
print(f"{'Veri Seti':<22} | {'Gürültü Tipi':<18} | {'Filtre':<15} | {'PSNR ↑':<8} | {'SSIM ↑':<7} | {'RMSE ↓':<7}")
print("-"*80)

if not report_table_data:
    print("Hiçbir veri işlenemedi.")
else:
    for row in report_table_data:
        print(f"{row[0]:<22} | {row[1]:<18} | {row[2]:<15} | {row[3]:<8.2f} | {row[4]:<7.3f} | {row[5]:<7.2f}")

print("\nDeney Tamamlandı.")
