import face_recognition #import a library for face recognition

#load pictures into the system
image = face_recognition.load_image_file("IMG20190311155809.jpg") 
image2 = face_recognition.load_image_file("IMG20190412203216.jpg")
#image2 = face_recognition.load_image_file('ronaldo.jpg') // enable to check the false statement of the system (disable the statement above)

#generate encoding and let system to analyse the pictures
student_original_encoding = face_recognition.face_encodings(image)[0]
student_current_encoding = face_recognition.face_encodings(image2)[0]

#compare faces to decide if it same person or not
results = face_recognition.compare_faces([student_original_encoding],student_current_encoding)
if results[0] == True:
    print ("Face was recognized \nAttendance was marked Successefully")
else:
    print('Face was not recognized try again')
