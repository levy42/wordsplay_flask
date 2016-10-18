from functools import wraps
from flask import Blueprint, Response, jsonify


class ErrorResponse(Response):
    def __init__(self, message):
        super(ErrorResponse, self).__init__()
        self.data = jsonify(status='error', data=message)


class SuccessResponse(Response):
    def __init__(self, data):
        super(SuccessResponse, self).__init__()
        self.data = jsonify(status='success', data=jsonify(data))


class Rest(Blueprint):
    def route(self, rule, **options):
        """Like :meth:`Flask.route` but for a blueprint.  The endpoint for the
        :func:`url_for` function is prefixed with the name of the blueprint.
        """

        def decorator(f):
            decorated_rule = self.rest(rule)
            endpoint = options.pop("endpoint", f.__name__)
            self.add_url_rule(decorated_rule, endpoint, f, **options)
            return f

        return decorator

    def rest(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                data = func(*args, **kwargs)
                return SuccessResponse(data)
            except Exception as e:
                return ErrorResponse(str(e))

        return wrapper
