invalid_confirmation = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "errors": {
      "type": "object",
      "properties": {
        "default": {
          "type": "array",
          "items": [
            {
              "type": "string"
            }
          ]
        }
      },
      "required": [
        "default"
      ]
    }
  },
  "required": [
    "errors"
  ]
}