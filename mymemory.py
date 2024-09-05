from deep_translator import MyMemoryTranslator
import argparse

def translate_file(input_file_path, output_path, source_mymemory_language):
    # Initialize the MyMemoryTranslator with source language auto-detection and target language as English
    translator = MyMemoryTranslator(source=source_mymemory_language, target='english')

    # Translate the content
    translated_text = translator.translate_file(input_file_path)

    # Write the translated content to the output file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(translated_text)

    print(f'Translation complete. Translated text by mymemory saved to {output_path}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate text from a file to English.")
    parser.add_argument("input_file", help="Path to the input text file.")
    parser.add_argument("output_file", help="Path to the output text file.")
    parser.add_argument("source_mymemory_language", help="Source language for translation (e.g., 'de', 'fr', 'es').")

    args = parser.parse_args()

    translate_file(args.input_file, args.output_file, args.source_mymemory_language)


