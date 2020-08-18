from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import filedialog
from cv2 import cv2
import sys
import numpy as np


class ObjectDetection:
    def __init__(self,master):
        def MainmenuFonk():
            master.update()
            master.deiconify()
            self.Quit()
        def openFileImg():
            try:
                filename=filedialog.askopenfilename(initialdir="/img/", title="Please Choose an Image or Video File",filetypes=(("JPG File", "*.jpg"),("PNG File", "*.png"),("MP4 File", "*.mp4"),("AVI File", "*.avi")))
                myImage.place_forget()
                imageFirst=Image.open(filename)
                imageLast=imageFirst.resize((450, 400),Image.ANTIALIAS)
                myImg=ImageTk.PhotoImage(imageLast)
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
                a=ObjectDetectAl(self.filename)
                a.objDetectionImg()
                
                myImage2.place_forget()
                if(self.video==1):
                    imageFirst=Image.open("img/noImage.png")
                else:
                    imageFirst=Image.open("img/dist/objtest.jpg")
                imageLast=imageFirst.resize((450, 400),Image.ANTIALIAS)
                myImg=ImageTk.PhotoImage(imageLast)
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
        self.root.title("Object Detection")
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

        videoButton=Button(self.root,image=videoImage,bd=0,highlightthickness=0,command=self.objVideo,bg="#2C073E",fg="#000000")
        videoButton.image=videoImage
        videoButton.place(x=220,y=575)

        streamButton=Button(self.root,image=camImage,bd=0,highlightthickness=0,command=self.objWeb,bg="#2C073E",fg="#ffffff")
        streamButton.image=camImage
        streamButton.place(x=320,y=575)

    #</---Butonların Oluşturulması--->

    #<---Labelların Oluşturulması--->

        title=Label(self.root,text="Object Detection",font = "Arial 12 bold ",bg="#2C073E",fg="#c1bdbd")
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
    def objVideo(self):
        try:
            a=ObjectDetectAl(self.filename)
            a.objDetectionVideo()
        except:
            pass
    def objWeb(self):
        a=ObjectDetectAl(" ")
        a.objDetectionWebcam()
    def Quit(self):
        self.root.destroy()

    #</---Fonksiyonların Tanımlanması--->

class ObjectDetectAl:
    def __init__(self,filename):
        self.filename=filename

    def objDetectionImg(self):
        try:
            net = cv2.dnn.readNet("data/yolov3.weights", "data/yolov3.cfg")
            classes = []
            with open("data/coco.names", "r") as f:
                classes = [line.strip() for line in f.readlines()]
            layer_names = net.getLayerNames()
            output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
            colors = np.random.uniform(0, 255, size=(len(classes), 3))

            img = cv2.imread(self.filename)
            
            height, width, channels = img.shape

            blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

            net.setInput(blob)
            outs = net.forward(output_layers)

            class_ids = []
            confidences = []
            boxes = []
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)

                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)

                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
            print(indexes)
            font = cv2.FONT_HERSHEY_PLAIN
            for i in range(len(boxes)):
                if i in indexes:
                    x, y, w, h = boxes[i]
                    label = str(classes[class_ids[i]])
                    color = colors[class_ids[i]]
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                    cv2.putText(img, label, (x, y + 30), font, 3, color, 2)


            cv2.imwrite('img/dist/objtest.jpg',img, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except:
            pass
        

    def objDetectionVideo(self):
        try:
            net = cv2.dnn.readNet("data/yolov3.weights", "data/yolov3.cfg")
            classes = []
            with open("data/coco.names", "r") as f:
                classes = [line.strip() for line in f.readlines()]
            layer_names = net.getLayerNames()
            output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
            colors = np.random.uniform(0, 255, size=(len(classes), 3))

            cap = cv2.VideoCapture(self.filename)
            while(True):
                _, img=cap.read()

                height, width, channels = img.shape

                blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

                net.setInput(blob)
                outs = net.forward(output_layers)

                class_ids = []
                confidences = []
                boxes = []
                for out in outs:
                    for detection in out:
                        scores = detection[5:]
                        class_id = np.argmax(scores)
                        confidence = scores[class_id]
                        if confidence > 0.5:
                            center_x = int(detection[0] * width)
                            center_y = int(detection[1] * height)
                            w = int(detection[2] * width)
                            h = int(detection[3] * height)

                            x = int(center_x - w / 2)
                            y = int(center_y - h / 2)

                            boxes.append([x, y, w, h])
                            confidences.append(float(confidence))
                            class_ids.append(class_id)

                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
                print(indexes)
                font = cv2.FONT_HERSHEY_PLAIN
                for i in range(len(boxes)):
                    if i in indexes:
                        x, y, w, h = boxes[i]
                        label = str(classes[class_ids[i]])
                        color = colors[class_ids[i]]
                        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                        cv2.putText(img, label, (x, y + 30), font, 3, color, 2)


                cv2.imshow("Object Detect From Video",img)
                k = cv2.waitKey(30) & 0xff
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        except:
            pass

    def objDetectionWebcam(self):

        try:

            net = cv2.dnn.readNet("data/yolov3.weights", "data/yolov3.cfg")
            classes = []
            with open("data/coco.names", "r") as f:
                classes = [line.strip() for line in f.readlines()]
            layer_names = net.getLayerNames()
            output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
            colors = np.random.uniform(0, 255, size=(len(classes), 3))

            cap = cv2.VideoCapture(0)
            while(True):
                _, img=cap.read()

                height, width, channels = img.shape

                blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

                net.setInput(blob)
                outs = net.forward(output_layers)

                class_ids = []
                confidences = []
                boxes = []
                for out in outs:
                    for detection in out:
                        scores = detection[5:]
                        class_id = np.argmax(scores)
                        confidence = scores[class_id]
                        if confidence > 0.5:
                            center_x = int(detection[0] * width)
                            center_y = int(detection[1] * height)
                            w = int(detection[2] * width)
                            h = int(detection[3] * height)

                            x = int(center_x - w / 2)
                            y = int(center_y - h / 2)

                            boxes.append([x, y, w, h])
                            confidences.append(float(confidence))
                            class_ids.append(class_id)

                indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
                print(indexes)
                font = cv2.FONT_HERSHEY_PLAIN
                for i in range(len(boxes)):
                    if i in indexes:
                        x, y, w, h = boxes[i]
                        label = str(classes[class_ids[i]])
                        color = colors[class_ids[i]]
                        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                        cv2.putText(img, label, (x, y + 30), font, 3, color, 2)


                cv2.imshow("Object Detect From Webcam",img)
                k = cv2.waitKey(30) & 0xff
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        except:
            pass
