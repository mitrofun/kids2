from django.views.generic.base import TemplateView
from dictionaries.models import Category


class DictionariesView(TemplateView):
    template_name = 'dictionaries/index.html'

    def get_context_data(self, **kwargs):
        context = super(DictionariesView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


