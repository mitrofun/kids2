from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from children.models import Child


class ChildrenBaseView(LoginRequiredMixin):
    model = Child
    context_object_name = 'children'


class ChildrenListView(ChildrenBaseView, ListView):
    template_name = 'children/children_list.html'

    def get_queryset(self):
        return Child.objects.all()


class ChildrenCreateView(ChildrenBaseView, CreateView):
    template_name = 'children/children_edit.html'
    context_object_name = 'child'
    fields = '__all__'


class ChildrenDetailView(ChildrenBaseView, DetailView):
    template_name = 'children/children_detail.html'
    context_object_name = 'child'


class ChildrenUpdateView(ChildrenBaseView, UpdateView):
    template_name = 'children/children_edit.html'
    context_object_name = 'child'
    fields = '__all__'
