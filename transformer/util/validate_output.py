import pathlib
import json
import jsonschema
from jsonschema import validate

def validate_json(output_json):
    with open(pathlib.Path(__file__).parent.parent / 'resources/sample_message_schema.json') as f:
        schema = json.load(f)

    try:
        validate(instance=output_json, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print('Error parsing schema {}'.format(err))
        return False
    return True