import os
import re
import importlib.util
import inspect
import sys
from yamale.validators import DefaultValidators, Validator
import yamale
from yamale import YamaleError
import glob
import yaml

schema_path = f'/app/{os.getenv("INPUT_SCHEMA")}' 
path_pattern = re.compile(os.getenv('INPUT_PATH_PATTERN'))
validators_file = f'/app/{os.getenv("INPUT_VALIDATORS_PATH")}'
strict = os.getenv("INPUT_STRICT").lower() in ("yes", "true", "t", "1")

validators = DefaultValidators.copy()
if os.path.isfile(validators_file):
    print(f"::debug::Looking for validators in {validators_file}")
    spec = importlib.util.spec_from_file_location("custom_loaded_yamale_validators", validators_file)
    module = importlib.util.module_from_spec(spec)
    sys.modules["custom_loaded_yamale_validators"] = module
    spec.loader.exec_module(module)
    for cl in inspect.getmembers(module, inspect.isclass):
        if inspect.isclass(cl) and not issubclass(cl, Validator) and not cl == Validator:
            continue
        print(f"::debug::Found validator {cl[1].tag}")
        validators[cl[1].tag] = cl[1]

schema = yamale.make_schema(schema_path, validators=validators)

def unknown(loader, suffix, node):
    if isinstance(node, yaml.ScalarNode):
        constructor = loader.__class__.construct_scalar
    elif isinstance(node, yaml.SequenceNode):
        constructor = loader.__class__.construct_sequence
    elif isinstance(node, yaml.MappingNode):
        constructor = loader.__class__.construct_mapping
    data = constructor(loader, node)
    return data
yaml.add_multi_constructor('!', unknown, Loader=yaml.CSafeLoader)

files_to_validate = list()
any_error = False
for file in glob.glob("./**", recursive=True):
    filename = os.fsdecode(file)
    actual_path = filename[1:] #cuts out the . from the path
    if path_pattern.match(actual_path):
        data = yamale.make_data(filename)
        try:
            yamale.validate(schema, data, strict=strict)
            print(f"::debug::Successfully validated file {actual_path}")
        except YamaleError as e:
            any_error = True
            for result in e.results:
                for error in result.errors:
                    print(f"::error file={actual_path}::{error}")

if any_error:
    exit(1)

