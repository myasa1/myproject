from django.shortcuts import render

# Create your views here.
from .models import product

def product_list(request):
    product_list = product.objects.all()
    context ={'product_list':product_list}
    
    return render(request,'prodect/product_list.html',context)
    
    

def product_detail():
    pass

