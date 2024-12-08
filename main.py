import cv2
import sys
import os

def detect_faces(image_path):
    # Загружаем изображение
    image = cv2.imread(image_path)
    if image is None:
        print("Не удалось загрузить изображение.")
        sys.exit(1)

    # Загружаем pre-trained классификатор лиц
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Конвертируем изображение в градации серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Обнаруживаем лица
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    print(f"Обнаружено лиц: {len(faces)}")
    for (x, y, w, h) in faces:
        print(f"Координаты лица: x={x}, y={y}, w={w}, h={h}")

if __name__ == "__main__":
    # Используем изображение по умолчанию, если аргумент не передан
    default_image = "faces.jpg"
    image_path = sys.argv[1] if len(sys.argv) > 1 else default_image

    if not os.path.exists(image_path):
        print(f"Файл {image_path} не найден.")
        sys.exit(1)

    detect_faces(image_path)