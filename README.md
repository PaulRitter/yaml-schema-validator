# Yaml Schema Validator

A github action used to validate yaml files using [Yamale](https://github.com/23andMe/Yamale)

For info on schema syntax, please consult the yamale readme.

An example can be found in the [example folder](/example)

## Usage
The workflow has four inputs, two of them required:
- `schema`: The path to the schema file you want to use to validate the yaml files
- `path_pattern`: A regex pattern matching the files you want to validate.
- (optional) `validators_path`: The path to a python file containing custom validator classes to be used in validation
- (optional) `validators_requirements`: The path to a pip requirements file containing packages needed to run the validators python file
- (optional) `strict`: Control wether or not strict mode is used (On by default)
- (optional) `yamale`: Sets the used yamale version. If not specified, the latest version served by pip is used. Note: Only Yamale versions >=3.0.0 are supported, since Yamale 2.0.0 does not yet contain types i rely on for this workflow to function. If you can/want to figure out a way around this, feel free to send a pr, i just dont see the need.

All path-related inputs are relative to the repository root.

I made the error output as verbose as it gets, sadly yamale doesnt provide more info on where in the file the schema violation was found, meaning no column/row indices for our errors.