from nanonets import NANONETSOCR
from dotenv import load_dotenv
import os
import json

load_dotenv()

NANONET_API = os.getenv('NANONETS_API')

model = NANONETSOCR()
model.set_token(NANONET_API)


pred_json = model.convert_to_prediction('pdfs/recipe.pdf')

# Assuming `pred_json` is your original data

def remove_coordinates(data):
    if isinstance(data, dict):
        return {key: remove_coordinates(value) for key, value in data.items() if key not in ['xmin', 'ymin', 'xmax', 'ymax']}
    elif isinstance(data, list):
        return [remove_coordinates(item) for item in data]
    else:
        return data

# Use the function to remove the specified keys
cleaned_data = remove_coordinates(pred_json)

# Print or use the cleaned data
print(json.dumps(cleaned_data, indent=4))

# Assuming `pred_json` is your OCR output

# def extract_title_and_authors(ocr_data):
#     # Placeholder function for extracting title and authors based on your OCR output format
#     # This is a simplified example that needs customization based on actual OCR output
#     title_text = ocr_data['results'][0]['page_data'][0]['words'][0]['text']
#     authors_text = " ".join([word['text'] for word in ocr_data['results'][0]['page_data'][0]['words'][1:5]])
#     return title_text, authors_text
#
# def extract_abstract(ocr_data):
#     # Placeholder for abstract extraction. You would need to implement logic to find and extract the abstract.
#     abstract_text = "Abstract text here..."
#     return abstract_text
#
# # Extract information using the placeholder functions
# title, authors = extract_title_and_authors(pred_json)
# abstract = extract_abstract(pred_json)
#
# # Structure extracted information into JSON-LD
# jsonld_data = {
#     "@context": "http://schema.org",
#     "@type": "ScholarlyArticle",
#     "headline": title,
#     "author": [{"@type": "Person", "name": author} for author in authors.split(", ")],
#     "abstract": abstract
# }
#
# # Convert to JSON string for display or further processing
# jsonld_str = json.dumps(jsonld_data, indent=4)
# print(jsonld_str)
#
