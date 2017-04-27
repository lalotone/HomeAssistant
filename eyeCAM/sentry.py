import cv2
import time
#import pyqrcode
#import qrtools
import pyttsx

#Voice engine for pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 120)
#Integrated web cam on netbook
cameraDaemon = True
camera_port = 0
camera = cv2.VideoCapture(camera_port)

def voiceEngineSpeak():
    engine.say("The weather is cloudy and sunny")
    engine.runAndWait()
def get_image():
    retval, im = camera.read()
    return im
def take_cam_shot():
    print("Taking image...")
    file = "/home/lalotone/test_image.png"
    camera_capture = get_image()
    cv2.imwrite(file, camera_capture)
    time.sleep(1)
    #If you want to kill the cam for another usages
    #del(camera)
    
#while cameraDaemon == True:
#    imageCam = take_cam_shot()
voiceEngineSpeak()
