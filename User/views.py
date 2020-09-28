from django.shortcuts import render


def user_view(request):
    return render(request,'User/index.html')

