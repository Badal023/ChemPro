#This Code Cannot be run on Online Environment (Cloud)
#The Code Requires Offline Environment (Offline Interpreter)
#Hence a Video is attached to demonstrate the working
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Function to open and display an image based on user input
def open_image_from_input():
    # Get the image name (or file path) entered by the user
    image_name = entry.get().strip()#
	
    if not image_name:
        # Show an error message if no input is entered
        messagebox.showerror("Input Error", "Please enter the name of the reaction.")
        return  # Do nothing if the input is empty
    # Set the image file path
    image_path = f"Images/{image_name}.png"
    
    # Check if the image file exists
    if not os.path.exists(image_path):
        # Show an error message if the image file is not found
        messagebox.showerror("Error", f"The reaction '{image_name}' was not found,\n Please check spelling from list")
        return

    try:
        # Try to open the image using PIL
        image = Image.open(image_path)
        
        # Convert the image to a format Tkinter can display
        tk_image = ImageTk.PhotoImage(image)
        
        # Update the label with the image
        label.config(image=tk_image)
        label.image = tk_image  # Keep a reference to the image to prevent garbage collection
    except Exception as e:
        # Show an error message if there is a problem loading the image
        messagebox.showerror("Loading Error", f"Error loading image: {e}")
        return

# Set up the main Tkinter window
root = tk.Tk()
root.title("Open Image from File Name")

# Create a Label widget for normal text (e.g., a title or instructions)
normal_text_label = tk.Label(root, text="Enter the name of the reaction\n(or enter 'list' to get list of reactions)")
normal_text_label.pack(pady=10)

# Create an Entry widget for the user to enter the image file name
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a Button widget to trigger the function when clicked
open_button = tk.Button(root, text="Find reaction", command=open_image_from_input)
open_button.pack(pady=10)

# Create a Label widget to display the image
label = tk.Label(root)
label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
