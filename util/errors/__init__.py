class CustomError(Exception):
    pass

class NoInternetConnection(CustomError):
    pass

class InvalidProgressBar(CustomError):
    pass
