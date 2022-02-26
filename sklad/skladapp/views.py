from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View


from .models import *


class ClientView(View):

    def get(self,request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            c = Client.objects.filter(ombor=o)
            return render(request, 'clients.html', {'all_clients': c})
        else:
            return redirect('login')
    def post(self,request):
        a = Ombor.objects.get(user=request.user)
        Client.objects.create(
            dokon_nomi=request.POST['client_shop'],
            manzil=request.POST['client_address'],
            tel=request.POST['client_phone'],
            ism=request.POST['client_name'],
            qarz=request.POST['client_qarzi'],
            ombor=a
        )
        return redirect('goods')
class Client_updateView(View):

    def get(self, request,son):
        if request.user.is_authenticated:
            c = Client.objects.get(id=son)
            return render(request,'client_update.html',{'client':c})
        else:
            return redirect('login')
    def post(self, request, son):
        client = Client.objects.get(id=son)
        client.ism = request.POST.get('client_name')
        client.tel = request.POST['client_phone']
        client.dokon_nomi = request.POST['client_shop']
        client.manzil = request.POST['client_address']
        client.save()
        return redirect('clients')

class Product_updateView(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            c = Product.objects.get(id=son)
            return render(request, 'product_update.html', {'product': c})
        else:
            return redirect('login')
    def post(self, request, son):
        if request.user.is_authenticated:
            product = Product.objects.get(id=son)
            product.nom = request.POST.get("name")
            product.brend_nomi = request.POST["brand_name"]
            product.kelgan_narx = request.POST["price"]
            product.sotuvdagi_narx = request.POST["price2"]
            product.miqdor=request.POST["amount"]
            product.save()
            return redirect('stats')
        else:
            return redirect('login')

class ProductView(View):
    def get(self,request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            p = Product.objects.filter(ombor=o)
            return render(request,'products.html',{'all_products':p})
        else:
            return redirect('login')
    def post(self,request):
        a = Ombor.objects.get(user=request.user)
        Product.objects.create(
            nom=request.POST.get('nom'),
            brend_nomi=request.POST.get('brend'),
            kelgan_narx=request.POST.get('kelgan narxi'),
            sotuvdagi_narx=request.POST.get('sotuvdagi_narxi'),
            miqdor=request.POST.get('miqdori'),
            ombor=a
        )
        return redirect('stats')






class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
class IndexView(View):
    def get(self,request):
        return render(request, 'index.html')


    def post(self,request):
        l =request.POST['login']
        p = request.POST['password']
        user = authenticate(username=l,password=p)
        if user is None:
            return redirect('login')
        else:
            login(request, user)
            return redirect('/bolim')

class BulimlarView(View):
    def get(self,request):
        if request.user.is_authenticated:

            return render(request, 'bulimlar.html')
        else:
            return redirect('login')


def Logout(request):
    logout(request)
    return redirect('/')
