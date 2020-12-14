# Python-Image-Processing
![logo](/SS/logo.png)
[Türkçe](https://github.com/ugurilgin/Python-Goruntu-Isleme/blob/master/Readme.md "Türkçe.md")

It is a Desktop Application with the Most Used Image Processing Tools in Python.
* The images to be processed must be in a different folder than the program folder.
* You can watch the video on youtube
[![Videoya Gözatınız](/SS/video.png)](https://www.youtube.com/watch?v=EtiYeyI45SI)
## Installation Guide
* 1-) Python 3 Download Link.
- https://www.python.org/downloads/
* 2-) Visual Studio Code Download Link.
 - https://code.visualstudio.com
* 3-) Yolov3 Dataset Download Link .
- https://pjreddie.com/media/files/yolov3.weights
* You need to copy the downloaded data set into the data folder in the program folder..
* 3-) You have to download the python libraries on the cmd screen with the help of the commands below.
~~~javascript
* pip install Pillow==2.2.2
* pip install opencv-python
* pip install numpy
* pip install matplotlib
* pip install pytesseract
~~~
* 4-) The teseract-OCR.exe application in the project folder needs to be installed.
* 5-) After selecting the file path of the Teseract.exe file in ProgramFiles from the file dialog window in the OCR / Teserract Path section of the program, it is necessary to click the save button and save the file path.

* The commandline (cmd or terminal) in the folder is opened to run the program. And the following command is used.
~~~javascript
* python3 main.py
~~~
* Or run main.py file via visual code.
## User Guide
* UML Class Diagram
* ![logo](/SS/UML.png)
* The program welcomes you with a visual interface at the first opening. You can view the window you want to trade through this Interface.
* ![logo](/SS/1.png)
* By clicking on the Face Detection Button, a window that enables face recognition operations opens. Through this window, you can perform face detection from picture, face detection from video, face detection via webcam..
* ![logo](/SS/2.png)
* ![logo](/SS/3.png)
*By clicking on the Object Detection Button, the window that enables object recognition operations opens. Through this window, you can perform object detection from image, object detection from video, object detection via webcam.
* ![logo](/SS/4.png)
* ![logo](/SS/5.png)
* Clicking the OCR button. The character in the selected picture is detected and converted into text format. You must save the Teseract-OCR location..
* ![logo](/SS/6.png)
* Clicking the Edge Detection Button opens the window that enables corner recognition operations. Through this window, you can perform corner detection from the image, corner detection from the video, corner detection through the webcam.
* ![logo](/SS/7.png)
* ![logo](/SS/8.png)
* Clicking the Image Gradient Button, operations are performed on the image using the .Laplace, SobelX and SobelY algorithms.
* ![logo](/SS/9.png)
* ![logo](/SS/10.png)
* ![logo](/SS/11.png)
* By clicking the Convexity Detect button, images are processed from the convex bar.
* ![logo](/SS/12.png)
* Blurring operations are performed on the image by clicking on the Smoothing Image button. Blurring samples are performed on the image using Gaussian and Median algorithms.

* ![logo](/SS/13.png)
* IClicking on the mage Pyramids button, the two images are combined, the junction is softened and it looks like a single image..

* ![logo](/SS/14.png)
## Copyright
Uğur ILGIN
