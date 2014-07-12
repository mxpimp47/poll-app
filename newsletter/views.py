from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm


class SignUp(SuccessMessageMixin, CreateView):
    form_class = SignUpForm
    template_name = 'newsletter/signup.html'
    success_message = "%(email_field)s was created successfully"
    success_url = reverse_lazy('newsletter-signup')
