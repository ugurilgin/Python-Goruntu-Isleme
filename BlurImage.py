from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog
from cv2 import cv2
import sys
import numpy as np


class ImageSmoothing:
    def __init__(self,master):

        def MainmenuFonk():
            master.update()
            master.deiconify()
            self.Quit()

        def openFileImg():
            try:
                filename=filedialog.askopenfilename(initialdir="/img/", title="Please Choose an Image or Video File",filetypes=(("JPG File", "*.jpg"),("PNG File", "*.png"),("MP4 File", "*.mp4"),("AVI File", "*.avi")))
                myImage.place_forget()
                imgFirst=Image.open(filename)
                imgLast=imgFirst.resize((450, 400),Image.ANTIALIAS)
                myImg=ImageTk.PhotoImage(imgLast)
                myImageLast=Label(self.root,image=myImg,bg="#2C073E",fg="#ffffff",width=450,height=400)
                myImageLast.image=myImg
                myImageLast.place(x=50,y=145)
                Path.config(text=filename)
                self.video=0
                self.filename=filename
            except:
                noImage=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\noImage.png"))
                myImageLast=Label(self.root,image=noImage,bg="#2C073E",fg="#ffffff",width=450,height=400)
                myImageLast.image=noImage
                myImageLast.place(x=50,y=145)
                Path.config(text=filename)
                myImage2.place_forget()
                myImage2Last=Label(self.root,image=noImage,bg="#2C073E",fg="#ffffff",width=450,height=400)
                myImage2Last.image=noImage
                myImage2Last.place(x=650,y=145)
                self.video=1
                self.filename=filename

        def imgDetect():
            try:
                a=ImageSmoothingAl(self.filename)
                a.imageSmoothingImg()
                
                myImage2.place_forget()
                if(self.video==1):
                    imgFirst=Image.open("img/noImage.png")
                else:
                    imgFirst=Image.open("img/dist/blur.png")
                imgLast=imgFirst.resize((450, 400),Image.ANTIALIAS)
                Myimg=ImageTk.PhotoImage(imgLast)
                myImageLast=Label(self.root,image=Myimg,bg="#2C073E",fg="#ffffff",width=450,height=400)
                myImageLast.image=Myimg
                myImageLast.place(x=650,y=145)
            except:
                pass

        def imgGaussianDetect():
            try:
                a=ImageSmoothingAl(self.filename)
                a.imageSmoothingGaussianImg()
                
                myImage2.place_forget()
                if(self.video==1):
                    imgFirst=Image.open("img/noImage.png")
                else:
                    imgFirst=Image.open("img/dist/gaussian.png")
                imgLast=imgFirst.resize((450, 400),Image.ANTIALIAS)
                myImg=ImageTk.PhotoImage(imgLast)
                myImageLast=Label(self.root,image=myImg,bg="#2C073E",fg="#ffffff",width=450,height=400)
                myImageLast.image=myImg
                myImageLast.place(x=650,y=145)
            except:
                pass      

        def imgMedianDetect():
            try:
                a=ImageSmoothingAl(self.filename)
                a.imageSmoothingMedianImg()
                
                myImage2.place_forget()
                if(self.video==1):
                    imgFirst=Image.open("img/noImage.png")
                else:
                    imgFirst=Image.open("img/dist/median.png")
                imgLast=imgFirst.resize((450, 400),Image.ANTIALIAS)
                myImg=ImageTk.PhotoImage(imgLast)
                myImageLast=Label(self.root,image=myImg,bg="#2C073E",fg="#ffffff",width=450,height=400)
                myImageLast.image=myImg
                myImageLast.place(x=650,y=145)
            except:
                pass            
            
    #<---Form Ayarları--->

        self.root = Toplevel()
        self.root.wm_iconbitmap('img/iconum.ico')
        self.root.geometry("1266x692+0+0")
        self.root.maxsize(1366,768)
        self.root.title("Image Blurring (Image Smoothing)")
        self.root.configure(background='#2C073E')
        
    #</---Form Ayarları--->


    #<---Resimlerin Eklenmesi--->

        mainmenu=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\home2.png"))
        find=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\search.png"))
        noImage=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\noImage.png"))
        smooth=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\smooth.png"))
        median=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\median.png"))
        gaussian=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\gaussian.png"))

    #</---Resimlerin Eklenmesi--->

    #<---Butonların Oluşturulması--->

        menu=Button(self.root,image=mainmenu,bd=0,highlightthickness=0,command=MainmenuFonk,width=150,height=50,bg="#2C073E",fg="#000000")
        menu.image=mainmenu
        menu.place(x=10,y=20)

        bulButton=Button(self.root,image=find,bd=0,highlightthickness=0,command=openFileImg,width=24,height=24,bg="#2C073E",fg="#000000")
        bulButton.image=find
        bulButton.place(x=980,y=100)

        imageButton=Button(self.root,image=smooth,bd=0,highlightthickness=0,command=imgDetect,bg="#2C073E",fg="#ffffff")
        imageButton.image=smooth
        imageButton.place(x=120,y=575)

        videoButton=Button(self.root,image=gaussian,bd=0,highlightthickness=0,command=imgGaussianDetect,bg="#2C073E",fg="#000000")
        videoButton.image=gaussian
        videoButton.place(x=220,y=575)

        streamButton=Button(self.root,image=median,bd=0,highlightthickness=0,command=imgMedianDetect,bg="#2C073E",fg="#ffffff")
        streamButton.image=median
        streamButton.place(x=320,y=575)

    #</---Butonların Oluşturulması--->

    #<---Labelların Oluşturulması--->

        title=Label(self.root,text="IMAGE BLURRING (IMAGE SMOOTHING)",font = "Arial 12 bold ",bg="#2C073E",fg="#c1bdbd")
        title.place(x=463,y=30)

        fileLbl=Label(self.root,text="File Path :",bg="#2C073E",fg="#ffffff")
        fileLbl.place(x=55,y=100)

        Path=Label(self.root,text="Please Choose a File ...",bg="#2C073E",fg="#ffffff")
        Path.place(x=160,y=100)
        
        myImage=Label(self.root,image=noImage,bg="#2C073E",fg="#ffffff",width=450,height=400)
        myImage.place(x=50,y=145)

        myImage2=Label(self.root,image=noImage,bg="#2C073E",fg="#ffffff",width=450,height=400)
        myImage2.place(x=650,y=145)

        

    #</---Labellerın Oluşturulması--->


        self.root.mainloop()
    
    #<---Fonksiyonların Tanımlanması--->

    def Quit(self):
        self.root.destroy()

    #</---Fonksiyonların Tanımlanması--->

class ImageSmoothingAl:
    def __init__(self,filename):
        self.filename=filename

    def imageSmoothingImg(self):
        try:
            img = cv2.imread(self.filename)
            blur = cv2.blur(img,(5,5))
            cv2.imwrite('img/dist/blur.png',blur, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            pass

    def imageSmoothingGaussianImg(self):
        try:
            img = cv2.imread(self.filename)
            blur = cv2.GaussianBlur(img,(5,5),0)
            cv2.imwrite('img/dist/gaussian.png',blur, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            pass

    def imageSmoothingMedianImg(self):
        try:
            img = cv2.imread(self.filename)
            blur = cv2.medianBlur(img,5)
            cv2.imwrite('img/dist/median.png',blur, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            pass
        