from flask import Flask, render_template, Response
import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score  # Accuracy metrics
import pickle

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

app = Flask(__name__)
with open('body_language.pkl', 'rb') as f:
    model = pickle.load(f)


def gen_frames():
    cap = cv2.VideoCapture(0)
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while cap.isOpened():
            success, frame = cap.read()  # read the camera frame
            if not success:
                break
            else:
                # Recolor image to RGB
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detection
                results = holistic.process(image)

                # Recolor back to BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Render detections
                # 1. Draw face landmarks
                mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(
                                              color=(80, 110, 10), thickness=1, circle_radius=1),
                                          mp_drawing.DrawingSpec(
                                              color=(80, 256, 121), thickness=1, circle_radius=1)
                                          )

                # 2. Right hand
                mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(
                                              color=(80, 22, 10), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(
                                              color=(80, 44, 121), thickness=2, circle_radius=2)
                                          )

                # 3. Left Hand
                mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(
                                              color=(121, 22, 76), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(
                                              color=(121, 44, 250), thickness=2, circle_radius=2)
                                          )

                # 4. Pose Detections
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(
                                              color=(245, 117, 66), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(
                                              color=(245, 66, 230), thickness=2, circle_radius=2)
                                          )

                # Export coordinates
                try:
                    # Extract Pose landmarks
                    pose = results.pose_landmarks.landmark
                    pose_row = list(np.array(
                        [[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in pose]).flatten())

                    # Extract Face landmarks
                    face = results.face_landmarks.landmark
                    face_row = list(np.array(
                        [[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in face]).flatten())

                    # Concate rows
                    row = pose_row+face_row

                    # Make Detections
                    X = pd.DataFrame([row])
                    body_language_class = model.predict(X)[0]
                    body_language_prob = model.predict_proba(X)[0]
                    print(body_language_class, body_language_prob)

                    # Grab ear coords
                    coords = tuple(np.multiply(
                        np.array(
                            (results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_EAR].x,
                             results.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_EAR].y)), [640, 480]).astype(int))

                    cv2.rectangle(image,
                                  (coords[0], coords[1]+5),
                                  (coords[0]+len(body_language_class)
                                   * 20, coords[1]-30),
                                  (245, 117, 16), -1)
                    cv2.putText(image, body_language_class, coords,
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                    # Get status box
                    cv2.rectangle(image, (0, 0), (250, 60), (245, 117, 16), -1)

                    # Display Class
                    cv2.putText(
                        image, 'CLASS', (95, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                    cv2.putText(image, body_language_class.split(' ')[
                                0], (90, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                    # Display Probability
                    cv2.putText(
                        image, 'PROB', (15, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                    cv2.putText(image, str(round(body_language_prob[np.argmax(body_language_prob)], 2)), (
                        10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                except:
                    pass

                ret, buffer = cv2.imencode('.jpg', image)
                image = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')  # concat frame one by one and show result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
