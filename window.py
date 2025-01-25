import tkinter as tk

def create_window():
    # Create the main window
    window = tk.Tk()

    # Set window title
    window.title("My Window")

    # Set window size (width x height)
    window.geometry("400x300")

    # Add a label as an example of content
    label = tk.Label(window, text="Hello, welcome to the window!", font=("Arial", 14))
    label.pack(pady=50)  # Add some padding for aesthetics

    # Run the window loop
    window.mainloop()

# Call the function to create the window
create_window()
