import cv2
import time

#############################################
# TO DO                                     #
# - Create A Function To Move Left Or Right #
# - Put On Raspberry Pi                     #
#  - Get The Port Setup                     #
#  - Get Webcam Working                     #
#############################################

#Facial Location
location_x = 0
location_y = 0

gpio_up = 5
gpio_down = 6
gpio_left = 13
gpio_right = 19


#For Global Width And Height Variables
_x = 0
_w = 0
_y = 0
_h = 0

#Booleans For Movement Of Servos
turning_left = False
turning_right = False
moving_up = False
moving_down = False

#Debugging
direction = ""
pitch = ""

def py_init():
    ##Init Board
    #GPIO.setmode(GPIO.BOARD)

    ##Init GPIO Pins
    #GPIO.setup(gpio_up, GPIO.OUT)
    #GPIO.setup(gpio_down, GPIO.OUT)
    #GPIO.setup(gpio_left, GPIO.OUT)
    #GPIO.setup(gpio_right, GPIO.OUT)
    pass

def move_left():
    pass

def move_right():
    pass

def move_up():
    pass

def move_down():
    pass

face_cascade = cv2.CascadeClassifier('trained.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (128, 67, 35), 2)
        
        #Calculate Center Of Face Position
        location_x = (x + w) /2
        location_y = (y + h) /2

        #Global Variables For x, y, w, h to use in fucntions etc...
        _x = x
        _y = y
        _w = w
        _h = h

        #Run Fucntion Based On Location Of The Face
        if location_x >= 215:
            turning_left = True
            direction = "Left"
            move_left()
        
        elif location_x <= 195:
            turning_right = True
            direction = "Right"
            move_right()
        
        if location_y >= 195:
            moving_up = True
            pitch = "Down"
            move_down()
        
        elif location_y <= 165:
            moving_down = True
            pitch = "Up"
            move_up()
        
        elif location_x >= 180 and location_x <= 200:
            direction = "Null"
        
        elif location_y >= 165 and location_x <= 185:
            pitch = "Flat"
    
    #Show Live Video
    cv2.imshow('Turret View', img)

    #Print Face Position
    print("X = " + str(int(location_x)) + " Y = " + str(int(location_y)) + " | " +"Currently Turning: " + direction + " Currently Angling: " + pitch + " | ")

    #Wait For Esc To Quit Program
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

# Release the Video Capture object
cap.release()
