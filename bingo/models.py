from django.db import models
from random import shuffle
from django.contrib.sessions.models import Session


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=255)

    def generate_card(self, session):
        term_list_unfree = list(self.terms.filter(free_space=False))
        term_list_free = list(self.terms.filter(free_space=True))

        shuffle(term_list_unfree)

        terms = term_list_unfree[:24]
        terms.insert(12, term_list_free[0])

        card = Card(session=session)
        card.save()
        for i, term in enumerate(terms):
            OrderedTerm(term=term, index=i, card=card).save()
        return card

    def __str__(self):
        return self.name


class Term(models.Model):
    text = models.CharField(max_length=255)
    game = models.ForeignKey('Game', related_name='terms')
    free_space = models.BooleanField()

    def __str__(self):
        return self.text


class OrderedTerm(models.Model):
    term = models.ForeignKey('Term')
    index = models.IntegerField()
    card = models.ForeignKey('Card', related_name='terms')
    checked = models.BooleanField(default=False)


class Card(models.Model):
    session = models.CharField(max_length=32, unique=True)
