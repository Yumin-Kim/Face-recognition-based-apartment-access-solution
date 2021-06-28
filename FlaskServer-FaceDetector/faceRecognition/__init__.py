from flask import jsonify
import face_recognition
import numpy as np
import math
def faceDetect_image(filestream,encodedGroupImages):
   
    unknown_image = face_recognition.load_image_file(filestream)
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
    test ="사진을 넣어주세요"
    face_names = []
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(encodedGroupImages[0], face_encoding,tolerance=0.5)
    # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(encodedGroupImages[0], face_encoding)
        best_match_index = np.argmin(face_distances)
    #해당 이름 변경 하는 코드
        if matches[best_match_index]:
            print(face_distances[best_match_index])
            test = "name : " + encodedGroupImages[1][best_match_index] +" | per : " +str(math.ceil(1-face_distances[best_match_index])*100) +"%"

    result = {
        "face_found_in_image": test,
    }
    print(result)
    return result

def encoding_images(pathname,imageNames,groupName):
    print(pathname)
    known_face_encodings =[]
    known_face_names = []
    for imageName in imageNames: 
        test_image = face_recognition.load_image_file(pathname+"/" + imageName)
        # test_face_locations = face_recognition.face_locations(test_image, number_of_times_to_upsample=0, model="cnn")
        test_face_locations = face_recognition.face_locations(test_image)
        test_face_encoding = face_recognition.face_encodings(test_image,test_face_locations)[0]
        known_face_encodings.append(test_face_encoding)
        known_face_names.append(imageName)
    return [known_face_encodings,known_face_names,{"groupName" : groupName}]
