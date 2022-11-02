from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

# we want an object containing a required schema
values_and_quantifier_schema = {
   'type': 'object',
   'properties': {
         "values": {
                    "type": "array",
                    "items": {
                        "description": "List of indoor hobbies",
                        "type": "number"
                    }
                },
         "quantifier": {
             "type": "number"
         }
   },
   'required': ['values', 'quantifier']
}

values_schema = {
   'type': 'object',
   'properties': {
         "values": {
                    "type": "array",
                    "items": {
                        "description": "List of indoor hobbies",
                        "type": "number"
                    }
                }
   },
   'required': ['values']
}


class InputsValidatorWithQuantifier(Inputs):
   json = [JsonSchema(schema=values_and_quantifier_schema)]


class InputsValidator(Inputs):
   json = [JsonSchema(schema=values_schema)]


def validate_input(request, is_quantifier):
    if is_quantifier:
        inputs = InputsValidatorWithQuantifier(request)
    else:
        inputs = InputsValidator(request)

    if inputs.validate():
        return None
    else:
        return inputs.errors
