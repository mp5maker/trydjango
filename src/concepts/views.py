from django.shortcuts import render
from django.views import View

# Base View Class = View
class IndexView(View):
    template_name = "concepts/index.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

# HTTP METHODS
def index(request, *args, **kwargs):
    print(request.method)
    return render(request, 'concepts/index.html', {})
