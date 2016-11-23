from django.shortcuts import render
from bingo.models import Card, Game, OrderedTerm
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def bingo(request):
    try:
        card = Card.objects.get(session=request.session.session_key)
    except Card.DoesNotExist:
        card = Game.objects.first().generate_card(request.session.session_key)
    return render(request, 'bingo.html', {'terms': card.terms.all().order_by('index')})


@csrf_exempt
def toggle(request):
    term = OrderedTerm.objects.get(pk=request.POST.get('id'))
    term.checked = not term.checked
    term.save()
    return HttpResponse('OK')
