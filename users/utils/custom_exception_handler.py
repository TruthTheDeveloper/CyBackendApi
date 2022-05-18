from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    exception_class = exc.__class__.__name__ 
    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
        if exception_class == 'ValidationError':
            response.data['message'] = "username or email already exist"


    return response