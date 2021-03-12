import face_recognition

# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("./data/obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("./data/biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

test01_image = face_recognition.load_image_file("./data/test01.jpg")
test01_face_encoding = face_recognition.face_encodings(test01_image)[0]

# Load a sample picture and learn how to recognize it.
test02_image = face_recognition.load_image_file("./data/test02.jpg")
test02_face_encoding = face_recognition.face_encodings(test02_image)[0]

test03_image = face_recognition.load_image_file("./data/test03.jpg")
test03_face_encoding = face_recognition.face_encodings(test03_image)[0]

# Load a sample picture and learn how to recognize it.
test04_image = face_recognition.load_image_file("./data/test04.jpg")
test04_face_encoding = face_recognition.face_encodings(test04_image)[0]

test05_image = face_recognition.load_image_file("./data/test05.jpg")
test05_face_encoding = face_recognition.face_encodings(test05_image)[0]

# Load a sample picture and learn how to recognize it.
test06_image = face_recognition.load_image_file("./data/test06.jpg")
test06_face_locations = face_recognition.face_locations(test06_image, number_of_times_to_upsample=0, model="cnn")
test06_face_encoding = face_recognition.face_encodings(test06_image,test06_face_locations)[0]


# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding,
    test01_face_encoding,
    test02_face_encoding,
    test03_face_encoding,
    test04_face_encoding,
    test05_face_encoding,
    test06_face_encoding,
]
known_face_names = [
    "Barack Obama",
    "Joe Biden",
    "person1",
    "person2",
    "person3",
    "person4",
    "person5",
    "person6",
]