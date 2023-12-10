from django.db import models

class StockMarketData(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=10)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()

    def __str__(self):
        return f"{self.date} - {self.trade_code}"
