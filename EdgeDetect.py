from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog
from cv2 import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

class EdgeDetection:
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
                a=EdgeDetectAI(self.filename)
                a.edgeDetectionImg()
                
                myImage2.place_forget()
                if(self.video==1):
                    imgFirst=Image.open("img/noImage.png")
                else:
                    imgFirst=Image.open("img/dist/testEdge.jpg")
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
        self.root.title("Edge Detection")
        self.root.configure(background='#2C073E')
        
    #</---Form Ayarları--->


    #<---Resimlerin Eklenmesi--->

        mainmenu=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\home2.png"))
        find=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\search.png"))
        noImage=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\noImage.png"))
        fotoImage=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\foto2.png"))
        videoImage=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\video.png"))
        camImage=ImageTk.PhotoImage(Image.open(os.getcwd()+"\\img\\cam.png"))

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

        videoButton=Button(self.root,image=videoImage,bd=0,highlightthickness=0,command=self.faceVideo,bg="#2C073E",fg="#000000")
        videoButton.image=videoImage
        videoButton.place(x=220,y=575)

        streamButton=Button(self.root,image=camImage,bd=0,highlightthickness=0,command=self.faceWeb,bg="#2C073E",fg="#ffffff")
        streamButton.image=camImage
        streamButton.place(x=320,y=575)
       
    #</---Butonların Oluşturulması--->

    #<---Labelların Oluşturulması--->

        title=Label(self.root,text="EDGE DETECTION",font = "Arial 12 bold ",bg="#2C073E",fg="#c1bdbd")
        title.place(x=463,y=30)

        fileLbl=Label(self.root,text="File Path :",bg="#2C073E",fg="#ffffff")
        fileLbl.place(x=55,y=100)

        Path=Label(self.root,text="Please Choose a File ...",bg="#2C073E",fg="#ffffff")
        Path.place(x=160,y=100)
        
        myImage=Label(self.root,image=noImage,bg="#2C073E",fg="#ffffff",width=450,height=400)
        myImage.place(x=50,y=145)

        myImage2=Label(self.root,image=noImage,bg="#2C073E",fg="#ffffff",width=450,height=400)
        myImage2.place(x=650,y=145)

        description=Label(self.root,text="Please press ESC key to close a window",bg="#2C073E",fg="#ffffff")
        description.place(x=720,y=570)
        

    #</---Labellerın Oluşturulması--->


        self.root.mainloop()
    
    #<---Fonksiyonların Tanımlanması--->
    
    def faceVideo(self):
        try:
            a=EdgeDetectAI(self.filename)
            a.edgeDetectionVideo()
        except:
            pass

    def faceWeb(self):
        a=EdgeDetectAI(" ")
        a.edgeDetectionWebcam()

    def Quit(self):
        self.root.destroy()

    #</---Fonksiyonların Tanımlanması--->

class EdgeDetectAI:
    def __init__(self,filename):
        self.filename=filename

    def edgeDetectionImg(self):
        try:
            img = cv2.imread(self.filename)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 20, 30)
            edges_high_thresh = cv2.Canny(gray, 60, 120)
            images = np.hstack((edges, edges_high_thresh))
            cv2.imwrite('img/dist/testEdge.jpg',images, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.waitKey()
        except:
            pass
    def edgeDetectionVideo(self):
        try:
            cap = cv2.VideoCapture(self.filename)
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret == True:
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    edges = cv2.Canny(gray, 20, 30)
                    edges_high_thresh = cv2.Canny(gray, 60, 120)
                    images = np.hstack((edges, edges_high_thresh))
                    cv2.imshow('Edge Detect From Video', images)
                    k = cv2.waitKey(30) & 0xff
                    if k==27:
                        break
                else: 
                    break
            cap.release()
            cv2.destroyAllWindows()
        except:
            pass
    def edgeDetectionWebcam(self):
        try:
            cap = cv2.VideoCapture(0)
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret == True:
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    edges = cv2.Canny(gray, 20, 30)
                    edges_high_thresh = cv2.Canny(gray, 60, 120)
                    images = np.hstack(( edges, edges_high_thresh))
                    cv2.imshow('Edge Detect From Webcam', images)
                    k = cv2.waitKey(30) & 0xff
                    if k==27:
                        break
                else: 
                    break
            cap.release()
            cv2.destroyAllWindows()
        except:
            pass

        

        
