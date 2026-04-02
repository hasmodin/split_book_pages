from PIL import Image, ImageOps
from pathlib import Path

def split_double_page():
    # 1. set up path
    input_folder = Path("/mnt/c/Users/hasmodin.ansari/Downloads/my_scans")
    output_folder = Path("/mnt/c/Users/hasmodin.ansari/Downloads/split_results")

    # 2. Validation
    if not input_folder.exists():
        print(f"X error: {input_folder} not found")
        return
        
    if not output_folder.exists():
        output_folder.mkdir(parents=True, exist_ok=True)
        print(f"Created Windows output folder: {output_folder}")  

    # 3. Processing
    # Added sorted() so files are processed in order (01, 02, 03...)
    images = sorted(list(input_folder.glob("*.jpg")) + list(input_folder.glob("*.JPG")))

    if not images:
        print("Empty folder: No .jpg files found")
        return
    
    print(f"Processing {len(images)} images...")

    for img_path in images:
        try:
            with Image.open(img_path) as img:
                # This fixes the rotation from Windows
                img = ImageOps.exif_transpose(img) 
                
                width, height = img.size
                midpoint = width // 2

                # Crop logic
                left_page = img.crop((0, 0, midpoint, height))
                right_page = img.crop((midpoint, 0, width, height))

                # --- ARABIC (RTL) SAVING LOGIC ---
                # Right side is the first page in Arabic
                right_page.save(output_folder / f"{img_path.stem}_1.jpg")
                # Left side is the second page in Arabic
                left_page.save(output_folder / f"{img_path.stem}_2.jpg")

                print(f"Split and saved: {img_path.name}")
        except Exception as e:
            print(f"X Error processing {img_path.name}: {e}")
            
    print(f"\nDone! You can find your files in Windows at: Downloads/split_results")

if __name__ == "__main__":
    split_double_page()