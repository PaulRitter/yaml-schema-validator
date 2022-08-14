from yamale.validators import Validator
import validators

class License(Validator):
    tag = "license"
    licenses = ["Custom", "CC-BY-3.0", "CC-BY-NC-SA-3.0", "MIT"]

    def _is_valid(self, value):
        return value in self.licenses

class Url(Validator):
    tag = "url"

    def _is_valid(self, value):
        return validators.url(value)