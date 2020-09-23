import urllib.request as URL
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'E:\OCR\tesseract.exe'
import PIL.Image
from tkinter import *


def DownloadImage(url,file_path,file_name):

    fullPath = file_path + file_name + '.png'
    
    URL.urlretrieve(url,fullPath)

    return fullPath

def Convert():
    Url = urlString.get()

    Image_name = nameString.get()

    path = DownloadImage(Url,Image_Path,Image_name)
    
    img = PIL.Image.open(path)

    text = tess.image_to_string(img)

    Text3 = Label(text = "Converted Text : ").grid(row=3,column=5)

    Text4 = Label(text = text,bg = "White").grid(row=4,column=5)


root = Tk()

root.title("ImageToTextConvertor")

root.geometry("600x400")

Text1 = Label(text = "Image URL : ").grid(row=0,column=0)

urlString = StringVar()

Entry1 = Entry(root,textvariable = urlString).grid(row = 0,column = 1)

Text2 = Label(text = "Image Name : ").grid(row=1,column=0)

nameString = StringVar()

Entry2 = Entry(root,textvariable = nameString).grid(row = 1,column = 1)

But1 = Button(text = "Convert",command = Convert).grid(row = 2,column = 1)

Image_Path = "D:\Python Projects\Images\ "

root.mainloop()