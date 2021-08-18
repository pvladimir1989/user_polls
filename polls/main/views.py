from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.conf import settings


def index(request: HttpRequest) -> HttpResponse:
    turn_on_block = settings.MAINTENANCE_MODE

    return render(request, 'main/index.html', {
        "turn_on_block": turn_on_block,
    })
