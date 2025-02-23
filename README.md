# Bulk Image Resizer & Converter

This Python script processes multiple images in bulk by:

✅ Resizing them while maintaining the **aspect ratio**  
✅ Correcting **EXIF orientation** issues  
✅ Converting images to a **specified format (JPEG, PNG, WEBP, etc.)**  
✅ Compressing images by adjusting the **quality**  
✅ Saving the processed images to an **output folder**  

---

## How the Script Works

1. **Ensure Output Folder Exists**  
   - Creates the `output_images` folder if it doesn’t exist.

2. **Fix Image Rotation**  
   - Reads EXIF metadata and rotates the image correctly.

3. **Resize Image While Keeping Aspect Ratio**  
   - Uses `thumbnail()` to maintain proportions.

4. **Process Images in Bulk**  
   - Loops through images, corrects rotation, resizes, and saves them.

---

## Code Features & Customization

| Feature | Description | Customization |
|---------|------------|---------------|
| **Input Folder** | Folder where original images are stored | Change `INPUT_FOLDER = "input_images"` |
| **Output Folder** | Folder where processed images will be saved | Change `OUTPUT_FOLDER = "output_images"` |
| **Max Size (Width x Height)** | Resized images fit within this size | Modify `TARGET_SIZE = (800, 600)` |
| **Image Format** | Convert images to different formats | Change `OUTPUT_FORMAT = "JPEG"` |
| **Quality Compression** | Adjusts compression for smaller file sizes | Modify `QUALITY = 85` |

---

## How to Use

1. ✅ **Ensure Python & Pillow are Installed:**  
   ```sh
   pip install pillow
   ```

2. ✅ **Place Images in `input_images` Folder**

3. ✅ **Run the Script:**  
   ```sh
   python bulk_image_resizer.py
   ```

4. ✅ **Check the `output_images` Folder** for processed images

---

## Why This Script is Useful

✔ **Batch Processing** – Process multiple images at once.  
✔ **Fixes Rotated Images** – Corrects orientation automatically.  
✔ **Maintains Aspect Ratio** – No stretched or distorted images.  
✔ **Flexible & Customizable** – Supports different formats and sizes.  
✔ **Reduces File Size** – Optimizes images for web or storage.  

---

Let me know if you need any modifications! 🚀
