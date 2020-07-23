from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from shop.models import Categorie, Produit



# Create your views here.
def products(request):

    #produit = Produit.objects.filter(status=True)

    datas = {
     #   "produit":produit
    }


    return render(request, 'pages/shop.html', datas)

def product(request,id):

    produit_single = get_object_or_404(Produit, id=id)
    produits = Produit.objects.filter(status=True)[:5]


    datas= {

        "single": produit_single
    }

    return render(request, 'pages/single-shop.html',datas)
