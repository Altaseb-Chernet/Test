import tkinter as tk

root = tk.Tk()
root.title('Login Image')
root.geometry('200x500')

# Open an image using Tkinter's PhotoImage
photo = tk.PhotoImage(file="Python-logo-notext.svg.png")

# Resize the image by subsampling (reduce the size by 4 times)
photo = photo.subsample(30, 30)  # Reduces the image by a factor of 4

# Create a Checkbutton with an image
check_button = tk.Checkbutton(root, text="Remember me", image=photo, compound="top")
check_button.pack()

# Keep a reference to the image so it doesn't get garbage collected
check_button.image = photo

root.mainloop()
