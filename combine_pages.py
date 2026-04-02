from PIL import Image
from pathlib import Path

# 1. Path set up on Windows
def combine_to_pdf():
    input_folder = Path("/mnt/c/Users/hasmodin.ansari/Downloads/split_results")
    output_pdf = Path("/mnt/c/Users/hasmodin.ansari/Downloads/combine_page.pdf")

# 2. Check input folder
    if not input_folder.exists():
        print(f"X Error: folder {input_folder} not found.")
        return

# 3. Get and Sort Files
# Using our natural_sort_key ensures Page_2 comes before Page_10
    image_files = sorted(list(input_folder.glob("*.jpg")))
    print(image_files)

    if not image_files:
        print("No .jpg files found in the split_results folder")
        return
    print(f"Found {len(image_files)} pages. Converting to PDF...")

# 4. Process Images
    image_list = []
    for file_path in image_files:
        try:
            img = Image.open(file_path)
            # PDF saving requires RGB mode (removes transparency/alpha if present)
            if(img.mode != "RGB"):
                img = img.convert("RGB")
            image_list.append(img)
            print(f" + Added: {file_path.name}")
        except Exception as e:
            print(f" ! Skipping {file_path.name}: {e}")
# 5. Save PDF
    if image_list:
        # Take the first image and append the rest
        image_list[0].save(
            output_pdf,
            save_all=True,
            append_images=image_list[1:],
            resolution =100.0,
            quality=95
        )
        print("\n SUCCESS!")
        print(f"Your PDF is ready at: {output_pdf}")
    # Cleanup memory
    for img in image_list:
        img.close()
if __name__ == "__main__":
    combine_to_pdf()