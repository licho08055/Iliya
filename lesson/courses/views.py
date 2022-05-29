from django.shortcuts import render
from django.views import View
# Create your views here.

class CourseView(View):
    template_name = 'about.html'
    def get(self,resp):
        return render(resp, self.template_name)