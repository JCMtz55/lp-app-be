from functools import wraps
from flask import request
import os
import cognitojwt

AWS_REGION = os.environ.get("AWS_REGION")
AWS_COGNITO_POOL_ID = os.environ.get("AWS_COGNITO_POOL_ID")
AWS_COGNITO_CLIENT_ID = os.environ.get("AWS_COGNITO_CLIENT_ID")


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            data: dict = cognitojwt.decode(
                token,
                AWS_REGION,
                AWS_COGNITO_POOL_ID,
                app_client_id=AWS_COGNITO_CLIENT_ID,  # Optional
                testmode=True  # Disable token expiration check for testing purposes
            )
            current_user = data['cognito:username']
            if current_user is None:
                return {
                    "message": "Invalid Authentication token!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": token,
                "error": str(e)
            }, 500

        return f(current_user, *args, **kwargs)

    return decorated
