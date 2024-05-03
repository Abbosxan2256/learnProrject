from django.views.generic import ListView, DetailView, CreateView

from apps.forms import RegisterModelForm
from apps.models import Person


class IndexListView(ListView):
    queryset = Person.objects.all()
    template_name = 'apps/index.html'
    context_object_name = 'index'

    paginate_by = 3


class RegisterCreateView(CreateView):
    form_class = RegisterModelForm
    template_name = 'apps/register.html'
    success_url = 'login'


class ProfileDetailView(DetailView):
    queryset = Person.objects.all()
    template_name = 'apps/profile.html'
    context_object_name = 'detail'
