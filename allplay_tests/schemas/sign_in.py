login_user = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "api_token": {
            "type": "string"
        },
        "data": {
            "type": "object",
            "properties": {
                "api_token": {
                    "type": "string"
                },
                "api_refresh_token": {
                    "type": "string"
                },
                "api_token_expire_at": {
                    "type": "string"
                },
                "now": {
                    "type": "string"
                },
                "is_new": {
                    "type": "boolean"
                }
            },
            "required": [
                "api_token",
                "api_refresh_token",
                "api_token_expire_at",
                "now",
                "is_new"
            ]
        }
    },
    "required": [
        "api_token",
        "data"
    ]
}
