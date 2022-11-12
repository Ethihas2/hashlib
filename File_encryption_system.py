from tkinter import *
from tkinter import filedialog as fd
import hashlib

root=Tk()
root.geometry("250x190")
root.config(bg="AntiqueWhite1")

def apply_md5():
    print("MD5 function")
    text_file = fd.askopenfilename(title="Open text files",filetypes=(("Text Files","*.txt"),))
    print(text_file)

    read_file = open(text_file,'r')
    paragraph = read_file.read()
    final_result = hashlib.md5(paragraph.encode())
    
    file_hexed = final_result.hexdigest()
    print(file_hexed)

    md5_file = open("md5.txt",'w')
    md5_file.write(file_hexed)
    
    
def apply_sha256():
    print("SHA function")   
    text_file = fd.askopenfilename(title="Open text files",filetypes=(("Text Files","*.txt"),))
    print(text_file)

    read_file = open(text_file,'r')
    paragraph = read_file.read()
    final_result = hashlib.sha256(paragraph.encode())
    
    file_hexed = final_result.hexdigest()
    print(file_hexed)

    sha256_file = open("sha256.txt",'w')
    sha256_file.write(file_hexed)
    
    
btn=Button(root, text="Apply MD5",command=apply_md5,bg="orange",relief=FLAT)
btn.place(relx=0.3,rely=0.5, anchor=CENTER)
btn1=Button(root, text="Apply SHA256",command=apply_sha256,bg="orange",relief=FLAT)
btn1.place(relx=0.7,rely=0.5, anchor=CENTER)
root.mainloop()