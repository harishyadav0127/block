from django.shortcuts import render
from .forms import BlockForm
from.models import Block
from django.http import HttpResponseRedirect

def create_block(request):
    try:
        form = BlockForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/getblock/')
        return render(request, "create_view.html", {'form': form})
    except:
        return render(request, "error_view.html")


def block_list(request):
    try:
        return render(request, "list_view.html", {"dataset":Block.objects.all()})
    except:
        return render(request, "error_view.html")
