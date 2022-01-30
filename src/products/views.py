from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.

# Alternative method to setting default data directly on the form at forms.py
# def render_initial_data(request):
#     initial_data = {
#         'title': 'Title',
#         'description': 'Description',
#         'price': '0.99'
#     }
#     form = RawProductForm(request.POST or None, initial=initial_data)
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     my_form = RawProductForm() # initializes with GET by default, same as request.GET
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data) # create requires two arguments, hence **
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", context)


# this method works but is very poor because it deos validate data
# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#         # Product.objects.create(title=my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm() # Re-render form to clear it

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

# def product_detail_view(request):
#     obj = Product.objects.get(id=2)
#     # context = {
#     #     'title': obj.title,
#     #     'description': obj.description,
#     # }
#     context = {
#         'object': obj
#     }
#     return render(request, "products/product_detail.html", context)

def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id) # preferred method; shorter syntax than try-except block
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        'object': obj,
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # POST request
    if request.method == 'POST':
        # confirming delete
        obj.delete()
        return redirect('/')
    context = {
        'object': obj
    }
    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/product_list.html", context)