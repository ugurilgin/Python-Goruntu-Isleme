from tkinter import *
from FaceDetect import *
from ObjectDetect import *
from OCR import *
from EdgeDetect import *
from GradientDetect import *
from ConvexityDetect import *
from BlurImage import *
from ImagePyramid import *

class MainMenu:
    def __init__(self):
        self.window = Tk()
        self.window.wm_iconbitmap('img/iconum.ico')
        self.window.geometry("1366x700+1+1")
        self.window.maxsize(1366,768)
        self.window.title("Image Processing In Pyhon")
        self.window.configure(background='#050238')
    
        face=PhotoImage(file="img/face.png")
        obj=PhotoImage(file="img/obj.png")
        ocr=PhotoImage(file="img/ocr.png")
        edge=PhotoImage(file="img/kose.png")
        setting=PhotoImage(file="img/grad.png")
        convext=PhotoImage(file="img/hough.png")
        blur=PhotoImage(file="img/grab.png")
        pyramid=PhotoImage(file="img/piramit.png")
        avatar=PhotoImage(file="img/logo2.png")
        
        
        
        faceButton=Button(self.window,image=face,bd=0,highlightthickness=0,command=self.GoFaceDetection,width=169,height=162,bg="#F4192B",fg="#000000")
        faceButton.place(x=80,y=80)

        objectButton=Button(self.window,command=self.GoObjectDetection,image=obj,bd=0,highlightthickness=0,width=169,height=162,bg="#F4192B",fg="#000000")
        objectButton.place(x=300,y=80)

        OCR=Button(self.window,image=ocr,bd=0,highlightthickness=0,command=self.GoOCRDetection,width=168,height=162,bg="#F4192B",fg="#000000")
        OCR.place(x=520,y=80)

        edgeButton=Button(self.window,image=edge,bd=0,highlightthickness=0,command=self.GoEdgeDetection,width=168,height=162,bg="#F4192B",fg="#000000")
        edgeButton.place(x=740,y=80)
        

        gradientButton=Button(self.window,image=setting,bd=0,highlightthickness=0,command=self.GoGradientDetection,width=168,height=162,bg="#F4192B",fg="#000000")
        gradientButton.place(x=80,y=350)

        convexityButton=Button(self.window,image=convext,bd=0,highlightthickness=0,command=self.GoConvexityDetection,width=168,height=162,bg="#F4192B",fg="#000000")
        convexityButton.place(x=300,y=350)

        blurButton=Button(self.window,image=blur,bd=0,highlightthickness=0,command=self.GoBlurImage,width=168,height=162,bg="#F4192B",fg="#000000")
        blurButton.place(x=520,y=350)

        pyramidButton=Button(self.window,image=pyramid,bd=0,highlightthickness=0,command=self.GoImagePyramids,width=168,height=162,bg="#F4192B",fg="#000000")
        pyramidButton.place(x=740,y=350)

        


        view =Label (self.window,image=avatar)
        view.place(x=1080,y=80,width=169,height=169)

        hello =Label (self.window,text="Welcome ",bg="#050238",fg="#ffffff")
        hello.place(x=1170,y=300)

        msg =Label (self.window,text="\n Using this program, \n you can see  how the image processing examples work.  ",bg="#050238",fg="#ffffff")
        msg.place(x=1000,y=330)

        copyright =Label (self.window,text=" Copyright (c) 2020 Uğur ILGIN ",bg="#050238",fg="#ffffff")
        copyright.place(x=80,y=650)
        
        self.window.mainloop()

 
    def GoFaceDetection(self):
        self.Quit()
        FaceDetection(self.window)
    def GoObjectDetection(self):
        self.Quit()
        ObjectDetectionClass(self.window)
    def GoOCRDetection(self):
        self.Quit()
        OCRDetection(self.window)
    def GoEdgeDetection(self):
        self.Quit()
        EdgeDetection(self.window)    
    def GoGradientDetection(self):
        self.Quit()
        GradientDetection(self.window) 
    def GoConvexityDetection(self):
        self.Quit()
        ConvexityDetection(self.window)   
    def GoBlurImage(self):
        self.Quit()
        ImageSmoothing(self.window) 
    def GoImagePyramids(self):
        self.Quit()
        ImagePyramid(self.window)     
    def Quit(self):
        self.window.withdraw()
    
        
        
    #</---Anamenü Fonksiyonunun Tanımlanması--->