import tkinter as tk
from tkinter import ttk
import customtkinter
import os


window = customtkinter.CTk()
window.title("Movie Titles")
window.geometry("800x500")

# Create a Tabview
tabview = customtkinter.CTkTabview(window)
tabview.pack(expand=True, fill="both", padx=10, pady=10)

# Add Tabs
tab1 = tabview.add("Movies")
tab2 = tabview.add("Favorites")
tab3 = tabview.add("Watch Later")

# Create scrollable frames inside each tab
movies_frame = customtkinter.CTkScrollableFrame(tab1, width=780, height=400)
movies_frame.pack(expand=True, fill="both", padx=10, pady=10)

favorites_frame = customtkinter.CTkScrollableFrame(tab2, width=780, height=400)
favorites_frame.pack(expand=True, fill="both", padx=10, pady=10)

watch_later_frame = customtkinter.CTkScrollableFrame(tab3, width=780, height=400)
watch_later_frame.pack(expand=True, fill="both", padx=10, pady=10)

# Function to load movie titles
def load_movie_titles(filename, frame):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            titles = file.readlines()
        
        # Display movie titles inside the scrollable frame
        for title in titles:
            title = title.strip()
            if title:  # Ignore empty lines
                label = customtkinter.CTkLabel(frame, text=title, font=("Arial", 14), anchor="w")
                label.pack(fill="x", padx=10, pady=5)

# Load movies into the "Movies" tab (AFTER creating frames)
load_movie_titles("test_titles.txt", movies_frame)

# Run the main loop
window.mainloop()
