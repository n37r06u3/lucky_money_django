from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from lucky_money.models import LuckMoney, LuckMoneyQuota
from decimal import Decimal, getcontext
from lucky_money.libs import money_random
def home(request):
    luck_money = LuckMoney.objects.all()
    return render(request, 'home.html', locals())


def generate_all(request, pk):
    LuckMoney.objects.get(pk=pk)
    return HttpResponse("成功")


def generate(request):
    if request.method == "POST":
        total_amount = Decimal(request.POST['total_amount'])
        quantity = int(request.POST['quantity'])
        one_amount = Decimal(request.POST['one_amount'])
        min_amount = Decimal(0.01)
        print(getcontext())
        print(one_amount)
        print(total_amount - min_amount * (quantity - 1))
        if one_amount >= total_amount:
            return HttpResponse("不能超出红包或等于总金额")
        elif one_amount > total_amount - min_amount * (quantity - 1):

            return HttpResponse("剩余红包不够分配")

        luck_money = LuckMoney.objects.create(total_amount=total_amount, quantity=quantity)
        luck_money.luckmoneyquota_set.create(amount=one_amount)
        num = quantity - 1
        total = total_amount - one_amount
        print('随机分配')
        print(total)
        print(num)
        quotas = money_random(int(total), int(num),float(min_amount))
        print(quotas)
        print(sum(quotas))
        for i in quotas:

            luck_money.luckmoneyquota_set.create(amount=i)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def generate_one(request, pk):
    luck_money = LuckMoney.objects.get(pk=pk)
    if request.method == "POST":
        amount = request.POST['amount']
        print(amount)
        if luck_money.quota_count >= 1:
            return HttpResponse("已经存在红包1")
        if int(amount) >= luck_money.total_amount:
            return HttpResponse("不能超出红包或等于总金额")
        else:
            luck_money.luckmoneyquota_set.create(amount=amount)
            return HttpResponse("成功")


def quota(request, pk):
    lm = LuckMoney.objects.get(pk=pk)
    luck_money_quota = LuckMoney.objects.get(pk=pk).luckmoneyquota_set.all()

    return render(request, 'quota.html', locals())


def receive(request, pk):
    lmq = LuckMoneyQuota.objects.get(pk=pk)
    lmq.is_received = True
    lmq.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
