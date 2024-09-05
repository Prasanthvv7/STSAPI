import requests
import sys
import os
import json


def transcribe(file_path, language, output_file, generate_vtt=False):
    """
    Transcribes the given audio/video file using the ASR API and saves only the transcript to an output file.

    Args:
        file_path (str): Path to the audio/video file to be transcribed.
        language (str): The language of the source audio/video.
        output_file (str): Path to the file where the transcript will be saved.
        generate_vtt (bool): Whether to generate a WebVTT caption file. Default is False.

    Returns:
        dict: JSON response from the ASR API containing the transcription and other metadata,
              or an error message.
    """
    url = 'https://asr.iitm.ac.in/internal/asr/decode'

    if not os.path.isfile(file_path):
        return {"error": f"File not found: {file_path}"}

    try:
        with open(file_path, 'rb') as f:
            # Prepare the files and data for the POST request
            files = {'file': f}
            data = {
                'language': language.lower(),  # Language should be in lowercase
                'vtt': 'true' if generate_vtt else 'false'  # Optional VTT generation
            }

            # Send the POST request to the ASR API with a timeout
            response = requests.post(url, files=files, data=data, timeout=30)  # Set a 30-second timeout
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)

            try:
                # Get JSON response
                result = response.json()
                transcript = result.get('transcript', 'Transcript not available')

                # Save transcript to the output file
                with open(output_file, 'w') as out_file:
                    out_file.write(transcript)
                return {"message": "Transcript saved successfully"}
            except ValueError:
                # Handle invalid JSON response
                return {"error": "Invalid JSON response from ASR API"}

    except requests.exceptions.Timeout:
        return {"error": "The request timed out"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Error during the request: {e}"}


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python transcribe.py <file_path> <language> <output_file> [vtt]")
        sys.exit(1)

    file_path = sys.argv[1]
    language = sys.argv[2]
    output_file = sys.argv[3]
    generate_vtt = len(sys.argv) > 4 and sys.argv[4].lower() == 'true'

    result = transcribe(file_path, language, output_file, generate_vtt)

    if result:
        print(result)
