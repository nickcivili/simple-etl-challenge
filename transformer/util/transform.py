from .load_sample import load_sample_file
from .validate_output import validate_json

def transform():
    input_json = load_sample_file()

    ### Write transformation here ###

    ### Assign result of transformation here ###
    output_json = {}
    
    if (validate_json(output_json)):
        print("The transformed object conforms to the schema.")
    else:
        print("Object \n {} \n does not conform to the given schema.")