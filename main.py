import tkinter as tk
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
import base64

window = tk.Tk()
window.title("Image in Tkinter")
window.minsize(200, 400)
window.configure(bg='grey')
resim_yolu = Image.open('resim.png').resize((100, 75), None)
resim_yolu_tk = ImageTk.PhotoImage(resim_yolu)
image_label = tk.Label(window, image=resim_yolu_tk)
image_label.grid(row=0, column=1)

# LABEL_ENTER_TITLE
label_title = tk.Label(text="Enter Your Title", font=("Arial"))
label_title.config(fg="black", bg="grey")
label_title.grid(row=1, column=1)
# ENTRY_TITLE
entry_title = tk.Entry(width=20)
entry_title.grid(row=2, column=1)

# LABEL_ENTER_MESAGE_TITLE
label_secret = tk.Label(text="Enter Your Secret", font=("Arial"))
label_secret.config(fg="black", bg="grey")
label_secret.grid(row=3, column=1)
# TEXT_MESSAGE
text_secret = tk.Text(window, height=10, width=200)
text_secret.grid(row=4, column=1)

# LABEL_ENTER_MASTER
label_master = tk.Label(text="Enter Master Key", font=("Arial"))
label_master.config(fg="black", bg="grey")
label_master.grid(row=5, column=1)
# ENTRY_MASTER
entry_master = tk.Entry(width=40)
entry_master.grid(row=6, column=1)

custom_key = None  # Anahtar başlangıçta tanımlanmamış

def set_custom_key():
    global custom_key
    user_key = entry_master.get().encode()

    # Anahtar uzunluğunu kontrol et
    if len(user_key) != 32:
        print("Anahtar 32 byte olmalıdır.")
        return

    custom_key = user_key

def sifreleme_islemi():
    '''
    if custom_key is None:
        print("Anahtar belirtilmedi. Lütfen anahtarınızı girin.")
        return

    message_text = text_secret.get('1.0', tk.END).encode()
    f = Fernet(custom_key)
    encrypted_message = f.encrypt(message_text)
    print(encrypted_message)
    with open("key.txt", mode="a") as belge:
        belge.write(f"\n{entry_title.get()}\n {encrypted_message}")
    '''

def sifrecozme_islemi():
    if custom_key is None:
        print("Anahtar belirtilmedi. Lütfen anahtarınızı girin.")
        return

    encrypted_message = text_secret.get('1.0', tk.END).encode()
    f = Fernet(custom_key)
    decrypted_message = f.decrypt(encrypted_message)

    print("<-----> Şifresi Çözülmüş Mesaj <----->")
    print(decrypted_message.decode())  # Şifresi çözülen metni yazdırın

# Anahtarı belirleme butonu
btnSetKey = tk.Button(window, text="Anahtar Belirle", command=set_custom_key)
btnSetKey.grid(row=7, column=1)

# SAVE & ENCRYPT BUTTON
btnKaydetSifrele = tk.Button(window, text="Kaydet ve Şifrele", command=sifreleme_islemi)
btnKaydetSifrele.grid(row=8, column=1)

# DECRYPT BUTTON
btnSifreCoz = tk.Button(window, text="Şifreyi Çöz", command=sifrecozme_islemi)
btnSifreCoz.grid(row=9, column=1)

window.mainloop()
