from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def example_view(request: HttpRequest):
    '''
    This is a view function that returns a simple HTML page.
    '''
    return render(request, 'my_app/example.html')

# def variable_view(request: HttpRequest):
#     '''
#     This is a view function that returns a simple HTML page with variables.
#     '''
#     my_var = {
#         'first_name': 'john',
#         'last_name': 'doe',
#         'some_list': [1, 2, 3],
#         'user_logged_in': True,
#     }
#     return render(request, 'my_app/variable.html', context=my_var)

def variable_view(request: HttpRequest):
    '''
    This is a view function that returns a simple HTML page with variables.
    '''

    return render(request, 'my_app/variable.html')