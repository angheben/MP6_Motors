from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    This class will serve as a template for the base.html file
    """
    template_name = "base.html"
