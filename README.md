# STSAPI
# Translation API

This repository provides a Flask API for transcribing and translating audio files using multiple translation services. The API processes audio files, extracts text, and translates it using `mymemory.py`, `google.py`, and `chatgpt.py` sequentially.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Required Python scripts: `transcribe.py`, `mymemory.py`, `google.py`, `chatgpt.py`

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Prasanthvv7/STSAPI.git
    cd STSAPI
    ```

2. Install Dependencies if you haven't already:

    ```bash
    bash setup.sh
    ```

3. Make sure all required Python scripts (`transcribe.py`, `mymemory.py`, `google.py`, `chatgpt.py`) are in the same directory as `app.py`.

### Running the API

Start the Flask server:

```bash
python app.py
