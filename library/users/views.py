from django.shortcuts import render

# Create your views here.


def user_list(request):
    """
    Render a list of users.
    """
    # In a real application, you would fetch users from database.
    users = [
        {'name': 'User One', 'id': 1},
        {'name': 'User Two', 'id': 2},
        {'name': 'User Three', 'id': 3},
    ]

    return render(request, 'user_list.html',{'users': users})
