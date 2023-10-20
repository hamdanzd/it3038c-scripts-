# Image Manipulation Script with Pillow

This Python script uses the Pillow (PIL) library for image manipulation. It demonstrates three different image manipulation tasks:

1. Resizing an image.
2. Applying a Gaussian blur filter.
3. Rotating an image.


To install Pillow on a Windows computer, open PowerShell and use the following command:
```bash
pip install Pillow
```

# Image Path 

The script processes the image located at C:\Users\Zain Hamdan\Desktop\projects\cat.jpg

Select an image of your choice, then copy the file path and replace the existing path in the script with the path to your selected image

```bash
image_path = r"C:\Users\Zain Hamdan\Desktop\projects\cat.jpg"
```




Copy the Python code and paste it into your virtual environment using a code editor such as Visual Studio Code for a smoother experience."

```bash

from PIL import Image, ImageFilter

# Open an image file
image_path = r"C:\Users\Zain Hamdan\Desktop\projects\cat.jpg"
original_image = Image.open(image_path)

# Use case 1: Resizing an Image
def resize_image(image, width, height):
    resized_image = image.resize((width, height))
    return resized_image

new_width = 300
new_height = 200
resized_image = resize_image(original_image, new_width, new_height)
resized_image.save("resized_image.jpg")
print("Image resized and saved as 'resized_image.jpg'.")

# Use case 2: Applying a Filter
def apply_filter(image, filter_type):
    filtered_image = image.filter(filter_type)
    return filtered_image

filtered_image = apply_filter(original_image, ImageFilter.GaussianBlur(2))
filtered_image.save("blurred_image.jpg")
print("Filter applied and saved as 'blurred_image.jpg'.")

# Use case 3: Rotating an Image
def rotate_image(image, angle):
    rotated_image = image.rotate(angle)
    return rotated_image

rotation_angle = 45
rotated_image = rotate_image(original_image, rotation_angle)
rotated_image.save("rotated_image.jpg")
print("Image rotated and saved as 'rotated_image.jpg'.")
```

# Output Images:
The resulting images will be saved in the same directory as your script with the following names:
```bash
*resized_image.jpg
*blurred_image.jpg
*rotated_image.jpg
```

# Example Results

*Original_image.jpg





![cat](https://github.com/hamdanzd/it3038c-scripts-/assets/143369477/d0bf73e1-cb3b-478f-bbd9-952fb4d8196f)

*resized_image.jpg



<img width="227" alt="cat 2" src="https://github.com/hamdanzd/it3038c-scripts-/assets/143369477/099955c1-12ba-4067-82f2-eaf50deeb360">

*blurred_image.jpg



<img width="239" alt="cat 1" src="https://github.com/hamdanzd/it3038c-scripts-/assets/143369477/b75deb4e-6752-4672-807f-23a8c00f9adf">

*rotated_image.jpg



<img width="242" alt="cat 3" src="https://github.com/hamdanzd/it3038c-scripts-/assets/143369477/f1c43356-5120-446d-b58c-7b3bdf50c855">

# Enjoy Image Manipulation with Pillow!
Feel free to experiment with your own images and explore the capabilities of the Pillow library. Enjoy enhancing your images with this Python script!




