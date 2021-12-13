
import jwt
import logging

from functools import wraps
from flask import abort, request
from passlib.hash import pbkdf2_sha256
from server.extensions import auth

# TOKEN_ALGO = 'RS512'
TEN_YEARS = 60 * 60 * 24 * 7 * 52 * 10
ONE_YEARS = 60 * 60 * 24 * 7 * 52

decorator_with_args = lambda decorator: lambda *args, **kwargs: lambda func: decorator(func, *args, **kwargs)

LOG = logging.getLogger(__name__)


def extract_payload(token):
    try:
        payload = jwt.decode(token, auth.public_key(), audience=auth.audience, algorithm=auth.token_algo)
        return payload
    except jwt.ExpiredSignatureError as e:
        LOG.error((str(e) + " ExpiredSignatureError"))
        raise
    except jwt.InvalidTokenError as e:
        LOG.error((str(e) + " InvalidTokenError"))
        raise
    except Exception as e:
        LOG.error((str(e) + " Error"))
        raise
    return False


def authentication_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(403, 'User not logged or no token received')
        token = request.headers['Authorization']
        token = token.split('Bearer ')
        if len(token) > 1:
            token = token[1]
        else:
            abort(403, 'Empty token')
        try:
            payload = extract_payload(token)
        except Exception as e:
            abort(403, 'User not logged or session expired ' + str(e))
        else:
            return f(user=payload, *args, **kwargs)
    return decorated_function


@decorator_with_args
def permissions(f, permissions=None):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_permission = kwargs['user'].get('permission', '')
        if not permissions:
            return f(*args, **kwargs)
        perms = permissions
        if not isinstance(permissions, tuple):
            perms = (permissions, )
        if user_permission not in perms:
            abort(403, 'User has not enough privilege')
        else:
            return f(*args, **kwargs)
    return decorated_function


def hash_password(password):
    return pbkdf2_sha256.encrypt(password, rounds=1000000, salt_size=16)


def verify_password(xhash, password):
    return pbkdf2_sha256.verify(password, xhash)
