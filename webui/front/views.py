from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from .models import Coser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request, pages = 1):
    cosers = Coser.objects.order_by('-id')
    paginator = Paginator(cosers, 48)
    page = pages
    try:
        coser = paginator.page(page)
    except PageNotAnInteger:
        coser = paginator.page(1)
    except EmptyPage:
        coser = paginator.page(paginator.num_pages)

    return render_to_response('web/templatePic.html',{"cosers": coser})