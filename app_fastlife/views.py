from django.shortcuts import render


def index(request):
    return render(request, "app_fastlife/index.html", context={"Prom" : "Toi"})