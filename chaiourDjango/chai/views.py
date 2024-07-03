from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_list_or_404

# Create your views here.
def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request,"chai.html",{'chais':chais})

def chai_detail(request,chai_id):
    chai=get_list_or_404(ChaiVarity,pk=chai_id)
    return render (request,'chai_detail.html',{'chai':chai})