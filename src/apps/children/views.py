from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from children.models import Child


class ChildrenBaseView(LoginRequiredMixin):
    model = Child
    context_object_name = 'children'


class ChildrenListView(ChildrenBaseView, ListView):
    template_name = 'children/children_list.html'

    def get_queryset(self):
        return Child.objects.all()
