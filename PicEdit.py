import numpy as np
import os
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
from PIL import ImageTk
import tkinter as tk
from tkinter import filedialog


def open_image():
    """
    Opens a dialog box to choose an image file. Retrieves the selected file name
    and displays it in a specific text field of the user interface.

    Inputs:
    - None

    Outputs:
    - None (but modifies the state of the user interface)

    1. Opens a file selection dialog for image file types (*.png, *.jpg, *.jpeg) 
       using filedialog.askopenfilename.
    2. Retrieves the selected file name without the full path using os.path.basename.
    3. Allows modification of the label_read text field, inserts the file name, then disables 
       modification of the field again.

    - The os, tkinter (or any other GUI), and filedialog modules must be imported.
    - A text field label_read must be defined in the user interface.

    - The label_read text field will contain the selected file name and will be in read-only state.
    """
    # Opens a dialog box to choose an image file
    load = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    
    # Retrieves the selected file name
    filename = os.path.basename(load)
    
    # Allows modification of the text field and inserts the file name
    label_read.config(state="normal")
    label_read.delete(0, tk.END)
    label_read.insert(0, filename)
    label_read.config(state="readonly")


def open_image2():
    """
    Opens a dialog box to choose a second image file. Retrieves the selected file name
    and displays it in a specific text field of the user interface.

    Inputs:
    - None

    Outputs:
    - None (but modifies the state of the user interface)

    1. Opens a file selection dialog for image file types (*.png, *.jpg, *.jpeg) 
       using filedialog.askopenfilename.
    2. Retrieves the selected file name without the full path using os.path.basename.
    3. Allows modification of the label_read2 text field, inserts the file name, then disables 
       modification of the field again.

    - The os, tkinter (or any other GUI), and filedialog modules must be imported.
    - A text field label_read2 must be defined in the user interface.

    - The label_read2 text field will contain the selected file name and will be in read-only state.
    """
    # Opens a dialog box to choose a second image file
    load = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    
    # Retrieves the selected file name
    filename = os.path.basename(load)
    
    # Allows modification of the text field and inserts the file name
    label_read2.config(state="normal")
    label_read2.delete(0, tk.END)
    label_read2.insert(0, filename)
    label_read2.config(state="readonly")


def crop(x):
    """
    Extracts the part of a file name before the first period ('.') in a given string.

    Inputs:
    - x (str): a string representing a file name

    Outputs:
    - nom3 (str): the part of string x before the first period ('.')

    1. Initialize an empty string nom3.
    2. Iterates through each character of string x until encountering a period ('.').
    3. If the current character is not a period, it is appended to nom3.
    4. If a period is encountered, the function immediately returns nom3.
    5. If no period is encountered, the function returns nom3 at the end of the loop.

    - x must be a string.

    - Returns the part of x before the first period, or the whole string if no period is present.
    """
    nom3 = ""
    for i in x:
        if i != ".":
            nom3 = nom3 + i
        else:
            return nom3
    return nom3



def init():
    """
    Retrieves the image file name from the text field, opens the image, resizes it for display,
    and creates a new empty image of the same size as the original image. Also clears the display of image B.

    Inputs:
    - None

    Outputs:
    - nom (str): the file name of the image
    - img (PIL.Image): the opened PIL image object
    - image_tk (ImageTk.PhotoImage): the resized image object for display
    - l (int): the width of the original image
    - h (int): the height of the original image
    - img2 (PIL.Image): a new empty image of the same size as the original image

    1. Retrieves the image file name from the label_read text field.
    2. Opens the image using PIL.Image.open and retrieves its dimensions (width and height).
    3. Resizes the image for display in the graphical interface.
    4. Displays the resized image in label_image.
    5. Creates a new empty image of the same size as the original image.
    6. Clears the display of image B and resets the label.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The text fields and labels label_read, label_image, and label_imageB must be defined in the user interface.

    - The label_read text field contains the file name of the image.
    - The label_image displays the resized image.
    - The label_imageB is reset.
    """
    # Retrieves the image file name from the text field
    nom = label_read.get()
    
    # Opens the image and retrieves its dimensions
    img = Image.open(nom)
    l, h = img.size
    
    # Resizes the image for display in the graphical interface
    img_resized = img.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img_resized)
    label_image.config(image=image_tk)
    label_image.image = image_tk
    
    # Creates a new empty image of the same size as the original image
    img2 = Image.new("RGB",(l,h))
    
    # Clears the display of image B and resets the label
    label_imageB.config(image="")
    label_imageB.place(x=0, y=0)
    
    return nom, img, image_tk, l, h, img2


