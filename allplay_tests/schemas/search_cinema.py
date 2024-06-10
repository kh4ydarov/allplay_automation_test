search_movie = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "data": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "category_id": {
                            "type": "integer"
                        },
                        "title": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "category_id",
                        "title",
                        "description"
                    ]
                }
            ]
        }
    },
    "required": [
        "data"
    ]
}
