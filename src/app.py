import os
import shutil

def organize_files(target_folder):
    if not os.path.exists(target_folder):
        print("❌ Hedef klasör bulunamadı.")
        return

    extensions = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Code": [".py", ".java", ".cpp"],
        "Archives": [".zip", ".rar"],
        "Others": []
    }

    for file in os.listdir(target_folder):
        file_path = os.path.join(target_folder, file)
        if os.path.isfile(file_path):
            moved = False
            for folder, exts in extensions.items():
                if any(file.lower().endswith(ext) for ext in exts):
                    dest_folder = os.path.join(target_folder, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    moved = True
                    break
            if not moved:
                others_folder = os.path.join(target_folder, "Others")
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(others_folder, file))

    print("✅ Dosyalar başarıyla sınıflandırıldı.")

if _name_ == "_main_":
    folder = input("📁 Hangi klasörü düzenlemek istiyorsunuz?: ")
    organize_files(folder.strip())
