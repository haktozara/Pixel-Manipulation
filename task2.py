from PIL import Image
import random


#Encrypt or decrypt an image by swapping pixels.
def swap_pixels(image, seed):
    random.seed(seed)
    pixels = list(image.getdata())
    width, height = image.size

    # Generate a random permutation of indices
    indices = list(range(len(pixels)))
    random.shuffle(indices)

    # Swap the pixel values based on the permutation
    encrypted_pixels = [pixels[i] for i in indices]

    # Create a new image with the swapped pixels
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    
    return encrypted_image

#Encrypt or decrypt an image by adding a constant value to each pixel.
def add_constant(image, constant):
    pixels = list(image.getdata())
    width, height = image.size
    mode = image.mode

    encrypted_pixels = []

    for pixel in pixels:
        if isinstance(pixel, int):
            # Grayscale image
            encrypted_pixel = (pixel + constant) % 256
        else:
            # RGB image
            encrypted_pixel = tuple((channel + constant) % 256 for channel in pixel)
        encrypted_pixels.append(encrypted_pixel)

    # Create a new image with the modified pixels
    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)

    return encrypted_image

def main():
    print("Image Encryption Tool")
    image_path = input("Enter the path to the image: ").strip()
    operation = input("Would you like to (S)wap pixels or (A)dd constant to each pixel? ").strip().upper()
    
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    if operation == 'S':
        seed = int(input("Enter the seed value for swapping: ").strip())
        encrypted_image = swap_pixels(image, seed)
        output_path = "swapped_" + image_path
    elif operation == 'A':
        constant = int(input("Enter the constant value to add: ").strip())
        encrypted_image = add_constant(image, constant)
        output_path = "added_" + image_path
    else:
        print("Invalid operation. Please select 'S' to swap pixels or 'A' to add a constant.")
        return

    encrypted_image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

if __name__ == "__main__":
    main()
