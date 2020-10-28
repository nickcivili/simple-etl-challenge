import pathlib
import json

def load_sample_file():
    with open(pathlib.Path(__file__).parent.parent / 'resources/sample_message.json') as f:
        message = json.load(f)
        return message
