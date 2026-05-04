def normalize(record):
    """
    Normalize incoming source fields
    """

    mapping = {
        "EmailAddress": "email",
        "user_email": "email",
        "email": "email",
        "PhoneNumber": "phone",
        "mobile_no": "phone",
        "FullName": "name",
        "username": "name"
    }

    normalized = {}

    for key, value in record.items():
        new_key = mapping.get(key, key.lower().strip())

        if value == "":
            value = None

        normalized[new_key] = value

    return normalized