from django.views.generic.base import TemplateView


class AddressView(TemplateView):
    template_name = 'dictionaries/address.html'
