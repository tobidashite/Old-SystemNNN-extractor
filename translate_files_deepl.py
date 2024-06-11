import os
import requests

def translate_file(input_file, output_file):
    # Read the content of the input file
    with open(input_file, "r", encoding="utf-8") as file:
        text = file.read()

    # Set parameters for the DeepL API request
    params = {
        # Your authentication key goes here
        "auth_key": "",
        "text": text,
        "target_lang": "EN-US"
    }

    # Make a POST request to the DeepL API
    response = requests.post("https://api-free.deepl.com/v2/translate", data=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract translated text from the JSON response
        translated_text = response.json()["translations"][0]["text"]

        # Write the translated text to the output file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(translated_text)
    else:
        print("Error translating file:", response.text)

def translate_files(input_dir, output_dir):
    # Ensure that the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Translate each file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, filename)
            translate_file(input_file, output_file)

if __name__ == "__main__":
    # Directory where the untranslated .txt files are located
    input_dir = "/path/to/untranslated/files/"
    
    # Directory where the translated files will be saved
    # Ensure that this directory exists and has appropriate permissions
    output_dir = "/path/to/save/translated/files/"
    
    translate_files(input_dir, output_dir)

