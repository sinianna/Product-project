from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from  . models import Product
from . forms import ProductForm

def product_list(request): # landing page
    products = Product.objects.all()
    return render(request,'product_list.html',{'products': products})

def product_detail(request, id): #detailed view
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

def product_create(request):  #Create the product
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)#request.FILES used for image handling. Ajesh
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

def product_update(request, id):  #Update the product
    products = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        #form = ProductForm(request.POST, instance=products)#instance load the stored data ,,old code wrong
        form = ProductForm(request.POST, request.FILES, instance=products)# corrected by ajesh
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=products)
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, id):  # Delete the product
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        product.delete()
        
        return redirect('product_list')
    return render(request, 'product_delete.html', {'product': product})
