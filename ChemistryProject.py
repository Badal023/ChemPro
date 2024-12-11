import os
from PIL import Image
import matplotlib.pyplot as plt
from google.colab import files

# Function to open and display an image based on user input
def open_image_from_input(image_name):
    # Get the image name (or file path) entered by the user
    image_name = image_name.strip()  # Assume image_name is already passed to the function
    
    if not image_name:
        print("Please enter the name of the reaction.")
        return  # Do nothing if the input is empty
    
    # Set the image file path
    image_path = f"Images/{image_name}.png"  # Update the path to the correct location in Colab
    
    # Check if the image file exists
    if not os.path.exists(image_path):
        print(f"The reaction '{image_name}' was not found. Please check spelling.")
        return

    try:
        # Try to open the image using PIL
        image = Image.open(image_path)
        
        # Display the image using matplotlib
        plt.imshow(image)
        plt.axis('off')  # Hide axes
        plt.show()
    except Exception as e:
        print(f"Error loading image: {e}")



# Step 2: Ask for the image name
image_name = input("Enter the name of the reaction image (without the .png extension): ")

# Step 3: Call the function with the provided image name
open_image_from_input(image_name)
