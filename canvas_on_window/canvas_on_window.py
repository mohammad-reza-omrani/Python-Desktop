import tkinter as tk

# Create the main window
mainWindow = tk.Tk()
mainWindow.title("Coordinate")

# Get screen width and height
screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()

# Get window dimensions
mainWindow_width = 500
mainWindow_height = 500

# Calculate position to center the window
vertical_offset = int(screen_height / 2 - mainWindow_height / 2)
horizontal_offset = int(screen_width / 2 - mainWindow_width / 2)

# Set the position of the window
mainWindow.geometry(f'{mainWindow_width}x{mainWindow_height}+{horizontal_offset}+{vertical_offset}')

# Create the canvas to draw the x and y axes
canvas = tk.Canvas(mainWindow, width=500, height=500)
canvas.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Start the Tkinter event loop
mainWindow.mainloop()