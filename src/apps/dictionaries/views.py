from django.views.generic.base import TemplateView


class DictionariesView(TemplateView):
    template_name = 'dictionaries/index.html'
