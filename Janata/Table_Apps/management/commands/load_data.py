import csv
from decimal import Decimal
from django.core.management.base import BaseCommand
from Table_Apps.models import StockMarketData

class Command(BaseCommand):
    help = 'Load data from CSV file into the database'

    def handle(self, *args, **kwargs):
        with open('C:\\Users\\Saleh Ahmed Shafin\\Webapps\\Data\\stock_market_data.csv', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                
                row['date'] = row['date']
                row['high'] = Decimal(row['high'].replace(',', ''))
                row['low'] = Decimal(row['low'].replace(',', ''))
                row['open'] = Decimal(row['open'].replace(',', ''))
                row['close'] = Decimal(row['close'].replace(',', ''))
                row['volume'] = int(row['volume'].replace(',', ''))
                
                
                StockMarketData.objects.create(**row)