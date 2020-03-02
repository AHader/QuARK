from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'pages/home.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('users:update'))

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
