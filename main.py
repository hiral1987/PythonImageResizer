import os
from PIL import Image, ExifTags

# Configuration
INPUT_FOLDER = "E:\\Input_files"  # Folder containing images
OUTPUT_FOLDER = "E:\\Output_files"  # Folder to save processed images
TARGET_SIZE = (600, 800)  # Resize to this width and height
OUTPUT_FORMAT = "JPEG"  # Choose format: "JPEG", "PNG", "WEBP"
QUALITY = 85  # Compression quality (1-100 for JPEG/WEBP, ignored for PNG)


def ensure_output_folder():
    """Creates the output folder if it does not exist."""
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)


def correct_orientation(image):
    """Corrects image orientation using EXIF metadata."""
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == "Orientation":
                break
        exif = image._getexif()

        if exif is not None:
            orientation_value = exif.get(orientation)
            if orientation_value == 3:
                image = image.rotate(180, expand=True)
            elif orientation_value == 6:
                image = image.rotate(270, expand=True)
            elif orientation_value == 8:
                image = image.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        # No EXIF data, no correction needed
        pass
    return image


def resize_with_aspect_ratio(image, max_size):
    """Resizes the image while maintaining aspect ratio."""
    image.thumbnail(max_size, Image.LANCZOS)  # Auto-maintains aspect ratio
    return image


def process_images():
    """Resizes, converts, and compresses images in bulk."""
    ensure_output_folder()

    for filename in os.listdir(INPUT_FOLDER):
        file_path = os.path.join(INPUT_FOLDER, filename)

        if os.path.isfile(file_path) and filename.lower().endswith(("jpg", "jpeg", "png", "webp")):
            try:
                with Image.open(file_path) as img:
                    # Auto-correct orientation
                    img = correct_orientation(img)

                    # Resize image while maintaining aspect ratio
                    img = resize_with_aspect_ratio(img, TARGET_SIZE)

                    # Get new filename and format
                    new_filename = os.path.splitext(filename)[0] + "." + OUTPUT_FORMAT.lower()
                    output_path = os.path.join(OUTPUT_FOLDER, new_filename)

                    # Save image with compression
                    img.save(output_path, OUTPUT_FORMAT, quality=QUALITY)
                    print(f"Processed: {filename} -> {new_filename}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print("✅ Image processing complete!")


if __name__ == "__main__":
    process_images()

