from django.shortcuts import render, redirect
from django.views import View

from statisticapp.models import Stats

from skladapp.models import Ombor,Client,Product




class StatisticView(View):
    def get(self,request):
        if request.user.is_authenticated:
            soz = request.GET.get("soz")
            qidirish = request.GET.get('qidirish')
            if qidirish == 'p' and soz != '':
                o = Ombor.objects.get(user=request.user)
                mahsulot = Product.objects.filter(ombor=o,nom=soz)
                s = Stats.objects.filter(ombor=o,product=mahsulot[0])
                C = Client.objects.filter(ombor=o)
                p = Product.objects.filter(ombor=o)
                return render(request, 'stats.html', {"stats":s, "ombor":o,'clients':C,'products':p})
            elif qidirish == 'c' and soz != '':
                o = Ombor.objects.get(user=request.user)
                client = Client.objects.filter(ombor=o,ism_contains=soz)
                if len(client) == 0:
                    client = Client.objects.filter(ombor=o, nom_contains=soz)
                s = Stats.objects.filter(ombor=o,client=client[0])
                C = Client.objects.filter(ombor=o)
                p = Product.objects.filter(ombor=o)
                return render(request, 'stats.html', {"stats":s, "ombor":o,'clients':C,'products':p})
            else:
                o = Ombor.objects.get(user=request.user)
                C = Client.objects.filter(ombor=o)
                p = Product.objects.filter(ombor=o)
                s = Stats.objects.filter(ombor=o)
                return render(request,'stats.html',{"all_statis":s,"products":p,"clients":C})
        else:
            return redirect('login')
    def post(self,request):
        a = Ombor.objects.get(user=request.user)
        p=request.POST['product']
        m =request.POST['miqdor']
        c=request.POST['client']
        n = request.POST['nasiya']
        # u = request.POST["summa"],
        # t  = request.POST["tolandi"],
        # n = u - t

        Stats.objects.create(
            product=Product.objects.get(id=p),
            client=Client.objects.get(id=c),
            sanasi= request.POST["sana"],
            miqdor= m,
            umumiy_summa= request.POST["summa"],
            tolandi= request.POST["tolandi"],
            nasiyaga= n,
            ombor=a
        )
        pro = Product.objects.get(id=p)
        pro.miqdor=int(pro.miqdor) - int(m)
        pro.save()
        cl = Client.objects.get(id=c)
        cl.qarz = int(cl.qarz) + int(n)
        cl.save()
        return redirect('statis')

# Create your views here.
