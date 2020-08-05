from django.views.generic import TemplateView
from flashcards_app.views import DeckListView

class Home(DeckListView):
    template_name = 'home.html'
