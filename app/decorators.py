from app.models import MainLog


def a_decorator_passing_logs(func):
    def wrapper_logs(request, *args, **kwargs):
        message = {}
        
        try:
            client_address = request.META['HTTP_X_FORWARDED_FOR']
        except KeyError:
            client_address = request.META.get('REMOTE_ADDR')
        
        message['path_info'] = request.META.get('PATH_INFO')
        message['method'] = request.method
        
        user = request.user
        if str(request.user) == 'AnonymousUser':
            user = None
        
        if request.method == 'POST':
            message['post_data'] = request.POST

        response_func = func(request, *args, **kwargs)
        response_content_type = response_func._headers['content-type'][1]
        response = b'<html>'
        if 'json' in response_content_type:
            response = response_func._container[0]
            
        MainLog.objects.create(user=user,
                               message=message,
                               client_address=client_address,
                               raw=str({'raw_request': message,
                                        'HTTP_USER_AGENT': request.META.get('HTTP_USER_AGENT'),
                                        'HTTP_CONNECTION': request.META.get('HTTP_CONNECTION'),
                                        'response_headers': response_func._headers,
                                        'response': response.decode('utf-8')})
                               )
        
        return response_func
    
    return wrapper_logs
