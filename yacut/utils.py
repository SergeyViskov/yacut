import random
import string

from .models import URLMap


def get_random_string():
    short = ''.join(
        random.choice(string.ascii_letters + string.digits) for _ in range(6)
    )
    while URLMap.query.filter_by(short=short).first():
        short = ''.join(
            random.choice(
                string.ascii_letters + string.digits
            ) for _ in range(6)
        )
    return short
