from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog
from cv2 import cv2
import sys
import numpy as np

class ConvexityDetection:
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
                a=ConvexityDetectAl(self.filename)
                a.convexityDetectionImg()
                
                myImage2.place_forget()
                if(self.video==1):
                    imgFirst=Image.open("img/noImage.png")
                else:
                    imgFirst=Image.open("img/dist/disbukey.png")
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
        self.root.title("Convexity Detects")
        self.root.configure(background='#2C073E')
        
    #</---Form Ayarları--->


    #<---Resimlerin Eklenmesi--->

        mainmenu=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\home2.png"))
        find=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\search.png"))
        noImage=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\noImage.png"))
        fotoImage=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\foto2.png"))
       

    #</---Resimlerin Eklenmesi--->

    #<---Butonların Oluşturulması--->

        menu=Button(self.root,image=mainmenu,bd=0,highlightthickness=0,command=MainmenuFonk,width=150,height=50,bg="#2C073E",fg="#000000")
        menu.image=mainmenu
        menu.place(x=10,y=20)

        findButton=Button(self.root,image=find,bd=0,highlightthickness=0,command=openFileImg,width=24,height=24,bg="#2C073E",fg="#000000")
        findButton.image=find
        findButton.place(x=980,y=100)

        imageButton=Button(self.root,image=fotoImage,bd=0,highlightthickness=0,command=imgDetect,bg="#2C073E",fg="#ffffff")
        imageButton.image=fotoImage
        imageButton.place(x=120,y=575)

        

    #</---Butonların Oluşturulması--->

    #<---Labelların Oluşturulması--->

        title=Label(self.root,text="CONVEXITY DETECTS",font = "Arial 12 bold ",bg="#2C073E",fg="#c1bdbd")
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

class ConvexityDetectAl:
    def __init__(self,filename):
        self.filename=filename

    def convexityDetectionImg(self):
        try:
            img = cv2.imread(self.filename)
            img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            ret, thresh = cv2.threshold(img_gray, 127, 255,0)
            contours,hierarchy = cv2.findContours(thresh,2,1)
            cnt = contours[0]

            hull = cv2.convexHull(cnt,returnPoints = False)
            defects = cv2.convexityDefects(cnt,hull)

            for i in range(defects.shape[0]):
                s,e,f,d = defects[i,0]
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])
                cv2.line(img,start,end,[0,255,0],2)
                cv2.circle(img,far,5,[0,0,255],-1)

            cv2.imwrite('img/dist/disbukey.png',img, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            pass

    