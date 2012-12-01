# This file is part of PyImgur.

# PyImgur is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# PyImgur is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with PyImgur.  If not, see <http://www.gnu.org/licenses/>.

'''
Decorators. Mainly used to ensure proper authentication before use.
'''

from functools import wraps

# I would love to do from . import errors, _client. But sadly this gives
# problems as _client is not defined at the runtime.

import pyimgur

def require_authentication(function):
    """
    Decorator for functions that require an api key.

    So far, the only function that doesn't require this is
    info_image.
    """

    @wraps(function)
    def wrapped(*args, **kwargs):
        if pyimgur._client is None or pyimgur._client.token is None:
            raise pyimgur.errors.AccessDeniedError('You need to be authenticated to do that')
        return function(*args, **kwargs)
    return wrapped

def _client_has_consumer(function):
    """
    Decorator for functions that require consumer info has been added to _client

    So far, the only function that doesn't require this is info_image.
    """

    @wraps(function)
    def wrapped(*args, **kwargs):
        if pyimgur._client != None:
            return function(*args, **kwargs)
        else:
            raise pyimgur.errors.AccessDeniedError('You need to be authenticated to do that')
    return wrapped