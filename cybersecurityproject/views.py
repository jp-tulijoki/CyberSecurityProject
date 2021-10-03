from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

logged_in = False
valid_users = [{'username': 'admin', 'password': 'password'}]


def home(request):
    print(logged_in)
    comments = request.session.get('comments', [])
    return render(request, 'pages/index.html', {'comments': comments, 'logged_in': logged_in})


def login(request):
    global logged_in
    username = request.POST.get('username')
    password = request.POST.get('password')
    user_index = None
    for user in valid_users:
        if user['username'] == username:
            assert user['password'] == password
            logged_in = True
    return redirect('/', {'logged_in': logged_in})


@csrf_exempt
def post_comment(request):
    comments = request.session.get('comments', [])
    comment = request.POST.get('comment', '').strip()
    comments.append(comment)
    request.session['comments'] = comments
    return render(request, 'pages/index.html', {'comments': comments})
