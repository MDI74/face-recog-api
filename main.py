import cv2
from deepface import DeepFace

metrics = ["cosine", "euclidean", "euclidean_l2"]

face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while True:
    res, img = cap.read()

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_n = img.copy()
    faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)

    for (x, y, w, h) in faces:
        cv2.rectangle(img_n, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imwrite('detect/facedetect.jpg', img[y:y + h, x:x + w])
        cv2.imwrite('detect/facedetects.jpg', img)
        try:
            result = DeepFace.verify(img1_path='detect/facedetect.jpg', img2_path='images/img4.jpg', distance_metric=metrics[2], detector_backend='opencv', model_name="VGG-Face")
            print(result)
            print("Личность подтверждена") if result['verified'] else print("Личность не подтверждена")
        except:
            print("Лицо не обнаружено")


    cv2.imshow('VideoCamera', img_n)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    #
    # if cv2.waitKey(1) & 0xff == ord('c'):
    #     try:
    #         result = DeepFace.verify(img1_path='facedetect.jpg', img2_path='images/img1.jpg')
    #         print(result)
    #         if result['verified']:
    #             print("Личность подтверждена")
    #     except:
    #         print("Лицо не обнаружено")

cap.release()
cv2.destroyAllWindows()