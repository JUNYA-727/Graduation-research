import cv2
import dlib
import imutils
from imutils import face_utils
import pandas as pd
import time

DEVICE_ID = 0
capture = cv2.VideoCapture(DEVICE_ID)
predictor_path = "shape_predictor_68_face_landmarks.dat"

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
df = pd.DataFrame()
main_data = []

count = 0
max_count = 5
time1 = time.time()
fps = 0
while(True):
    ret, frame = capture.read()
    count += 1
    if count == max_count:
        time2 = time.time()
        during_time = time2-time1
        fps = max_count/during_time
        count = 0
        time1 = time.time()
        continue
    cv2.putText(frame, 'FPS: {:.2f}'.format(fps),
                (1100, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), thickness=2)

    frame = imutils.resize(frame, width=1000)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)

    face_detecter = False

    for rect in rects:
        face_detecter = True

        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        data = []
        for i, (x, y) in enumerate(shape):  # 顔全体の68箇所のランドマークをプロット
            cv2.circle(frame, (x, y), 1, (255, 255, 255), -1)
            data.append(x)
            data.append(y)
        main_data.append(data)
    # もし顔が判定できない場合はNot detect!と判定を行なう｡
    if face_detecter == True:
        cv2.putText(frame, 'Detect face!', (0, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), thickness=1)
    else:
        cv2.putText(frame, 'Not detect!', (0, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), thickness=1)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        name_index = []
        for i in range(1, 69):
            name_index.append('x'+str(i))
            name_index.append('y'+str(i))

        landmark_data = pd.DataFrame(main_data, columns=name_index)
        landmark_data.to_csv('to_csv_out.csv')

        break

capture.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
