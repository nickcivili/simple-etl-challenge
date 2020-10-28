# simple-etl-challenge
A simple template for an (E)T(L) challenge, in Python (3.5+), designed to be completed in about 30 minutes.

## Required input file
Create a file named `sample_message.json` in the `resources` directory. 

This can contain any pre-transformation JSON as long as it is valid JSON.


## Required output for validation
Create a file named `sample_message_schema.json` in the `resources` directory.

This should contain a valid JSON schema that you would like to validate the TRANSFORMED input JSON against.

## Write the code
In the `utils/transform.py` file's `transform()` function write your code to transform the input to match to the output schema.

### To Test
Simply invoke `python(3) -m transformer`, you will be informed if your transform is successful or if it fails.
