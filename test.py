#cv2 is the OpenCV library used for handling the video stream and drawing shapes on frames.
import cv2
#face_recognition is a Python library built on top of dlib that provides easy-to-use functions for face detection and face recognition.
import face_recognition

#Known_Face_encodings will store the encoded representations of known faces.
Known_Face_encodings=[]
#Face_names will store the names corresponding to each known face encoding, allowing us to label detected faces.
Face_names=[]

#face_recognition.load_image_file() loads each image file.
person1=face_recognition.load_image_file("C:/Users/Prasanth/Pictures/images/Downey.jpg")
person2=face_recognition.load_image_file("C:/Users/Prasanth/Pictures/images/Andrew.webp")
person3=face_recognition.load_image_file("C:/Users/Prasanth/Pictures/images/mom.jpg")
person4=face_recognition.load_image_file("C:/Users/Prasanth/Pictures/images/dad.jpg")

#person1=face_recognition.load_image_file("")
#person1=face_recognition.load_image_file("")

#face_recognition.face_encodings() takes a face image and returns a list of face encodings.
#Each encoding is a unique representation of a face.
#[0] at the end selects the first encoding from the list returned by face_encodings() (assuming one face per image).
person1_encoding=face_recognition.face_encodings(person1)[0]
person2_encoding=face_recognition.face_encodings(person2)[0]
person3_encoding=face_recognition.face_encodings(person3)[0]
person4_encoding=face_recognition.face_encodings(person4)[0]

#append() adds the encoding to Known_Face_encodings
Known_Face_encodings.append(person1_encoding)
Known_Face_encodings.append(person2_encoding)
Known_Face_encodings.append(person3_encoding)
Known_Face_encodings.append(person4_encoding)

#append() adds the corresponding name to Face_names
Face_names.append("Robert Downey Jr")
Face_names.append("Andrew Garfield")
Face_names.append("Mom")
Face_names.append("Dad")


#Initialize webcam
video_capture=cv2.VideoCapture(0)

while True:
    #video_capture.read() captures a single frame from the webcam. 
    #ret is a Boolean indicating if the frame was successfully read.
    ret,frame=video_capture.read()
    
    #face_recognition.face_locations(frame) detects all faces in the frame and returns their coordinates (top, right, bottom, left).
    face_locations=face_recognition.face_locations(frame)
    #face_recognition.face_encodings(frame, face_locations) encodes each detected face location, resulting in a list of encodings for each face in the current frame.
    Face_encodings=face_recognition.face_encodings(frame,face_locations)

    #Loop through each face found in the frame
    #zip(face_locations, Face_encodings) pairs each detected face location with its corresponding face encoding
    for (top,right,bottom,left),face_encoding in zip(face_locations,Face_encodings):
        #Check if the face matches any known faces
        matches=face_recognition.compare_faces(Known_Face_encodings,face_encoding)
        name="Unkown"

        if True in matches:
            #matches.index(True) finds the position of the first True in the matches list. This position, stored in first_match_index.
            first_match_index=matches.index(True)
            #Face_names[first_match_index] retrieves the name corresponding to the matched face encoding using first_match_index.
            name=Face_names[first_match_index]

        #Draw a box around the face and label with the name
        #cv2.rectangle() draws a box around the detected face using the coordinates (left, top) and (right, bottom) with a red color (0, 0, 225) and a thickness of 2.
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,225),2)
        #cv2.putText() places the recognized person’s name above the bounding box, with font size 0.9 and thickness 2.
        #(top - 10) is used to place the text slightly above the bounding box
        cv2.putText(frame,name,(left,top-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,225),2)

    #Display the resultinng frame
    cv2.imshow("Video",frame)

    #Break the loop when the "q" key is pressed
    #The parameter 1 specifies the delay in milliseconds , meaning it checks for key presses every 1 millisecond.
    #cv2.waitKey(1) returns a 32-bit integer representing the ASCII code of the pressed key if a key is pressed within the delay time; otherwise, it returns -1.
    #The bitwise AND operation & 0xFF ensures we only get the last 8 bits of the key code returned by cv2.waitKey(1).
    #The entire condition if cv2.waitKey(1) & 0xFF == ord('q') checks if the key pressed matches the ASCII code for 'q'.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Stops the webcam and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
