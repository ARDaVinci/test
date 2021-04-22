from django.views.generic import TemplateView

# Create your views here.

class TestPage(TemplateView):
    template_name = 'collapseapp/test.html'