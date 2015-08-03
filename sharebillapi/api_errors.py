
class api_errors():
    SUCCESS = 0
    UNEXPECTED_ERROR = 1
    TOKEN_EXPIRED = 2
    ACCOUNT_EXIST = 3
    INVALID_PASSWORD = 4
    FORM_INVALID = 5
    ACCOUNT_DIABLED = 6
    USER_NOT_FOUND = 7

class api_errors_message():
    SUCCESS = 'Success'
    UNEXPECTED_ERROR = 'Unexpected error.'
    USER_NOT_FOUND = 'User not found.'
    TOKEN_EXPIRED = 'Token expired.'
    ACCOUNT_EXIST = 'Account exist.'
    INVALID_PASSWORD = 'Invalid password'
    FORM_INVALID = 'Form invalid.'
    ACCOUNT_DIABLED = 'Account disabled.'