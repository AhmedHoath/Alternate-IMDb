import customtkinter
import titles

def create_window():
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
        first_letter = movie["letter_index"].upper()  # Ensure uniform tab naming
        if first_letter not in tabs:
            tabs[first_letter] = tabview.add(first_letter)  # Create tab for each letter

    # Create scrollable frames inside each letter tab
    frames = {letter: customtkinter.CTkScrollableFrame(tabs[letter], width=780, height=400) for letter in tabs}
    for frame in frames.values():
        frame.pack(expand=True, fill="both", padx=10, pady=10)

    # Add movie titles under their respective letter tab
    for movie in titles.movies:
        first_letter = movie["letter_index"].upper()
        title = movie["title"]
        label = customtkinter.CTkLabel(frames[first_letter], text=title, font=("Arial", 14), anchor="w")
        label.pack(fill="x", padx=10, pady=5)

    # Run the main loop
    window.mainloop()


create_window()  # This ensures the GUI only runs when executing window.py directly


# Extract the movie titles from the list
if hasattr(titles, "movies") and isinstance(titles.movies, list):
    print("Movie Titles:")
    for movie in titles.movies:
        print(movie["title"])  # Access the 'title' field in each dictionary
else:
    print("No movies found or incorrect data format.")


