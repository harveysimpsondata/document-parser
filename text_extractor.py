import fitz  # PyMuPDF
import json


def extract_text_from_first_page(pdf_path):
    # Open the provided PDF file
    doc = fitz.open(pdf_path)
    first_page = doc[0]
    text = first_page.get_text()
    return text


def simple_text_to_jsonld(text):
    # Placeholder function to simulate the process of structuring text into JSON-LD
    # This example assumes the first line is the title, the second line is the author(s), and the rest is a description
    lines = text.split('\n')
    title = lines[0]
    authors = lines[1].split(", ")
    description = " ".join(lines[2:])

    jsonld = {
        "@context": "http://schema.org",
        "@type": "ScholarlyArticle",
        "headline": title,
        "author": [{"@type": "Person", "name": author} for author in authors],
        "description": description
    }

    return jsonld


# Path to your PDF file
pdf_path = "pdfs/quantum.pdf"

# Extract text from the first page
extracted_text = extract_text_from_first_page(pdf_path)

# Convert the extracted text to JSON-LD
jsonld_data = simple_text_to_jsonld(extracted_text)

# Print the JSON-LD output
print(json.dumps(jsonld_data, indent=4))
