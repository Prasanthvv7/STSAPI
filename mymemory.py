from deep_translator import MyMemoryTranslator
import argparse

def split_text_into_chunks(text, max_length=500):
    chunks = []
    while len(text) > max_length:
        # Find the nearest space or punctuation mark to avoid cutting words in half
        split_index = text.rfind(' ', 0, max_length)
        if split_index == -1:
            split_index = max_length  # If no space is found, split at max_length
        chunks.append(text[:split_index].strip())  # Strip to remove leading/trailing spaces
        text = text[split_index:].strip()  # Remove leading space from next chunk
    chunks.append(text)  # Append the remaining text as the last chunk
    return chunks

def translate_file(input_file_path, output_path, source_mymemory_language):
    try:
        # Initialize the MyMemoryTranslator with source language and target language as English
        translator = MyMemoryTranslator(source=source_mymemory_language, target='english')

        # Read the content of the input file
        with open(input_file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Split the text into chunks if it's larger than 500 characters
        text_chunks = split_text_into_chunks(text)

        # Perform translation on each chunk and accumulate results
        translated_text = ""
        for chunk in text_chunks:
            translated_text += translator.translate(chunk)

        # Write the translated text to the output file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(translated_text)

        print(f'Translation complete. Translated text by MyMemory saved to {output_path}')

    except Exception as e:
        print(f'Error occurred during translation: {e}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate text from a file to English using MyMemory Translator.")
    parser.add_argument("input_file", help="Path to the input text file.")
    parser.add_argument("output_file", help="Path to the output text file.")
    parser.add_argument("source_mymemory_language", help="Source language for translation (e.g., 'de', 'fr', 'es').")

    args = parser.parse_args()

    translate_file(args.input_file, args.output_file, args.source_mymemory_language)
