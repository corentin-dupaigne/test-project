ADMIN_CREDENTIALS = {
    "valid": {"username": "admin", "password": "password"},
    "invalid_password": {"username": "admin", "password": "wrongpassword"},
    "invalid_user": {"username": "unknown", "password": "password"},
    "empty": {"username": "", "password": ""},
}

CONTACT_FORM = {
    "valid": {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "01234567890",
        "subject": "Booking enquiry",
        "message": "Hello, I would like to enquire about a room booking for next month. Please get back to me.",
    },
    "missing_name": {
        "name": "",
        "email": "john.doe@example.com",
        "phone": "01234567890",
        "subject": "Booking enquiry",
        "message": "Hello, I would like to enquire about a room booking.",
    },
    "invalid_email": {
        "name": "John Doe",
        "email": "not-an-email",
        "phone": "01234567890",
        "subject": "Test subject",
        "message": "Hello, this is a test message with invalid email address provided.",
    },
    "short_message": {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "phone": "01234567891",
        "subject": "Hi",
        "message": "Hi",
    },
}

ROOM_DATA = {
    "valid_single": {
        "name": "101",
        "type": "Single",
        "accessible": False,
        "price": "100",
    },
    "valid_double": {
        "name": "202",
        "type": "Double",
        "accessible": True,
        "price": "150",
        "features": ["WiFi", "TV"],
    },
    "missing_price": {
        "name": "303",
        "type": "Twin",
        "accessible": False,
        "price": "",
    },
}

BOOKING_DATA = {
    "valid": {
        "firstname": "Alice",
        "lastname": "Smith",
        "email": "alice.smith@example.com",
        "phone": "07700900000",
    },
    "missing_firstname": {
        "firstname": "",
        "lastname": "Smith",
        "email": "alice.smith@example.com",
        "phone": "07700900000",
    },
    "invalid_email": {
        "firstname": "Bob",
        "lastname": "Jones",
        "email": "not-valid",
        "phone": "07700900001",
    },
}
