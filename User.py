class User:
    def __init__(self, user_id, user_name, email, phone_number, active=True):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.phone_number = phone_number
        self.active = active
