import cv2
import mediapipe as mp
import numpy as np


class AttentionDetector:
    def __init__(self):
        self.face_mesh = mp.solutions.face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=5,
            refine_landmarks=True
        )

    def detect_attention(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb)

        attention_scores = []

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                nose = face_landmarks.landmark[1]
                left_eye = face_landmarks.landmark[33]
                right_eye = face_landmarks.landmark[263]

                head_direction = abs(nose.x - 0.5)

                if head_direction < 0.08:
                    score = 90
                    status = "Focused"
                elif head_direction < 0.15:
                    score = 70
                    status = "Slightly Distracted"
                else:
                    score = 40
                    status = "Distracted"

                attention_scores.append((score, status))

        return attention_scores