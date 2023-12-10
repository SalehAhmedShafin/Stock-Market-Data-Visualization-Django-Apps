from django.http import JsonResponse
from django.shortcuts import render
from .models import StockMarketData

def view_table(request):
    data = StockMarketData.objects.all()
    return render(request, 'table_apps.html', {'data': data,})

def graph_view(request):
    
    data = StockMarketData.objects.all()
    trade_codes = StockMarketData.objects.values_list('trade_code', flat=True).distinct()
    return render(request, 'graphs.html',{ 'data': data, 'trade_codes': trade_codes, })
    
def stock_data_api(request):
    if request.method == 'GET':
        trade_code = request.GET.get('trade_code', '')
        data = StockMarketData.objects.filter(trade_code=trade_code).order_by('date')
        dates = [str(item.date) for item in data]
        close_prices = [float(item.close) for item in data]
        volumes = [item.volume for item in data]
        return JsonResponse({'dates': dates, 'close_prices': close_prices, 'volumes': volumes})
    else:
        return JsonResponse({'error': 'Invalid request method'})