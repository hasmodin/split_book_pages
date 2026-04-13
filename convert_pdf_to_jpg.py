from pdf2image import convert_from_path, pdfinfo_from_path
import os
from pathlib import Path
input_path= Path("/mnt/c/Users/hasmodin.ansari/Downloads/combine_page.pdf")
output_folder = Path("/mnt/c/Users/hasmodin.ansari/Downloads/split_jpg_results")

def convert_pdf_to_jpg():
    #create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created folder : {output_folder}")
        # Get total page count first
        info = pdfinfo_from_path(input_path)
        total_pages = info.get("Pages", 0)
        if total_pages == 0:
            print("Error : Could not determine page count or PDF is empty.")
            return
        print(f"Total pages to process: {total_pages}")

    print("Starting conversion...this may take a minute for large file")

    # Process page by page (looping)
    for i in range(1, total_pages + 1):
        # Convert only ONE specific page at a time
        page = convert_from_path(
            input_path,
            first_page=i,
            last_page=i,
            dpi=300
        )[0]

        filename = f"page_{i:03d}.jpg"
        path = os.path.join(output_folder, filename)
        page.save(path, "jpg", quality=90)

        # Clean up memory explicitly
        page.close()
        if i % 10 == 0:
            print(f"Done with {i}/{total_pages} pages")
    print("Success! No any error occurred during process.")
   
if __name__ == "__main__":
    convert_pdf_to_jpg()