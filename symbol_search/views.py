from django.shortcuts import render
from django.http import HttpResponse
from symbol_search.models import Stock
from django.core.paginator import Paginator



def index(request):
    stocks = Stock.objects.all()
    paginator = Paginator(stocks, 10)
    current_page = request.GET.get('page')
    page_obj = paginator.get_page(current_page)

    context = {
        'stocks': stocks,
        'current_page': int(current_page),
        'page': page_obj,
        'page_range': range(1, page_obj.paginator.num_pages)
    }

    return render(request, 'symbol_list.html', context)