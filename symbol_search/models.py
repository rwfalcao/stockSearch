from django.db import models


class Stock(models.Model):

    symbol = models.CharField(
        'Symbol',
        max_length=10,
        null=False
        )

    name = models.CharField(
        'Description',
        max_length=200,
        null=False
        )

    last_sale = models.DecimalField(
        'Last sale value',
        max_digits=12, 
        decimal_places=2
        )

    market_cap = models.DecimalField(
        'Market Cap',
        max_digits=12, 
        decimal_places=2
        )

    ipo_year = models.IntegerField(
        'IPO Year',
        )

    nasdaq_url = models.URLField()

