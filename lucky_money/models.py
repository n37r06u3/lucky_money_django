from django.db import models
from django.db.models import Sum


class LuckMoney(models.Model):
    total_amount = models.DecimalField(decimal_places=2, max_digits=6)
    quantity = models.IntegerField()
    @property
    def quota_count(self):
        return self.luckmoneyquota_set.count()
    @property
    def receive_count(self):
        return self.luckmoneyquota_set.filter(is_received=True).count()

    @property
    def amount_sum(self):
        return self.luckmoneyquota_set.aggregate(Sum('amount'))
    @property
    def receive_sum(self):
        aggr_sum = self.luckmoneyquota_set.filter(is_received=True).aggregate(Sum('amount'))['amount__sum']
        if aggr_sum:
            return aggr_sum
        return 0

    @property
    def amount_rest(self):
        aggr_sum = self.luckmoneyquota_set.aggregate(Sum('amount'))['amount__sum']
        if aggr_sum:
            return self.total_amount - self.luckmoneyquota_set.aggregate(Sum('amount'))['amount__sum']
        else:
            return self.total_amount



class LuckMoneyQuota(models.Model):
    luck_money_fk = models.ForeignKey(LuckMoney)
    amount = models.DecimalField(decimal_places=2,max_digits=6)
    is_received = models.BooleanField(default=False)