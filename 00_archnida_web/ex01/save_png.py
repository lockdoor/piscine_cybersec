from PIL import Image
import sys
from pathlib import Path

def save_png():
    try:
        path = Path(sys.argv[1])
        if not path.exists():
            raise Exception("File does not exist.")
        if not path.is_file():
            raise Exception("Not a file.")
        filename = path.stem + ".png"
        im = Image.open(path)
        im.save(f'{path.parent}/{filename}')
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 save_png.py [image]")
        sys.exit(1)
    save_png()