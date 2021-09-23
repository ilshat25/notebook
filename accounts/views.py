from django.shortcuts import render

# Авторизация через провайдеров
def login_view(request):
    return render(request, 'accounts/login.html', {})
