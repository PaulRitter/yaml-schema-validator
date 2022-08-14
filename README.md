# Yaml Schema Validator

[![.github/workflows/test.yml](https://github.com/PaulRitter/yaml-schema-validator/actions/workflows/test.yml/badge.svg)](https://github.com/PaulRitter/yaml-schema-validator/actions/workflows/test.yml)

A github action used to validate yaml files using [Yamale](https://github.com/23andMe/Yamale). With this action, you can add you own custom yamale validators, use a RegEx pattern to select files to validate and specify the yamale version you wish to use.

For info on schema syntax, please consult the yamale readme.

I made the error output as verbose as it gets, sadly yamale doesnt provide more info on where in the file the schema violation was found, meaning no column/row indices for our errors.

## Usage
### `schema`:
**Required** The path to the schema file you want to use to validate the yaml files.
### `path_pattern`:
**Required** A RegEx pattern matching the files you want to validate.
### `validators_path`:
The path to a python file containing custom validator classes to be used in validation.
### `validators_requirements`:
The path to a pip requirements file containing packages needed to run the validators python file.
### `strict`:
Control wether or not strict mode is used. (On by default)
### `yamale`:
Sets the used yamale version. If not specified, the latest version served by pip is used.

**Note:** Only Yamale versions >=3.0.0 are supported, since Yamale 2.0.0 does not yet contain types i rely on for this workflow to function. If you can/want to figure out a way around this, feel free to send a pr, i just dont see the need.

All path-related inputs are relative to the repository root.

## Example usage

The files referenced in this example can be found in the [example folder](/example).

```yaml
name: YAML Schema Validator
on: [push]

jobs:
  yaml-schema-validation:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - uses: PaulRitter/yaml-schema-validator@v2
      with:
        schema: attribution_schema.yml
        path_pattern: .*attribution.ya?ml$
        validators_path: validators.py
        validators_requirements: requirements.txt
        yamale: 4.0.0
        strict: true
```


## Local testing

```
docker build -t local .

docker run -e INPUT_VALIDATORS_REQUIREMENTS=example/requirements.txt -e INPUT_SCHEMA=example/attribution_schema.yml -e INPUT_PATH_PATTERN=.*example/.+_file\.yml$ -e INPUT_VALIDATORS_PATH=example/validators.py -e INPUT_STRICT='TRUE' local
```