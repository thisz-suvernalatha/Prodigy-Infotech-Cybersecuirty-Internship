from PIL import Image
import numpy as np
import os

def identify_image_format(image_path):
    with open(image_path, 'rb') as image_file:
        signature = image_file.read(8)

    if signature.startswith(b'\xFF\xD8'):
        return 'JPEG'
    elif signature.startswith(b'\x89PNG'):
        return 'PNG'
    elif signature.startswith(b'RIFF') and signature[8:12] == b'WEBP':
        return 'WEBP'
    else:
        return 'Unknown format'


def manipulate_pixels(image_format, image_path):
    if image_format == 'JPEG':
        return manipulate_jpeg(image_path)
    elif image_format == 'PNG':
        return manipulate_png(image_path)
    elif image_format == 'WEBP':
        return manipulate_webp(image_path)
    else:
        print("Unsupported image format!")
        return None, None


def manipulate_jpeg(image_path):
    img = Image.open(image_path)
    pixels = np.array(img)
    original_values = np.copy(pixels) 

    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            r, g, b = pixels[i, j]
            avg = (r + g + b) // 3  
            pixels[i, j] = [avg, avg, avg]  
            
    result_img = Image.fromarray(pixels)
    return result_img, original_values


def manipulate_png(image_path):
    img = Image.open(image_path)
    pixels = np.array(img)
    original_values = np.copy(pixels)  

    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            r, g, b = pixels[i, j][:3]  
            avg = (r + g + b) // 3 
            pixels[i, j][:3] = [avg, avg, avg] 

    result_img = Image.fromarray(pixels)
    return result_img, original_values


def manipulate_webp(image_path):
    img = Image.open(image_path)
    pixels = np.array(img)
    original_values = np.copy(pixels)  

    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            r, g, b = pixels[i, j]
            avg = (r + g + b) // 3 
            pixels[i, j] = [avg, avg, avg] 

    result_img = Image.fromarray(pixels)
    return result_img, original_values


def decrypt_image(image_path, original_values):
    original_img = Image.fromarray(original_values)
    return original_img


def create_metadata_file(output_name, image_format):
    metadata_file_name = f"{output_name}_metadata.txt"
    with open(metadata_file_name, 'w') as meta_file:
        meta_file.write(f"Image Format: {image_format}\n")
        meta_file.write("This image was encrypted using a simple average of RGB values.\n")
        meta_file.write("Original pixel data saved in 'original_pixels.npy'.\n")
    return metadata_file_name


def load_metadata(metadata_file):
    try:
        with open(metadata_file, 'r') as meta_file:
            lines = meta_file.readlines()
            image_format = lines[0].split(": ")[1].strip()
            return image_format
    except FileNotFoundError:
        print("Metadata file not found.")
        return None


while True:
    operation = input("Would you like to 'encrypt' or 'decrypt' the image? (type 'exit' to quit): ").lower()

    if operation == 'encrypt':
        image_path = input("Please enter the image file name or full path: ") 
        image_format = identify_image_format(image_path)
        print(f"The image format is: {image_format}")

        result, original_values = manipulate_pixels(image_format, image_path)

        if result is not None:
            output_name = input("Enter the name for the encrypted output file (with extension): ")
            result.save(output_name)

            
            np.save('original_pixels.npy', original_values) 

            metadata_file = create_metadata_file(output_name, image_format)
            print(f"Encryption successful. Metadata file '{metadata_file}' created.")

    elif operation == 'decrypt':
        image_path = input("Please enter the encrypted image file name or full path: ")
        metadata_file = input("Please enter the metadata file name or full path: ")

        image_format = load_metadata(metadata_file)

        if image_format is not None:
            
            if os.path.exists('original_pixels.npy'):
                original_values = np.load('original_pixels.npy')  

                result = decrypt_image(image_path, original_values)

                if result is not None:
                    output_name = input("Enter the name for the decrypted output file (with extension): ")
                    result.save(output_name)
                    print("Decryption successful.")
            else:
                print("Error: Original pixel data not found. Decryption not possible.")
        else:
            print("Invalid or missing metadata. Decryption not possible.")

    elif operation == 'exit':
        print("Exiting the program.")
        break

    else:
        print("Invalid operation. Please choose 'encrypt', 'decrypt', or 'exit'.")
