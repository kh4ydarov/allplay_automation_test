invalid_sign_in = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "errors": {
      "type": "object",
      "properties": {
        "email": {
          "type": "array",
          "items": [
            {
              "type": "string"
            }
          ]
        }
      },
      "required": [
        "email"
      ]
    }
  },
  "required": [
    "errors"
  ]
}