def copy():
    """
    Copies each pixel from the original image to a new image and displays the latter.
    Also creates a button to save the copied image.

    Inputs:
    - None

    Outputs:
    - None (but modifies the state of the user interface)

    1. Initializes variables and retrieves the image by calling the init() function.
    2. Iterates through each pixel of the original image and copies them to a new image.
    3. Resizes the copied image for display in the graphical interface.
    4. Displays the resized copied image in label_image2.
    5. Creates a "Save" button to save the copied image with a new name.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The text fields and labels label_read, label_image, label_imageB, and label_image2 must be defined in the user interface.

    - The label_image2 displays the resized copied image.
    - A "Save" button allows saving the copied image.
    """
    # Initializes variables and retrieves the image
    nom, img, image_tk, l, h, img2 = init()
    
    # Iterates through each pixel of the image and copies them to a new image
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            img2.putpixel((x, y), (r, g, b))
    
    # Resizes the image for display
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Creates the "Save" button to save the image
    button_save = tk.Button(window, text="Save", command=lambda: img2.save("copy of " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)



def grayscale():
    """
    Converts each pixel of the original image to grayscale levels and displays the resulting image.
    Also creates a button to save the grayscale image.

    Inputs:
    - None

    Outputs:
    - None (but modifies the state of the user interface)

    1. Initializes variables and retrieves the image by calling the init() function.
    2. Iterates through each pixel of the original image and converts the colors to grayscale.
    3. Resizes the grayscale image for display in the graphical interface.
    4. Displays the resized grayscale image in label_image2.
    5. Creates a "Save" button to save the grayscale image with a new name.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The text fields and labels label_read, label_image, label_imageB, and label_image2 must be defined in the user interface.

    - The label_image2 displays the resized grayscale image.
    - A "Save" button allows saving the grayscale image.
    """
    # Initializes variables and retrieves the image
    nom, img, image_tk, l, h, img2 = init()
    
    # Iterates through each pixel of the image and converts to grayscale
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            c = int((r + g + b) / 3)
            img2.putpixel((x, y), (c, c, c))
    
    # Resizes the image for display
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Creates the "Save" button to save the image
    button_save = tk.Button(window, text="Save", command=lambda: img2.save("grayscale of " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def invert_colors():
    """
    Inverts the colors of each pixel of the original image and displays the resulting image.
    Also creates a button to save the image with inverted colors.

    Inputs:
    - None

    Outputs:
    - None (but modifies the state of the user interface)

    1. Initializes variables and retrieves the image by calling the init() function.
    2. Iterates through each pixel of the original image and inverts the colors (255 - value of each RGB component).
    3. Resizes the inverted image for display in the graphical interface.
    4. Displays the resized inverted image in label_image2.
    5. Creates a "Save" button to save the inverted image with a new name.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The text fields and labels label_read, label_image, label_imageB, and label_image2 must be defined in the user interface.

    - The label_image2 displays the resized inverted image.
    - A "Save" button allows saving the inverted image.
    """
    # Initializes variables and retrieves the image
    nom, img, image_tk, l, h, img2 = init()
    
    # Iterates through each pixel of the image and inverts the colors
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            r2 = 255 - r
            g2 = 255 - g
            b2 = 255 - b
            img2.putpixel((x, y), (r2, g2, b2))
    
    # Resizes the image for display
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Creates the "Save" button to save the image
    button_save = tk.Button(window, text="Save", command=lambda: img2.save("inverted colors of " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def flip_vertical():
    """
    Flips the image vertically and displays the resulting image.
    Also creates a button to save the vertically flipped image.

    Inputs:
    - None

    Outputs:
    - None (but modifies the state of the user interface)

    1. Initializes variables and retrieves the image by calling the init() function.
    2. Iterates through each pixel of the original image and flips the vertical positions.
    3. Resizes the vertically flipped image for display in the graphical interface.
    4. Displays the resized vertically flipped image in label_image2.
    5. Creates a "Save" button to save the vertically flipped image with a new name.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The text fields and labels label_read, label_image, label_imageB, and label_image2 must be defined in the user interface.

    - The label_image2 displays the resized vertically flipped image.
    - A "Save" button allows saving the vertically flipped image.
    """
    # Initializes variables and retrieves the image
    nom, img, image_tk, l, h, img2 = init()
    
    # Iterates through each pixel of the image
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            
            # Places the pixel at the corresponding position, but vertically flipped
            img2.putpixel((x, h - y - 1), (r, g, b))
    
    # Resizes the image for display
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Creates the "Save" button to save the image
    button_save = tk.Button(window, text="Save", command=lambda: img2.save("flipped image (top-bottom) of " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)



def flip_horizontal():
    """
    Flips the image horizontally and displays the resulting image.
    Also creates a button to save the horizontally flipped image.

    Inputs:
    - None

    Outputs:
    - None (but modifies the state of the user interface)

    1. Initializes variables and retrieves the image by calling the init() function.
    2. Iterates through each pixel of the original image and flips the horizontal positions.
    3. Resizes the horizontally flipped image for display in the graphical interface.
    4. Displays the resized horizontally flipped image in label_image2.
    5. Creates a "Save" button to save the horizontally flipped image with a new name.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The text fields and labels label_read, label_image, label_imageB, and label_image2 must be defined in the user interface.

    - The label_image2 displays the resized horizontally flipped image.
    - A "Save" button allows saving the horizontally flipped image.
    """
    # Initializes variables and retrieves the image
    nom, img, image_tk, l, h, img2 = init()
    
    # Iterates through each pixel of the image
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            
            # Places the pixel at the corresponding position, but horizontally flipped
            img2.putpixel((l - x - 1, y), (r, g, b))
    
    # Resizes the image for display
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Creates the "Save" button to save the image
    button_save = tk.Button(window, text="Save", command=lambda: img2.save("flipped image (left-right) of " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def red():
    """
    Preserves the red pixels of the original image and converts other pixels to grayscale.
    Displays the resulting image. Also creates a button to save the modified image.

    Inputs:
    - None

    Outputs:
    - None (but modifies the state of the user interface)

    1. Initializes variables and retrieves the image by calling the init() function.
    2. Iterates through each pixel of the original image.
    3. If red is the dominant component, preserves the original colors; otherwise, converts to grayscale.
    4. Resizes the modified image for display in the graphical interface.
    5. Displays the resized modified image in label_image2.
    6. Creates a "Save" button to save the modified image with a new name.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The text fields and labels label_read, label_image, label_imageB, and label_image2 must be defined in the user interface.

    - The label_image2 displays the resized modified image.
    - A "Save" button allows saving the modified image.
    """
    # Initializes variables and retrieves the image
    nom, img, image_tk, l, h, img2 = init()
    
    # Iterates through each pixel of the image
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            
            # If red is the dominant component, preserves the red color; otherwise, converts to grayscale
            if r > g and r > b:
                img2.putpixel((x, y), (r, g, b))
            else:
                c = int((r + g + b) / 3)
                img2.putpixel((x, y), (c, c, c))
    
    # Resizes the image for display
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Creates the "Save" button to save the image
    button_save = tk.Button(window, text="Save", command=lambda: img2.save("red preserved in " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)



def green():
    """
    Preserves the green pixels of the original image and converts other pixels to grayscale.
    Displays the resulting image. Also creates a button to save the modified image.

    Inputs:
    - None

    Outputs:
    - None (but modifies the state of the user interface)

    1. Initializes variables and retrieves the image by calling the init() function.
    2. Iterates through each pixel of the original image.
    3. If green is the dominant component, preserves the original colors; otherwise, converts to grayscale.
    4. Resizes the modified image for display in the graphical interface.
    5. Displays the resized modified image in label_image2.
    6. Creates a "Save" button to save the modified image with a new name.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The text fields and labels label_read, label_image, label_imageB, and label_image2 must be defined in the user interface.

    - The label_image2 displays the resized modified image.
    - A "Save" button allows saving the modified image.
    """
    # Initializes variables and retrieves the image
    nom, img, image_tk, l, h, img2 = init()
    
    # Iterates through each pixel of the image
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            
            # If green is the dominant component, preserves the green color; otherwise, converts to grayscale
            if g > r and g > b:
                img2.putpixel((x, y), (r, g, b))
            else:
                c = int((r + g + b) / 3)
                img2.putpixel((x, y), (c, c, c))
    
    # Resizes the image for display
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Creates the "Save" button to save the image
    button_save = tk.Button(fenetre, text="Save", command=lambda: img2.save("green preserved in " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def blue():
    """
    Preserves the blue pixels of the original image and converts other pixels to grayscale.
    Displays the resulting image. Also creates a button to save the modified image.

    Inputs:
    - None

    Outputs:
    - None (but modifies the state of the user interface)

    1. Initializes variables and retrieves the image by calling the init() function.
    2. Iterates through each pixel of the original image.
    3. If blue is the dominant component, preserves the original colors; otherwise, converts to grayscale.
    4. Resizes the modified image for display in the graphical interface.
    5. Displays the resized modified image in label_image2.
    6. Creates a "Save" button to save the modified image with a new name.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The text fields and labels label_read, label_image, label_imageB, and label_image2 must be defined in the user interface.

    - The label_image2 displays the resized modified image.
    - A "Save" button allows saving the modified image.
    """
    # Initializes variables and retrieves the image
    nom, img, image_tk, l, h, img2 = init()
    
    # Iterates through each pixel of the image
    for x in range(0, l):
        for y in range(0, h):
            r, g, b = img.getpixel((x, y))
            
            # If blue is the dominant component, preserves the blue color; otherwise, converts to grayscale
            if b > r and b > g:
                img2.putpixel((x, y), (r, g, b))
            else:
                c = int((r + g + b) / 3)
                img2.putpixel((x, y), (c, c, c))
    
    # Resizes the image for display
    img2_resized = img2.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Creates the "Save" button to save the image
    button_save = tk.Button(fenetre, text="Save", command=lambda: img2.save("blue preserved in " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)



def reduce_size():
    """
    Reduces the image to half its original dimensions and displays the resulting image.
    Also creates a button to save the reduced image.

    Inputs:
    - None

    Outputs:
    - None (but modifies the state of the user interface)

    1. Initializes variables and retrieves the image by calling the init() function.
    2. Calculates the new dimensions of the image reduced by half.
    3. Creates a new image with reduced dimensions.
    4. Iterates through each pixel of the original image, skipping every other pixel, and copies the values to the reduced image.
    5. Resizes the reduced image for display in the graphical interface.
    6. Displays the resized reduced image in label_image2.
    7. Creates a "Save" button to save the reduced image with a new name.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The text fields and labels label_read, label_image, label_imageB, and label_image2 must be defined in the user interface.

    - The label_image2 displays the resized reduced image.
    - A "Save" button allows saving the reduced image.
    """
    # Initializes variables and retrieves the image
    nom, img, image_tk, l, h, img2 = init()
    
    # Calculates the new dimensions of the image reduced by half
    l2 = int(l / 2)
    h2 = int(h / 2)
    
    # Creates a new image with reduced dimensions
    img2 = Image.new("RGB", (l2, h2))
    
    # Iterates through each pixel of the image, skipping every other pixel, and copies the values to the reduced image
    for x in range(0, l, 2):
        for y in range(0, h, 2):
            r, g, b = img.getpixel((x, y))
            img2.putpixel((int(x / 2), int(y / 2)), (r, g, b))
    
    # Resizes the reduced image for display
    img2_resized = img2.resize((int(l * 250 / l / 2), int(h / (l / (l * 250 / l / 2)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Creates the "Save" button to save the reduced image
    button_save = tk.Button(fenetre, text="Save", command=lambda: img2.save("reduction of " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def red_filter(value):
    """
    Applies a red filter to the image by increasing the intensity of red.
    Also creates a button to save the filtered image.

    Inputs:
    - value: intensity of the red filter (value of the scale)

    Outputs:
    - None (but modifies the state of the user interface)

    1. Retrieves the intensity from the value of the scale.
    2. Retrieves the filename of the image from the read label.
    3. Opens the image and gets its dimensions.
    4. Resizes the image for display in the graphical interface.
    5. Converts the image to a numpy array for more efficient manipulation.
    6. Applies the red filter by increasing the intensity of red.
    7. Converts the resulting numpy array back to a PIL image.
    8. Resizes the filtered image for display.
    9. Displays the resized filtered image in label_image2.
    10. Creates a "Save" button to save the filtered image with a new name.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The numpy modules must be imported.
    - The text fields and labels label_read, label_image, label_imageB, and label_image2 must be defined in the user interface.

    - The label_image2 displays the resized filtered image.
    - A "Save" button allows saving the filtered image.
    """
    label_imageB.config(image="")
    label_imageB.place(x=0, y=0)
    
    # Get the intensity from the scale value
    intensity = int(value)
    
    # Get the filename of the image from the read label
    nom = label_read.get()
    
    # Open the image
    img = Image.open(nom)
    
    # Get the dimensions of the image
    l, h = img.size
    
    # Resize the image for display
    img_resized = img.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img_resized)
    label_image.config(image=image_tk)
    label_image.image = image_tk
    
    # Convert the image to



def green_filter(value):
    """
    Applies a green filter to the image by increasing the intensity of green.
    Displays the resulting image. Also creates a button to save the filtered image.

    Inputs:
    - value: intensity of the green filter (scale value)

    Outputs:
    - None (but modifies the state of the user interface)

    1. Retrieves the intensity from the scale value.
    2. Retrieves the filename of the image from the read label.
    3. Opens the image and gets its dimensions.
    4. Resizes the image for display in the graphical interface.
    5. Converts the image to a numpy array for more efficient manipulation.
    6. Applies the green filter by increasing the intensity of the green channel.
    7. Converts the resulting numpy array back to a PIL image.
    8. Resizes the filtered image for display.
    9. Displays the resized filtered image in label_image2.
    10. Creates a "Save" button to save the filtered image with a new name.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The numpy modules must be imported.
    - The text fields and labels label_read, label_image, label_imageB, and label_image2 must be defined in the user interface.

    - The label_image2 displays the resized filtered image.
    - A "Save" button allows saving the filtered image.
    """
    label_imageB.config(image="")
    label_imageB.place(x=0, y=0)
    
    # Get the intensity from the scale value
    intensity = int(value)
    
    # Get the filename of the image from the read label
    nom = label_read.get()
    
    # Open the image
    img = Image.open(nom)
    
    # Get the dimensions of the image
    l, h = img.size
    
    # Resize the image for display
    img_resized = img.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img_resized)
    label_image.config(image=image_tk)
    label_image.image = image_tk
    
    # Convert the image to a numpy array for more efficient manipulation
    img_array = np.array(img)
    
    # Apply the green filter by increasing the intensity of the green channel
    img_array[:,:,1] = np.minimum(img_array[:,:,1] + 255 * intensity / 100, 255)
    
    # Ensure the values stay within the range [0, 255]
    img_array[:,:,1] = np.minimum(img_array[:,:,1], 255)
    
    # Convert the resulting numpy array back to a PIL image
    img_filtered = Image.fromarray(np.uint8(img_array))
    
    # Resize the filtered image for display
    img2_resized = img_filtered.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Resize the filtered image for saving
    img_save = img_filtered.resize((l, h))
    
    # Create the "Save" button to save the filtered image
    button_save = tk.Button(fenetre, text="Save", command=lambda: img_save.save("green filter on " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)



def blue_filter(value):
    """
    Applies a blue filter to the image by increasing the intensity of blue.
    Displays the resulting image. Also creates a button to save the filtered image.

    Inputs:
    - value: intensity of the blue filter (scale value)

    Outputs:
    - None (but modifies the state of the user interface)

    1. Retrieves the intensity from the scale value.
    2. Retrieves the filename of the image from the read label.
    3. Opens the image and gets its dimensions.
    4. Resizes the image for display in the graphical interface.
    5. Converts the image to a numpy array for more efficient manipulation.
    6. Applies the blue filter by increasing the intensity of the blue channel.
    7. Converts the resulting numpy array back to a PIL image.
    8. Resizes the filtered image for display.
    9. Displays the resized filtered image in label_image2.
    10. Creates a "Save" button to save the filtered image with a new name.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The numpy modules must be imported.
    - The text fields and labels label_read, label_image, label_imageB, and label_image2 must be defined in the user interface.

    - The label_image2 displays the resized filtered image.
    - A "Save" button allows saving the filtered image.
    """
    label_imageB.config(image="")
    label_imageB.place(x=0, y=0)
    
    # Get the intensity from the scale value
    intensity = int(value)
    
    # Get the filename of the image from the read label
    nom = label_read.get()
    
    # Open the image
    img = Image.open(nom)
    
    # Get the dimensions of the image
    l, h = img.size
    
    # Resize the image for display
    img_resized = img.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img_resized)
    label_image.config(image=image_tk)
    label_image.image = image_tk
    
    # Convert the image to a numpy array for more efficient manipulation
    img_array = np.array(img)
    
    # Apply the blue filter by increasing the intensity of the blue channel
    img_array[:,:,2] = np.minimum(img_array[:,:,2] + 255 * intensity / 100, 255)
    
    # Ensure the values stay within the range [0, 255]
    img_array[:,:,2] = np.minimum(img_array[:,:,2], 255)
    
    # Convert the resulting numpy array back to a PIL image
    img_filtered = Image.fromarray(np.uint8(img_array))
    
    # Resize the filtered image for display
    img2_resized = img_filtered.resize((int(l * 250 / l), int(h / (l / (l * 250 / l)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Resize the filtered image for saving
    img_save = img_filtered.resize((l, h))
    
    # Create the "Save" button to save the filtered image
    button_save = tk.Button(fenetre, text="Save", command=lambda: img_save.save("blue filter on " + nom), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)



def brighten(value):
    """
    Applies a brightening filter to the image by increasing color intensity.
    Displays the resulting image. Also creates a button to save the brightened image.

    Inputs:
    - value: intensity of the brightening filter (value from the scale)

    Outputs:
    - None (but modifies the state of the user interface)

    1. Retrieve the intensity from the scale value.
    2. Get the filename of the image from the read label.
    3. Open the image and get its dimensions.
    4. Convert the image to a numpy array for more efficient manipulation.
    5. Calculate brightness values to be added to each color.
    6. Apply brightening to the image by adding brightness values to the pixels.
    7. Ensure that values remain within the range [0, 255].
    8. Convert the resulting numpy array back to a PIL image.
    9. Resize the original image for display in the graphical interface.
    10. Display the resized original image in label_image.
    11. Resize the brightened image for display.
    12. Display the resized brightened image in label_image2.
    13. Resize the brightened image for saving.
    14. Create a "Save" button to save the brightened image.

    - The label_image2 displays the resized brightened image.
    - A "Save" button allows saving the brightened image.
    """
    label_imageB.config(image="")
    label_imageB.place(x=0, y=0)
    
    # Get the intensity from the scale value
    intensity = int(value)
    
    # Get the filename of the image from the read label
    filename = label_read.get()
    
    # Open the image
    img = Image.open(filename)
    
    # Get the dimensions of the image
    width, height = img.size
    
    # Convert the image to a numpy array for more efficient manipulation
    img_array = np.array(img)
    
    # Calculate brightness values to apply to each color
    bright_values = np.array([intensity, intensity, intensity]) * 255 / 100
    
    # Apply brightening to the image by adding brightness values to the pixels
    brightened_img_array = img_array + bright_values
    
    # Ensure that values remain within the range [0, 255]
    brightened_img_array = np.minimum(brightened_img_array, 255)
    
    # Convert the resulting numpy array back to a PIL image
    brightened_img = Image.fromarray(np.uint8(brightened_img_array))
    
    # Resize the original image for display
    resized_img = img.resize((int(width * 250 / width), int(height / (width / (width * 250 / width)))))
    image_tk = ImageTk.PhotoImage(resized_img)
    label_image.config(image=image_tk)
    label_image.image = image_tk
    
    # Resize the brightened image for display
    resized_brightened_img = brightened_img.resize((int(width * 250 / width), int(height / (width / (width * 250 / width)))))
    image_tk = ImageTk.PhotoImage(resized_brightened_img)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Resize the brightened image for saving
    saved_brightened_img = brightened_img.resize((width, height))
    
    # Create the "Save" button to save the brightened image
    button_save = tk.Button(fenetre, text="Save", command=lambda: saved_brightened_img.save("brightening of " + filename), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)



def darken(value):
    """
    Applies a darkening filter to the image by reducing color intensity.
    Displays the resulting image. Also creates a button to save the darkened image.

    Inputs:
    - value: intensity of the darkening filter (value from the scale)

    Outputs:
    - None (but modifies the state of the user interface)

    1. Retrieve the intensity from the scale value.
    2. Get the filename of the image from the read label.
    3. Open the image and get its dimensions.
    4. Resize the image for display.
    5. Convert the resized image to ImageTk for display.
    6. Convert the image to a numpy array for more efficient manipulation.
    7. Calculate dark values to apply to each color.
    8. Apply darkening to the image by subtracting dark values from the pixels.
    9. Ensure that values remain within the range [0, 255].
    10. Convert the resulting numpy array back to a PIL image.
    11. Resize the darkened image for display.
    12. Update the image in the graphical interface.
    13. Resize the darkened image for saving.
    14. Create a "Save" button to save the darkened image.

    - The label_image2 displays the resized darkened image.
    - A "Save" button allows saving the darkened image.
    """
    label_imageB.config(image="")
    label_imageB.place(x=0, y=0)
    
    # Get the intensity from the dark scale
    intensity = int(value)
    
    # Get the filename of the image from the read label
    filename = label_read.get()
    
    # Open the image
    img = Image.open(filename)
    
    # Get the dimensions of the image
    width, height = img.size
    
    # Resize the image for display
    resized_img = img.resize((int(width * 250 / width), int(height / (width / (width * 250 / width)))))
    
    # Convert the resized image to ImageTk for display
    image_tk = ImageTk.PhotoImage(resized_img)
    label_image.config(image=image_tk)
    label_image.image = image_tk
    
    # Convert the image to a numpy array for more efficient manipulation
    img_array = np.array(img)
    
    # Calculate dark values to apply to each color
    dark_values = np.array([intensity, intensity, intensity]) * 255 / 100
    
    # Apply darkening to the image by subtracting dark values from the pixels
    darkened_img_array = img_array - dark_values
    
    # Ensure that values remain within the range [0, 255]
    darkened_img_array = np.maximum(darkened_img_array, 0)
    
    # Convert the resulting numpy array back to a PIL image
    darkened_img = Image.fromarray(np.uint8(darkened_img_array))
    
    # Resize the darkened image for display
    resized_darkened_img = darkened_img.resize((int(width * 250 / width), int(height / (width / (width * 250 / width)))))
    
    # Update the image in the graphical interface
    image_tk = ImageTk.PhotoImage(resized_darkened_img)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Resize the darkened image for saving
    saved_darkened_img = darkened_img.resize((width, height))
    
    # Create the "Save" button to save the darkened image
    button_save = tk.Button(fenetre, text="Save", command=lambda: saved_darkened_img.save("darkening of " + filename), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)



def pixelization(value):
    """
    Applies a pixelation effect to the image by replacing blocks of pixels with single pixels.
    Displays the resulting image. Also creates a button to save the pixelated image.

    Inputs:
    - value: intensity of the pixelation (value from the scale)

    Outputs:
    - None (but modifies the state of the user interface)

    1. Retrieve the intensity from the scale value.
    2. Get the filename of the image from the read label.
    3. Open the image and get its dimensions.
    4. Convert the image to a numpy array for more efficient manipulation.
    5. Apply pixelation by replacing blocks of pixels with single pixels.
    6. Convert the resulting numpy array back to a PIL image.
    7. Resize the pixelated image for display in the graphical interface.
    8. Display the resized pixelated image in label_image2.
    9. Resize the pixelated image for saving.
    10. Create a "Save" button to save the pixelated image.

    - The label_image2 displays the resized pixelated image.
    - A "Save" button allows saving the pixelated image.
    """
    label_imageB.config(image="")
    label_imageB.place(x=0, y=0)
    
    # Get the intensity from the pixelation scale
    intensity = int(value)
    
    # Get the filename of the image from the read label
    filename = label_read.get()
    
    # Open the image
    img = Image.open(filename)
    
    # Get the dimensions of the image
    width, height = img.size
    
    # Resize the image for display
    resized_img = img.resize((int(width * 250 / width), int(height / (width / (width * 250 / width)))))
    
    # Convert the resized image to ImageTk for display
    image_tk = ImageTk.PhotoImage(resized_img)
    label_image.config(image=image_tk)
    label_image.image = image_tk
    
    # Convert the image to a numpy array for more efficient manipulation
    img_array = np.array(img)
    img2_array = np.zeros_like(img_array)
    
    # Pixelate the image by replacing blocks with single pixels
    for x in range(0, img_array.shape[0], intensity):
        for y in range(0, img_array.shape[1], intensity):
            img2_array[x:x+intensity, y:y+intensity] = img_array[x, y]
            
    # Convert the resulting numpy array back to a PIL image
    img2 = Image.fromarray(img2_array)

    # Resize the pixelated image for display
    img2_resized = img2.resize((int(width * 250 / width), int(height / (width / (width * 250 / width)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Resize the pixelated image for saving
    img2_resized = img2.resize((width, height))

    # Create the "Save" button to save the pixelated image
    button_save = tk.Button(fenetre, text="Save", command=lambda: img2_resized.save("pixelization of " + filename), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def vivid():
    """
    Applies a "vivid" effect to the image by increasing the intensity of dominant colors.
    Displays the resulting image. Also creates a button to save the resulting image.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The text fields and labels label_read, label_image, label_image2 must be defined in the user interface.

    - The label_image2 displays the image with the "vivid" effect.
    - A "Save" button allows saving the resulting image.
    """
    # Initialize variables and retrieve the image
    filename, img, image_tk, width, height, img2 = init()
    
    # Iterate through each pixel of the image and adjust values to make the image "vivid"
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x, y))
            
            # If the red channel is the largest, intensify the red color and remove other channels
            if r > b and r > g:
                r = 255
                g = 0
                b = 0
            
            # If the green channel is the largest, intensify the green color and remove other channels
            if g > r and g > b:
                g = 255
                r = 0
                b = 0
            
            # If the blue channel is the largest, intensify the blue color and remove other channels
            if b > r and b > g:
                b = 255
                r = 0
                g = 0
            
            # Place the adjusted values into the resulting image
            img2.putpixel((x, y), (r, g, b))
    
    # Resize the resulting image for display
    img2_resized = img2.resize((int(width * 250 / width), int(height / (width / (width * 250 / width)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Create the "Save" button to save the resulting image
    button_save = tk.Button(fenetre, text="Save", command=lambda: img2.save("vivid of " + filename), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def mix():
    """
    Mixes two images by alternately placing the pixels of each into a new image.
    Displays the resulting image. Also creates a button to save the resulting image.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The text fields and labels label_read, label_read2, label_image, label_imageB, label_image2 must be defined in the user interface.

    - The label_image2 displays the resulting mixed image.
    - A "Save" button allows saving the resulting image.
    """
    # Initialize variables and retrieve the images
    name, img, image_tk, width, height, img2 = init()
    name2 = label_read2.get()
    img2 = Image.open(name2)
    width2, height2 = img2.size
    
    # Determine the dimensions of the resulting image based on the dimensions of the two input images
    new_width = min(width, width2)
    new_height = min(height, height2)
    
    # Create a new resulting image
    img3 = Image.new("RGB", (new_width, new_height))
    
    # Display the second image in a dedicated area of the graphical interface
    label_imageB.place(x=700, y=int(height / (width / (width * 250 / width)) + 60))
    img2_resized = img2.resize((int(width2 * 250 / width2), int(height2 / (width2 / (width2 * 250 / width2)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_imageB.config(image=image_tk)
    label_imageB.image = image_tk
    
    # Iterate through each pixel of the two images and alternately place them in the resulting image
    for x in range(0, new_width, 2):
        for y in range(0, new_height, 2):
            r, g, b = img.getpixel((x, y))
            img3.putpixel((x, y), (r, g, b))
    
    for x in range(1, new_width, 2):
        for y in range(1, new_height, 2):
            r, g, b = img2.getpixel((x, y))
            img3.putpixel((x, y), (r, g, b))
    
    # Resize the resulting image for display
    img3_resized = img3.resize((int(new_width * 250 / new_width), int(new_height / (new_width / (new_width * 250 / new_width)))))

    image_tk = ImageTk.PhotoImage(img3_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Create the "Save" button to save the resulting image
    button_save = tk.Button(fenetre, text="Save", command=lambda: img3.save("mix of " + crop(name) + " and " + name2), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def enlarge():
    """
    Enlarges the image by doubling the size of each pixel.
    Displays the enlarged image. Also creates a button to save the enlarged image.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The text fields and labels label_read, label_image, label_image2 must be defined in the user interface.

    - The label_image2 displays the enlarged image.
    - A "Save" button allows saving the enlarged image.
    """
    # Initialize variables and retrieve the original image
    name, img, image_tk, width, height, img2 = init()
    
    # Calculate the new dimensions of the enlarged image
    new_width = int(width * 2)
    new_height = int(height * 2)
    
    # Create a new enlarged image with the new dimensions
    img2 = Image.new("RGB", (new_width, new_height))
    
    # Iterate through each pixel of the original image and place them in the new enlarged image
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x, y))
            # Place the original pixel and its copies in the new enlarged image
            img2.putpixel((int(x * 2) - 1, int(y * 2) - 1), (r, g, b))
            img2.putpixel((int(x * 2) - 1 + 1, int(y * 2) - 1), (r, g, b))
            img2.putpixel((int(x * 2) - 1, int(y * 2) - 1 + 1), (r, g, b))
            img2.putpixel((int(x * 2) - 1 + 1, int(y * 2) - 1 + 1), (r, g, b))
    
    # Resize the enlarged image for display
    img2_resized = img2.resize((int(width * 250 / width * 2), int(height / (width / (width * 250 / width * 2)))))

    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Create the "Save" button to save the enlarged image
    button_save = tk.Button(fenetre, text="Save", command=lambda: img2.save("enlargement of " + name), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)

def contrast(value):
    """
    Applies a contrast filter to the image.
    Displays the resulting image with adjusted contrast.
    Also creates a button to save the resulting image.

    Inputs:
    - value: intensity of the contrast filter (value from the scale)

    Outputs:
    - None (but modifies the state of the user interface)

    1. Initializes the variables name, img, image_tk, width, height, and img2 with the init() function.
    2. Retrieves the intensity of the contrast filter from the scale value.
    3. Applies the contrast filter to the image.
    4. Resizes the resulting image for display in the graphical interface.
    5. Displays the resized resulting image in label_image2.
    6. Creates a "Save" button to save the resulting image.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The text fields and labels label_read, label_image, label_imageB, and label_image2 must be defined in the user interface.
    - The init() function must be defined and return the variables name, img, image_tk, width, height, and img2.

    - The label_image2 displays the resulting image with adjusted contrast.
    - A "Save" button allows saving the resulting image with adjusted contrast.
    """
    name, img, image_tk, width, height, img2 = init()
    intensity = scale_contrast.get()
    contrast = ImageEnhance.Contrast(img)
    img2 = contrast.enhance(intensity)
    
    # Resize the resulting image for display
    img2_resized = img2.resize((int(width * 250 / width), int(height / (width / (width * 250 / width)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Create the "Save" button to save the resulting image
    button_save = tk.Button(fenetre, text="Save", command=lambda: img2.save("contrast of " + name), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)


def blur(value):
    """
    Applies a blur effect to the image.
    Displays the resulting image with the blur effect.
    Also creates a button to save the resulting image.

    Inputs:
    - value: intensity of the blur effect (value from the scale)

    Outputs:
    - None (but modifies the state of the user interface)

    1. Initializes the variables name, img, image_tk, width, height, and img2 with the init() function.
    2. Retrieves the intensity of the blur effect from the scale value.
    3. Applies the blur effect to the image.
    4. Resizes the resulting image for display in the graphical interface.
    5. Displays the resized resulting image in label_image2.
    6. Creates a "Save" button to save the resulting image.

    - The os, tkinter, filedialog, and PIL modules must be imported.
    - The text fields and labels label_read, label_image, label_imageB, and label_image2 must be defined in the user interface.
    - The init() function must be defined and return the variables name, img, image_tk, width, height, and img2.

    - The label_image2 displays the resulting image with the blur effect.
    - A "Save" button allows saving the resulting image with the blur effect.
    """
    name, img, image_tk, width, height, img2 = init()
    intensity = scale_blur.get()
    img2 = img.filter(ImageFilter.GaussianBlur(radius=intensity))
    
    # Resize the resulting image for display
    img2_resized = img2.resize((int(width * 250 / width), int(height / (width / (width * 250 / width)))))
    image_tk = ImageTk.PhotoImage(img2_resized)
    label_image2.config(image=image_tk)
    label_image2.image = image_tk
    
    # Create the "Save" button to save the resulting image
    button_save = tk.Button(fenetre, text="Save", command=lambda: img2.save("blur of " + name), bg="#0093FF", fg="white", font=("Helvetica", 12))
    button_save.place(x=50, y=0)



# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Retouche Photo")
fenetre.geometry("1400x800")
fenetre.config(bg="white")

# Création des label de texte
label_nom = tk.Label(fenetre, text="Chargez l'image que vous souhaiter modifier", bg="white")
label_nom.place(x=50, y=50)
label_nom2 = tk.Label(fenetre, text="Chargez la deuxième image", bg="white")
label_nom2.place(x=135, y=510)
label_couleur = tk.Label(fenetre, text="Choisissez la couleur :", bg="white")
label_couleur.place(x=250, y=265)
label_sens = tk.Label(fenetre, text="Choisissez le sens :", bg="white")
label_sens.place(x=145, y=230)

# Création des entry inchengeables
label_read = tk.Entry(fenetre, readonlybackground="grey", relief="flat", foreground="white")
label_read.config(state="readonly")
label_read.place(x=50, y=75)
label_read2 = tk.Entry(fenetre, readonlybackground="grey", relief="flat", foreground="white")
label_read2.config(state="readonly")
label_read2.place(x=415, y=510)

# Création des boutons pour toutes les fonctions
button = tk.Button(fenetre, text="Ouvrir une image", command=open_image)
button.place(x=300, y=50)
button = tk.Button(fenetre, text="Ouvrir une image", command=open_image2)
button.place(x=305, y=510)
button_copier = tk.Button(fenetre, text="Copier", command=copier, bg="#0093FF", fg="white", font=("Helvetica", 12))
button_copier.place(x=50, y=125)
button_gris = tk.Button(fenetre, text="Mettre en noir et blanc", command=gris, bg="#0093FF", fg="white", font=("Helvetica", 12))
button_gris.place(x=50, y=160)
button_inverser = tk.Button(fenetre, text="Inverser les couleurs", command=inverser, bg="#0093FF", fg="white", font=("Helvetica", 12))
button_inverser.place(x=50, y=195)
button_retourner = tk.Button(fenetre, text="Retourner", bg="#0093FF", fg="white", font=("Helvetica", 12))
button_retourner.place(x=50, y=230)
button_valoriser = tk.Button(fenetre, text="Valoriser une couleur", bg="#0093FF", fg="white", font=("Helvetica", 12))
button_valoriser.place(x=50, y=265)
button_diminuer = tk.Button(fenetre, text="Diminuer la taile", command=diminuer, bg="#0093FF", fg="white", font=("Helvetica", 12))
button_diminuer.place(x=50, y=300)
button_filtre = tk.Button(fenetre, text="Filtre de couleur", bg="#0093FF", fg="white", font=("Helvetica", 12))
button_filtre.place(x=50, y=335)
button_clair = tk.Button(fenetre, text="Eclaircir", bg="#0093FF", fg="white", font=("Helvetica", 12))
button_clair.place(x=50, y=370)
button_sombre = tk.Button(fenetre, text="Assombrir", bg="#0093FF", fg="white", font=("Helvetica", 12))
button_sombre.place(x=50, y=405)
button_pixel = tk.Button(fenetre, text="Pixéliser", bg="#0093FF", fg="white", font=("Helvetica", 12))
button_pixel.place(x=50, y=440)
button_vive = tk.Button(fenetre, text="RVB", command=vive, bg="#0093FF", fg="white", font=("Helvetica", 12))
button_vive.place(x=50, y=475)
button_melange = tk.Button(fenetre, text="Mélanger", command=melange, bg="#0093FF", fg="white", font=("Helvetica", 12))
button_melange.place(x=50, y=510)
button_agrandir = tk.Button(fenetre, text="Agrandir", command=agrandir, bg="#0093FF", fg="white", font=("Helvetica", 12))
button_agrandir.place(x=50, y=545)
button_contraste = tk.Button(fenetre, text="Contraste", bg="#0093FF", fg="white", font=("Helvetica", 12))
button_contraste.place(x=50, y=580)
button_flou = tk.Button(fenetre, text="Flou", bg="#0093FF", fg="white", font=("Helvetica", 12))
button_flou.place(x=50, y=615)
button_rouge = tk.Button(fenetre, text="Rouge", command=rouge)
button_rouge.place(x=400, y=265)
button_vert = tk.Button(fenetre, text="Vert", command=vert)
button_vert.place(x=455, y=265)
button_bleu = tk.Button(fenetre, text="Bleu", command=bleu)
button_bleu.place(x=500, y=265)
button_hb = tk.Button(fenetre, text="Haut/Bas", command=haut_bas)
button_hb.place(x=270, y=230)
button_gd = tk.Button(fenetre, text="Gauche/Droite", command=gauche_droite)
button_gd.place(x=345, y=230)

# Création des labels image pour l'affichage des images
label_image = tk.Label(fenetre, bg="white")
label_image.place(x=700, y=50)
label_image2 = tk.Label(fenetre, bg="white")
label_image2.place(x=975, y=50)
label_imageB = tk.Label(fenetre, bg="white")
label_imageB.place(x=0, y=0)

# Création des echelles utiles aux fonctions
scale_filtreR = tk.Scale(fenetre, from_=0, to=100, orient=tk.HORIZONTAL, bg="white", label="Rouge", command=lambda value: filtre_rouge(value), showvalue=False, font=("Helvetica", 8))
scale_filtreR.place(x=185, y=335)
scale_filtreV = tk.Scale(fenetre, from_=0, to=100, orient=tk.HORIZONTAL, bg="white", label="Vert", command=lambda value: filtre_vert(value), showvalue=False, font=("Helvetica", 8))
scale_filtreV.place(x=305, y=335)
scale_filtreB = tk.Scale(fenetre, from_=0, to=100, orient=tk.HORIZONTAL, bg="white", label="Bleu", command=lambda value: filtre_bleu(value), showvalue=False, font=("Helvetica", 8))
scale_filtreB.place(x=425, y=335)
scale_clair = tk.Scale(fenetre, from_=0, to=100, orient=tk.HORIZONTAL, bg="white", command=lambda value: clair(value), showvalue=False)
scale_clair.place(x=130, y=375)
scale_sombre = tk.Scale(fenetre, from_=0, to=100, orient=tk.HORIZONTAL, bg="white", command=lambda value: sombre(value), showvalue=False)
scale_sombre.place(x=145, y=410)
scale_pixel = tk.Scale(fenetre, from_=1, to=100, orient=tk.HORIZONTAL, bg="white", command=lambda value: pixel(value), showvalue=False)
scale_pixel.place(x=135, y=445)
scale_contraste = tk.Scale(fenetre, from_=0, to=10, resolution=0.1, orient=tk.HORIZONTAL, bg="white", command=lambda value: contraste(value), showvalue=False)
scale_contraste.place(x=140, y=580)
scale_contraste.set(1)
scale_flou = tk.Scale(fenetre, from_=0, to=10, resolution=0.1, orient=tk.HORIZONTAL, bg="white", command=lambda value: flou(value), showvalue=False)
scale_flou.place(x=140, y=615)

# Garder la fenêtre ouverte
fenetre.mainloop()
