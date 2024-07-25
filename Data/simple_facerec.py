#!/usr/bin/env python
# coding: utf-8

# In[1]:


import face_recognition
import cv2
import os
import numpy as np

class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.frame_resizing = 0.25  # Adjust if needed for performance

    def load_encoding_images(self, images_path):
        image_files = os.listdir(images_path)

        for img_path in image_files:
            img = cv2.imread(os.path.join(images_path, img_path))
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the filename without the extension
            basename = os.path.basename(img_path)
            (filename, _) = os.path.splitext(basename)

            # Get encoding
            img_encoding = face_recognition.face_encodings(rgb_img)
            if img_encoding:
                self.known_face_encodings.append(img_encoding[0])
                self.known_face_names.append(filename)

    def detect_known_faces(self, frame):
        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame, model='hog')
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # Use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]

            face_names.append(name)

        # Convert face locations from the resized frame back to the original frame
        face_locations = np.array(face_locations) / self.frame_resizing
        face_locations = face_locations.astype(int)

        return face_locations, face_names


# In[ ]:




