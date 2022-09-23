class InputError(Exception):
    def __init__(self, user_input):
        super().__init__()
        self.user_message = f"Invalid input: '{user_input}'. Please try again."