from functools import partial

from __MY_APP__.user import User
from __MY_APP__.typing import Maybe, Success
from __MY_APP__.functools import bind


def _create_token(user: User) -> Maybe[Success]:
    print(user)
    return Success({'token': 'TODO'}, 200)


create_token = partial(bind, _create_token)
