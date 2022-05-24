from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

from .models import AdvUser
from .forms import ChangeUserInfoForm, RegisterUserForm

# user profile, authorizied only
@login_required
def profile(request):
    return render(request, 'main/profile.html')

# rendering main page
def index(request):
    return render(request, 'main/index.html')

# rendering page by name or exception
def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


# login
class BbLoginView(LoginView):
    template_name = 'main/login.html'

# logout
class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'

# change user info
class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile')
    success_message = 'Данные пользователя изменены'

    # take an id of current user
    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    # take a queryset by id
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

# password change
class BBPaswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'main/password_change.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'Пароль пользователя изменен'

# register user
class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'main/rregister_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')

# success register message
class RegisterDoneViews(TemplateView):
    template_name = 'main/register_done.html'