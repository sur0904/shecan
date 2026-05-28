from django.shortcuts import render
from django.http import JsonResponse

from .models import Register


def home(request):

    return render(request, 'home.html')


def register(request):

    if request.method == "POST":

        name = request.POST.get('name')

        email = request.POST.get('email')

        message = request.POST.get('message')

        Register.objects.create(
            name=name,
            email=email,
            message=message
        )

        context = {
            'name': name,
            'email': email,
            'message': message
        }

        return render(request, 'welcome.html', context)

    return render(request, 'register.html')


def api_data(request):

    data = list(
        Register.objects.values()
    )

    return JsonResponse(data, safe=False)