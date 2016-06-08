from django.http import HttpResponse
from django.shortcuts import render

from lucky_money.models import LuckMoney, LuckMoneyQuota


def home(request):
    luck_money = LuckMoney.objects.all()
    return render(request, 'home.html',locals())

def generate_all(request,pk):
    LuckMoney.objects.get(pk=pk)
    return HttpResponse("成功")

def generate_one(request,pk):
    luck_money = LuckMoney.objects.get(pk=pk)
    if request.method=="POST":
        amount = request.POST['amount']
        print(amount)
        if luck_money.quota_count >= luck_money.quantity:
            return HttpResponse("失败")
        if int(amount) > luck_money.amount_rest:
            return HttpResponse("失败")
        else:
            luck_money.luckmoneyquota_set.create(amount=amount)
            return HttpResponse("成功")

def quota(request,pk):
    lm = LuckMoney.objects.get(pk=pk)
    luck_money_quota = LuckMoney.objects.get(pk=pk).luckmoneyquota_set.all()

    return render(request, 'quota.html',locals())