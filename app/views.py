from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

#class file(TemplateView):
  #  template_name='file.html'

class file2(TemplateView):
    template_name='file2.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['data']='hello how are u guys'
        context['ab']='cd'
        return context