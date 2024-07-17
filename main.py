import face_recognition
import os
from concurrent.futures import ThreadPoolExecutor
from timerit import Timerit

def compare_face_in_images(image_path_one, image_path_two):
    image_one = face_recognition.load_image_file(image_path_one)
    image_two = face_recognition.load_image_file(image_path_two)
    image_one_encodings = face_recognition.face_encodings(image_one)
    image_two_encodings = face_recognition.face_encodings(image_two)
    if len(image_one_encodings) == 0 or len(image_two_encodings) == 0:
        return False
    for face_encoding in image_two_encodings:
        matches = face_recognition.compare_faces([image_one_encodings[0]], face_encoding)
        if True in matches:
            return True
    return False

def compare_image_pair(args):
    img1, img2 = args
    result = compare_face_in_images(img1, img2)
    return result

def compare_folders(folder_one, folder_two):
    images_one = sorted([os.path.join(folder_one, f) for f in os.listdir(folder_one)])
    images_two = sorted([os.path.join(folder_two, f) for f in os.listdir(folder_two)])
    if len(images_one) != len(images_two):
        print("Las carpetas no tienen el mismo número de imágenes.")
        return
    print("Cantidad de procesadores: ", os.cpu_count())

    timer = Timerit(num=1, verbose=2)
    for _ in timer:
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(compare_image_pair, zip(images_one, images_two)))

    coincidencias = sum(results)
    no_coincidencias = len(results) - coincidencias
    print(f"Total de imágenes: {len(results)}")
    print(f"Coincidencias encontradas: {coincidencias}")
    print(f"No se encontraron coincidencias en: {no_coincidencias} imágenes")
    print(f"Tiempo total de comparación: {timer.mean():.2f} segundos")

from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Hora actual =", current_time)
print("PNG ORIGINAL:")
compare_folders('C:/Users/Usuario/Desktop/face/muestra', 'C:/Users/Usuario/Desktop/face/muestra2')
print()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Hora actual =", current_time)
print("JPEG80:")
compare_folders('C:/Users/Usuario/Desktop/face/muestra', 'C:/Users/Usuario/Desktop/face/jpeg')
print()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Hora actual =", current_time)
print("JPEG40:")
compare_folders('C:/Users/Usuario/Desktop/face/muestra', 'C:/Users/Usuario/Desktop/face/jpeg40')
print()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Hora actual =", current_time)
print("JPEG10:")
compare_folders('C:/Users/Usuario/Desktop/face/muestra', 'C:/Users/Usuario/Desktop/face/jpeg10')
print()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Hora actual =", current_time)
print("WEBP80:")
compare_folders('C:/Users/Usuario/Desktop/face/muestra', 'C:/Users/Usuario/Desktop/face/webp')
print()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Hora actual =", current_time)
print("WEBP40:")
compare_folders('C:/Users/Usuario/Desktop/face/muestra', 'C:/Users/Usuario/Desktop/face/webp40')
print()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Hora actual =", current_time)
print("WEBP10:")
compare_folders('C:/Users/Usuario/Desktop/face/muestra', 'C:/Users/Usuario/Desktop/face/webp10')