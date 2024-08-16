# Pixel Based Encryption
Develop a simple image encyption tool using pixel manipulation. Support operations like swapping pixel values or applying a basic mathematical operation to each pixel.

## Image Encryption Tool

This repository contains a simple image encryption tool that provides two methods for encrypting or decrypting images: swapping pixels based on a seed value and adding a constant value to each pixel.

### Features

1. **Swap Pixels**:
   - Encrypts or decrypts an image by swapping its pixels based on a seed value.
   
2. **Add Constant**:
   - Encrypts or decrypts an image by adding a constant value to each pixel.

### Dependencies

- Python 3.x
- PIL (Pillow)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/image-encryption-tool.git
    cd image-encryption-tool
    ```

2. **Install the required libraries**:
    ```bash
    pip install Pillow
    ```

### Usage

1. **Run the script**:
    ```bash
    python task2.py
    ```

2. **Follow the prompts**:
    - Enter the path to the image file you want to encrypt or decrypt.
    - Choose the operation: Swap pixels (S) or Add constant (A).
    - Enter the seed value (for swapping pixels) or the constant value (for adding to pixels).
    - The encrypted image will be saved with a new name prefixed by either `swapped_` or `added_`.

### Example

```bash
Image Encryption Tool
Enter the path to the image: example.jpg
Would you like to (S)wap pixels or (A)dd constant to each pixel? S
Enter the seed value for swapping: 1234
Encrypted image saved as swapped_example.jpg
```

### Functions

- **swap_pixels(image, seed)**:
  - Encrypts or decrypts an image by swapping its pixels based on a seed value.
  - Parameters:
    - `image`: The input image to be encrypted or decrypted.
    - `seed`: The seed value for the random number generator used to shuffle the pixels.
  - Returns:
    - The encrypted or decrypted image.

- **add_constant(image, constant)**:
  - Encrypts or decrypts an image by adding a constant value to each pixel.
  - Parameters:
    - `image`: The input image to be encrypted or decrypted.
    - `constant`: The constant value to add to each pixel.
  - Returns:
    - The encrypted or decrypted image.


