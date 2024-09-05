from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Get source language and API key
    source_language = request.form.get('source_language', 'en')
    mymemory_source_language = request.form.get('mymemory_source_language', source_language)  # Handle different format
    chatgpt_api_key = request.form.get('chatgpt_api_key', '')

    # Save the uploaded file
    audio_path = 'input_audio.wav'
    file.save(audio_path)

    # Step 1: Transcribe the audio file
    try:
        subprocess.run(['python', 'transcribe.py', audio_path, source_language, 'transcribe.txt'], check=True)
    except subprocess.CalledProcessError as e:
        return jsonify({'error': f'Transcription failed: {e}'}), 500

    # Step 2: Translate using mymemory.py
    if not attempt_translation('mymemory.py', mymemory_source_language):
        # Step 3: Translate using google.py
        if not attempt_translation('google.py', source_language):
            # Step 4: Translate using chatgpt.py
            if chatgpt_api_key:
                if not attempt_translation('chatgpt.py', source_language, chatgpt_api_key):
                    return jsonify({'error': 'Translation failed'}), 500
            else:
                return jsonify({'error': 'ChatGPT API key is required'}), 400

    # Read the output file and return the contents
    if os.path.exists('output.txt'):
        with open('output.txt', 'r') as f:
            translated_text = f.read()
        return jsonify({'translated_text': translated_text}), 200
    else:
        return jsonify({'error': 'Translation failed'}), 500

def attempt_translation(script_name, source_language, chatgpt_api_key=None):
    try:
        if script_name == 'chatgpt.py':
            subprocess.run(['python', script_name, 'transcribe.txt', 'output.txt', chatgpt_api_key, source_language], check=True)
        else:
            subprocess.run(['python', script_name, 'transcribe.txt', 'output.txt', source_language], check=True)
        if os.path.exists('output.txt'):
            return True
    except subprocess.CalledProcessError:
        pass
    return False

if __name__ == '__main__':
    app.run(debug=True)
