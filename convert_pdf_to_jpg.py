import pymupdf


def convert_pdf_to_jpg():
    input_path = "/mnt/c/Users/hasmodin.ansari/Downloads/combine_page.pdf"
    output_folder = "/mnt/c/Users/hasmodin.ansari/Downloads/jpg_images"

    if not input_path.exists():
        print(f"Error {input_path} not found")
        return
    if not output_folder.exists():
         output_folder.mkdir(parents=True, exist_ok=True)
         print(f"Created Windows output folder: {output_folder}")  
    # Open pdf file
    document = pymupdf.open(input_path)

    # finding page number
    for page_number in range(document.page_count):
        print(page_number)

        # loading pages
        pages = document.load_page(page_number)
        # getting images
        images = pages.get_pixmap()
        #saving images
        images.save(f"{output_folder} {page_number}.jpg")
        print(f"Page {page_number} Converted to image") 

convert_pdf_to_jpg()