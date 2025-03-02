import tkinter as tk

# Create the main window
mainWindow = tk.Tk()
mainWindow.title("Coordinate")

# Get screen width and height
screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()

print(screen_width)
print(screen_height)

# Start the Tkinter event loop
mainWindow.mainloop()