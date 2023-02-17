import environ

    
def get_api_key_stripe() -> str:
    env = environ.Env()
    return env('API_KEY_STRIPE')


def get_public_key() -> str:
    env = environ.Env()
    return env('API_PUBLIC_KEY_STRIPE')