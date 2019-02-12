from django.shortcuts import render
from .models import Page


def page_list_view(request):
    context = {
        "pages":Page.objects.all()
    }
    return render(request, 'list.html', context)




def page_detail_view(request, page_id):
    context = {
        "page":Page.objects.get(id=page_id)
    }
    return render(request, 'detail.html', context)

