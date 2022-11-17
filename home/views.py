from django.shortcuts import render

# Create your views here.


def home(request):
    """

    :param request:
    :return:
    """
    return render(request, "home/home.html")