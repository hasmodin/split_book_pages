import img2pdf
from PIL import Image, ImageOps
from pathlib import Path
import os
from natsort import natsorted

def combine_to_pdf_high_volume():
    input_folder = Path("/mnt/c/Users/hasmodin.ansari/Downloads/split_results")
    output_pdf = "/mnt/c/Users/hasmodin.ansari/Downloads/combine_page.pdf"
    temp_folder = Path("/mnt/c/Users/hasmodin.ansari/Downloads/temp_rotated")

    if not input_folder.exists():
        print(f"Error: {input_folder} not found.")
        return

    # image_files = sorted(list(input_folder.glob("*.jpg")))
    # Replace the image_files line with this:
    extensions = (".jpg", ".jpeg", ".JPG", ".JPEG")
    image_files = sorted([p for p in input_folder.iterdir() if p.suffix in extensions])
   
    print(f"Processing {len(image_files)} pages. This may take a moment...")

    # Create a temporary folder for rotated images
    temp_folder.mkdir(parents=True, exist_ok=True)
    processed_paths = []

    try:
        # Step 1: Fix rotation and save to temp files
        # We do this one-by-one to keep RAM usage near zero
        for i, file_path in enumerate(image_files):
            with Image.open(file_path) as img:
                img = ImageOps.exif_transpose(img)
                if img.mode != "RGB":
                    img = img.convert("RGB")
                
                temp_file = temp_folder / f"temp_{i:04d}.jpg"
                img.save(temp_file, "JPEG", quality=85)
                processed_paths.append(str(temp_file))
            
            if i % 100 == 0:
                print(f" - Prepared {i} pages...")

        # Step 2: Convert to PDF using img2pdf (Streaming)
        print("Writing PDF to disk...")
        with open(output_pdf, "wb") as f:
            f.write(img2pdf.convert(processed_paths))

        print(f"\nSUCCESS! PDF ready at: {output_pdf}")

    finally:
        # Step 3: Cleanup temporary files
        print("Cleaning up temporary files...")
        for p in processed_paths:
            if os.path.exists(p):
                os.remove(p)
        if temp_folder.exists():
            temp_folder.rmdir()

if __name__ == "__main__":
    combine_to_pdf_high_volume()
    