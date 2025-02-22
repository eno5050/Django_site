from django.shortcuts import render
from django.http import HttpResponse
from .models import TopImage
from django.template import loader


def index(request):
    latest_topimage_list = TopImage.objects.filter(no=1)
    template = loader.get_template("top/index.html")
    context = {
        "latest_topimage_list": latest_topimage_list,
    }
    return HttpResponse(template.render(context, request))