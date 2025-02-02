import customtkinter
import titles

# Create the main window
window = customtkinter.CTk()
window.title("Movie Titles")
window.geometry("800x500")

# Create a Tabview
tabview = customtkinter.CTkTabview(window)
tabview.pack(expand=True, fill="both", padx=10, pady=10)

# Create a tab for each letter
tabs = {}
for movie in titles.movies:
    first_letter = movie["letter_index"]  # Use the correct key
    if first_letter not in tabs:
        tabs[first_letter] = tabview.add(first_letter)  # Create tab for each letter

# Create scrollable frames inside each letter tab
frames = {letter: customtkinter.CTkScrollableFrame(tabs[letter], width=780, height=400) for letter in tabs}
for frame in frames.values():
    frame.pack(expand=True, fill="both", padx=10, pady=10)

# Add movie titles under their respective letter tab
for movie in titles.movies:
    first_letter = movie["letter_index"]
    title = movie["title"]
    label = customtkinter.CTkLabel(frames[first_letter], text=title, font=("Arial", 14), anchor="w")
    label.pack(fill="x", padx=10, pady=5)

# Run the main loop
window.mainloop()
