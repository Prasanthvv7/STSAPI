from deep_translator import ChatGptTranslator
import argparse
import os


def translate_file(input_file_path, output_file_path, api_key, source_language):


    # Initialize the translator
    translator = ChatGptTranslator(api_key=api_key, source=source_language, target='english')

    # Perform translation
    translated_text = translator.translate_file(input_file_path)

    # Write the translated text to the output file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(translated_text)

    print(f"Translation complete. Translated text by chatgpt written to {output_file_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate text from a file to English using ChatGPT.")
    parser.add_argument("input_file", help="Path to the input text file.")
    parser.add_argument("output_file", help="Path to the output text file.")
    parser.add_argument("api_key", help="API key for ChatGPT.")
    parser.add_argument("source_language", help="Source language for translation (e.g., 'de', 'fr', 'es').")

    args = parser.parse_args()

    translate_file(args.input_file, args.output_file, args.api_key, args.source_language)
