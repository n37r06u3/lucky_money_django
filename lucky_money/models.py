from django.db import models
from django.db.models import Sum


class LuckMoney(models.Model):
    total_amount = models.DecimalField(decimal_places=2, max_digits=6)
    quantity = models.IntegerField()
    @property
    def quota_count(self):
        return self.luckmoneyquota_set.count()

    @property
    def amount_sum(self):
        return self.luckmoneyquota_set.aggregate(Sum('amount'))

    @property
    def amount_rest(self):
        return self.total_amount - self.luckmoneyquota_set.aggregate(Sum('amount'))['amount__sum']



class LuckMoneyQuota(models.Model):
    luck_money_fk = models.ForeignKey(LuckMoney)
    amount = models.DecimalField(decimal_places=2,max_digits=6)
    is_used = models.BooleanField(default=False)