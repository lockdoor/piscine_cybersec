import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import piexif

def load_image():
    # file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.tiff")])
    file_path = filedialog.askopenfilename(filetypes=[("Images", ["*.jpg", "*.jpeg"])])
    if not file_path:
        return

    try:
        # Load the EXIF metadata
        img = Image.open(file_path)
        exif_data = piexif.load(img.info.get("exif", b""))
        display_exif(file_path, exif_data)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load EXIF data: {e}")


def display_exif(file_path, exif_data):
    # Clear the current fields
    for widget in exif_frame.winfo_children():
        widget.destroy()

    tk.Label(exif_frame, text=f"Editing EXIF for: {file_path}", font=("Arial", 12)).pack(anchor="w")

    for tag, value in exif_data.get("0th", {}).items():
        tag_name = piexif.TAGS["0th"][tag]["name"]
        tk.Label(exif_frame, text=tag_name).pack(anchor="w")
        entry = tk.Entry(exif_frame)
        print(value)
        entry.insert(0, str(value))
        entry.pack(anchor="w")
        exif_fields[tag] = entry

    save_button = tk.Button(exif_frame, text="Save Changes", command=lambda: save_exif(file_path, exif_data))
    save_button.pack(pady=10)


def save_exif(file_path, exif_data):
    try:
        for tag, entry in exif_fields.items():
            print(tag, entry.get().encode())
            exif_data["0th"][tag] = entry.get().encode()

        exif_bytes = piexif.dump(exif_data)
        img = Image.open(file_path)
        img.save(file_path, "jpeg", exif=exif_bytes)
        messagebox.showinfo("Success", "EXIF data saved successfully!")
    except Exception as e:
        # print(exif_fields)
        messagebox.showerror("Error", f"Failed to save EXIF data: {e}")


# Main GUI setup
root = tk.Tk()
root.title("EXIF Editor")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Button(frame, text="Load Image", command=load_image).pack(pady=5)

exif_frame = tk.Frame(root, padx=10, pady=10)
exif_frame.pack()

exif_fields = {}

root.mainloop()
