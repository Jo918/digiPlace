from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from marketplace.models import Productos
from django.core.paginator import Paginator



class HomeView(View):
    def get(self, request, *args, **kwargs):
        productos = Productos.objects.filter(activo=True)


        if productos:
            paginator = Paginator(productos, 9)
            page_number = request.GET.get('page')
            digital_products_data = paginator.get_page(page_number)

        context = {
            'producto': digital_products_data

        }
        return render(request, 'pages/index.html', context)
    