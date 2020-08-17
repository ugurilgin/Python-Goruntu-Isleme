from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog
import numpy as np,sys
from cv2 import cv2


class ImagePyramid:
    def __init__(self,master):
        def MainmenuFonk():
            master.update()
            master.deiconify()
            self.Quit()

        def openFileImg():
            try:
                filename=filedialog.askopenfilename(initialdir="/img/", title="Please Choose an Image or Video File",filetypes=(("JPG File", "*.jpg"),("PNG File", "*.png")))
                myImage.place_forget()
                imageFirst=Image.open(filename)
                imageLast=imageFirst.resize((450, 250),Image.ANTIALIAS)
                myImg=ImageTk.PhotoImage(imageLast)
                myImageLast=Label(self.root,image=myImg,bg="#2C073E",fg="#ffffff",width=450,height=250)
                myImageLast.image=myImg
                myImageLast.place(x=50,y=170)
                Path.config(text=filename)
                self.filename=filename
            except:
                pass
        
        def openFileImg2():
            try:
                filename=filedialog.askopenfilename(initialdir="/img/", title="Please Choose an Image or Video File",filetypes=(("JPG File", "*.jpg"),("PNG File", "*.png")))
                myImage.place_forget()
                imageFirst=Image.open(filename)
                imageLast=imageFirst.resize((450, 250),Image.ANTIALIAS)
                myImg=ImageTk.PhotoImage(imageLast)
                myImageLast2=Label(self.root,image=myImg,bg="#2C073E",fg="#ffffff",width=450,height=250)
                myImageLast2.image=myImg
                myImageLast2.place(x=50,y=430)
                fileLoc.config(text=filename)
                self.filename2=filename
            except:
                pass              
            
        def imgDetect():
                    a=ImagePyramidAl(self.filename,self.filename2)
                    a.imagePyramidImg()
                    myImage2.place_forget()
                    imageFirst=Image.open("img/dist/pyramid.jpg")
                    imageLast=imageFirst.resize((450, 400),Image.ANTIALIAS)
                    myImg=ImageTk.PhotoImage(imageLast)
                    myImageLast=Label(self.root,image=myImg,bg="#2C073E",fg="#ffffff",width=450,height=400)
                    myImageLast.image=myImg
                    myImageLast.place(x=670,y=170)
                   
                     

    #<---Form Ayarları--->

        self.root = Toplevel()
        self.root.wm_iconbitmap('img/iconum.ico')
        self.root.geometry("1266x692+0+0")
        self.root.maxsize(1366,768)
        self.root.title("Image Pyramids")
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

        filebulButton=Button(self.root,image=find,bd=0,highlightthickness=0,command=openFileImg2,width=24,height=24,bg="#2C073E",fg="#000000")
        filebulButton.image=find
        filebulButton.place(x=980,y=135)

        imageButton=Button(self.root,image=fotoImage,bd=0,highlightthickness=0,command=imgDetect,bg="#2C073E",fg="#ffffff")
        imageButton.image=fotoImage
        imageButton.place(x=540,y=380)
        


    #</---Butonların Oluşturulması--->

    #<---Labelların Oluşturulması--->

        title=Label(self.root,text="IMAGE PYRAMIDS ",font = "Arial 12 bold ",bg="#2C073E",fg="#c1bdbd")
        title.place(x=463,y=30)

        fileLbl=Label(self.root,text="File Path :",bg="#2C073E",fg="#ffffff")
        fileLbl.place(x=55,y=100)

        Path=Label(self.root,text="Please Choose a File ...",bg="#2C073E",fg="#ffffff")
        Path.place(x=160,y=100)

        fileLocName=Label(self.root,text="Second File Path :",bg="#2C073E",fg="#ffffff")
        fileLocName.place(x=55,y=135)
        
        fileLoc=Label(self.root,text="Please Choose a File ...",bg="#2C073E",fg="#ffffff")
        fileLoc.place(x=160,y=135)
        
        myImage=Label(self.root,image=noImage,bg="#2C073E",fg="#ffffff",width=450,height=250)
        myImage.place(x=50,y=170)

        myImage2=Label(self.root,image=noImage,bg="#2C073E",fg="#ffffff",width=450,height=250)
        myImage2.place(x=50,y=430)

        myImage3=Label(self.root,image=noImage,bg="#2C073E",fg="#ffffff",width=450,height=470)
        myImage3.place(x=670,y=170)

       

    #</---Labellerın Oluşturulması--->


        self.root.mainloop()
    
    #<---Fonksiyonların Tanımlanması--->
    
    
    def Quit(self):
        self.root.destroy()

    #</---Fonksiyonların Tanımlanması--->

class ImagePyramidAl:
    def __init__(self,filename,filename2):
        self.filename=filename
        self.filename2=filename2
        
    def imagePyramidImg(self):
        imageFirst=Image.open(self.filename)
        imageLast=imageFirst.resize((450, 450),Image.ANTIALIAS)
        imageLast.save('img/dist/temp1.jpg')
        imageFirst2=Image.open(self.filename2)
        imageLast2=imageFirst2.resize((450, 450),Image.ANTIALIAS)
        imageLast2.save('img/dist/temp2.jpg')

        A = cv2.imread('img/dist/temp1.jpg')
        B = cv2.imread('img/dist/temp2.jpg')
     
        

        G = A.copy()
        gpA = [G]
        for i in range(6):
            G = cv2.pyrDown(G)
            gpA.append(G)

        G = B.copy()
        gpB = [G]
        for i in range(6):
            G = cv2.pyrDown(G)
            gpB.append(G)

        lpA = [gpA[5]]
        for i in range(6,0,-1):
        
            GE = cv2.pyrUp(gpA[i])
            GE=cv2.resize(GE,gpA[i - 1].shape[-2::-1])
            L = cv2.subtract(gpA[i-1],GE)
            lpA.append(L)


        lpB = [gpB[5]]
        for i in range(6,0,-1):
            
            GE = cv2.pyrUp(gpB[i])
            GE = cv2.resize(GE, gpB[i - 1].shape[-2::-1])
            L = cv2.subtract(gpB[i-1],GE)
           
            lpB.append(L)

        LS = []
        lpAc=[]
        for i in range(len(lpA)):
            b=cv2.resize(lpA[i],lpB[i].shape[-2::-1])
            lpAc.append(b)
       
        j=0
        for i in zip(lpAc,lpB):
            la,lb = i
            rows,cols,dpt = la.shape
            ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
            j=j+1
            LS.append(ls)

        ls_ = LS[0]
        for i in range(1,6):
            ls_ = cv2.pyrUp(ls_)
            ls_= cv2.resize(ls_, LS[i].shape[-2::-1])
            ls_ = cv2.add(ls_, LS[i])

        B= cv2.resize(B, A.shape[-2::-1])
        real = np.hstack((A[:,:cols//2],B[:,cols//2:]))

        cv2.imwrite('img/dist/pyramid.jpg',ls_)
        
            



        

    
