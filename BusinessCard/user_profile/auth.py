class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


def validate_user(request,user_id):
    
    if request.user.id != user_id:
        raise AuthError({
            'code':'invalid user id',
            'description':"user_id does not match with the system"},400)


