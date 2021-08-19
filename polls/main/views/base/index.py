import uuid

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    client_id = request.session.get('client_id', None)
    if client_id is None:
        client_id = str(uuid.uuid4())
        request.session['client_id'] = client_id

    return render(request, 'main/index.html', {
        'client_id': client_id
    })

def index2(request: HttpRequest, pk) -> HttpResponse:
    client_id = request.session.get('client_id', None)
    if client_id is None:
        client_id = str(uuid.uuid4())
        request.session['client_id'] = client_id

    return render(request, 'main/selected_poll_with_questions.html', {
        'client_id': client_id,
        'pk': pk,
    })
