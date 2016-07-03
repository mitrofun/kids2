from django.views.generic.base import TemplateView


class SecondaryView(TemplateView):
    template_name = 'dictionaries/secondary.html'
