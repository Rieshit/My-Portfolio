from flask import Flask, render_template
import os

app = Flask(__name__)

# Get images sorted by category
def get_wallpapers():
    wallpaper_folder = "static"
    categories = {}

    # Loop through static/ folders (categories)
    for folder in os.listdir(wallpaper_folder):
        folder_path = os.path.join(wallpaper_folder, folder)
        if os.path.isdir(folder_path):  # Only process folders (categories)
            categories[folder] = [f"{folder}/{f}" for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

    return categories  # Return a dictionary

@app.route("/")
def home():
    wallpapers = get_wallpapers()
    return render_template("index.html", wallpapers=wallpapers)

if __name__ == "__main__":
    app.run(debug=True)
