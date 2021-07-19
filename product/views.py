from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product

# Create your views here.
def product(request):
    if(request.method == 'POST'):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        product_header = request.POST.get('product_header')
        plot_no = request.POST.get('plot_no')
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        product_body = request.POST.get('product_body')

        product = Product(first_name=first_name, last_name=last_name, product_header=product_header, plot_no= plot_no, lat=lat, lng=lng, product_body=product_body)
        product.save()

        return render(request, 'pages/webmap.html')

    selector = Product.objects.all()
    context = {
        'product': selector
    }
    return render(request, 'pages/product.html', context)