face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while True:
    res, img = cap.read()

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_n = img.copy()
    faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)

    for (x, y, w, h) in faces:
        cv2.rectangle(img_n, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # cv2.imwrite('detect/facedetect.jpg', img[y:y + h, x:x + w])
        cv2.imwrite('detect/facedetects.jpg', img)
        # try:
        #     result = DeepFace.verify(img1_path='detect/facedetects.jpg', img2_path='images/img5.jpg',
        #                              distance_metric=metrics[2], detector_backend='mtcnn', model_name="VGG-Face")
        #
        #     print("Личность подтверждена") if result['verified'] else print("Личность не подтверждена")
        # except:
        #     print("Лицо не обнаружено")

    cv2.imshow('VideoCamera', img_n)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

if cv2.waitKey(1) & 0xff == ord('c'):
    try:
        result = DeepFace.find(img_path='detect/facedetects.jpg', db_path='images',
                               distance_metric=metrics[2], detector_backend=backends[3], model_name=models[0])
        print(result)
        # home_page(result['identity'][0])
    except:
        print("Лицо не обнаружено")

cap.release()
cv2.destroyAllWindows()