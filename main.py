import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import base64

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


window = tkinter.Tk()
window.title("Secret NOTES")
window.config(padx=100, pady=100)
window.minsize(width=300, height=550)


def save_encrpt_notes():
    title = wusers_inlput.get()

    message = info_text.get("1.0" , END)
    mastelr_inlpu = master_inlput.get()

    if len(title) == 0 or  len(message) == 0 or len(mastelr_inlpu) == 0 :
        messagebox.showwarning("Eror ",message="Plase enter all info.")
    else:
        #ecryption
        encrtyp_savedd = encode( mastelr_inlpu,message)

        try:
            with open("mysecretly.txt" , "a") as data_file:
              data_file.write(f"\n{title}\n{encrtyp_savedd}")
        except FileNotFoundError :
             with open("mysecretly.txt", "a") as data_file:
                 data_file.write(f"\n{title}\n{encrtyp_savedd}")
        finally:
             wusers_inlput.delete(0, END)
             info_text.delete("1.0",END)
             master_inlput.delete(0,END)



def encrypted_keydecode():
    text_decode = info_text.get("1.0",END)
    master_key_decode= master_inlput.get()

    if  len(text_decode) == 0 or  len(master_key_decode) == 0 :

        messagebox.showwarning("Eror" , message="PLASE ENTER ALL İNFO ")
    else :

        try:
             decrepyrtrd_message= decode( master_key_decode,text_decode)
             info_text.delete("1.0",END)
             info_text.insert("1.0",decrepyrtrd_message)
        except :
            messagebox.showwarning("Eror !!!" ,message="plase enter encrypted text !!!!")




# ui 1.basamak
wusers_inlput = tkinter.Label(text="Enter your title", font=('Arial', 13, 'italic'), )
wusers_inlput.pack()
wusers_inlput = tkinter.Entry(width=30)
wusers_inlput.pack()

wusers_inlput_two = tkinter.Label(text="Enter your secret")
wusers_inlput_two.pack()

info_text= Text(width=20 , height=10)
info_text.pack()
# master key
master_inlput = tkinter.Label(text="Entry master key")
master_inlput.pack(side="bottom")
master_inlput = tkinter.Entry(width=20)
master_inlput.place(x=33, y=350)
# encrypt
master_key_button = tkinter.Button(width=11, text="Save&Encrypt",command=save_encrpt_notes)
master_key_button.place(x=43, y=370)
# decrypte
decrypte_button = tkinter.Button(width=6, text="Decrypte",command= encrypted_keydecode)
decrypte_button.place(x=59, y=400)

my_image = PhotoImage(file='C:/Users/Abdullah Atılgan/Documents/yeniKaliSECRETödev.png')
lbl_icopng = Label(image=my_image)
lbl_icopng.place(x=63, y=-60)

window.mainloop()
