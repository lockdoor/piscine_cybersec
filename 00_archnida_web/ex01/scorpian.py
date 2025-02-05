import sys
import exifread

def scorpians():
    for image in sys.argv[1:]:
        try:
            with open(image, 'rb') as image_file:

                tags = exifread.process_file(image_file)
                # print(tags.keys())
                print(f"Filename: {image}")
                for tag in tags.keys():
                    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                        print(f"{tag}: {tags[tag]}")
                print()

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scorpian.py [image, ...]")
        sys.exit(1)
    scorpians()