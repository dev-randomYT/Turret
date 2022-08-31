import cv2

#############################################
# TO DO                                     #
# - Create A Function To Move Left Or Right #
# - Put On Raspberry Pi                     #
#############################################


location_x = 0
location_y = 0

turning_left = False
turning_right = False
moving_up = False
moving_down = False

direction = ""
pitch = ""

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

        #Run Fucntion Based On Location Of The Face
        if location_x >= 200:
            turning_left = True
            direction = "Left"
        
        elif location_x <= 180:
            turning_right = True
            direction = "Right"
        
        if location_y >= 210:
            moving_up = True
            pitch = "Up"
        
        elif location_y <= 165:
            moving_down = True
            pitch = "Down"
        
        elif location_x >= 180 and location_x <= 200:
            direction = "Null"
        
        elif location_y >= 165 and location_x <= 185:
            pitch = "Flat"
        
        fps = cap.get(cv2.CAP_PROP_FPS)

        #Print Face Position
        print("X = " + str(int(location_x)) + " Y = " + str(int(location_y)) + " | " +"Currently Turning: " + direction + " Currently Angling: " + pitch + " | " + "Framerate: " + format(fps))
    
    #Show Live Video
    cv2.imshow('Turret View', img)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

# Release the VideoCapture object
cap.release()
