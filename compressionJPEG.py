from PIL import Image
import os


def convert_png_to_jpeg(source_folder, destination_folder, quality=80):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if filename.endswith('.png'):
            source_file = os.path.join(source_folder, filename)

            with Image.open(source_file) as img:
                if img.mode == 'RGBA':
                    img = img.convert('RGB')

                destination_file = os.path.join(destination_folder, os.path.splitext(filename)[0] + '.jpeg')

                img.save(destination_file, 'JPEG', quality=quality)

            print(f"Imagen {filename} convertida y guardada como {destination_file}")


source_folder = r'C:\Users\Usuario\Desktop\face\muestra'

destination_folder = r'C:\Users\Usuario\Desktop\face\jpeg80'

convert_png_to_jpeg(source_folder, destination_folder)
