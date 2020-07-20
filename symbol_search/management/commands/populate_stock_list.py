from django.core.management.base import BaseCommand, CommandError
from symbol_search.models import Stock
import pandas as pd


class Command(BaseCommand):
    help = "Populates database with provided excel file."

    def handle(self, *args, **options):
        Stock.objects.all().delete()
        xls_path = './symbol_search/files/stocks.xlsx'
        df = pd.read_excel(xls_path)

        df['IPOyear'] = df['IPOyear'].fillna(0)

        for index, stock in enumerate(df.iterrows()):
            Stock.objects.create(
                symbol = stock[1].get('Symbol', None), 
                name = stock[1].get('Name', None), 
                last_sale = stock[1].get('LastSale', None), 
                market_cap = stock[1].get('MarketCap', None) ,
                ipo_year = int(stock[1].get('IPOyear')) if stock[1].get('IPOyear') != 0 else None , 
                nasdaq_url = stock[1].get('Summary Quote', None) 
            )
            print(index)
