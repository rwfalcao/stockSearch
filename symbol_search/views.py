from django.shortcuts import render
from django.http import HttpResponse
from symbol_search.models import Stock
from django.core.paginator import Paginator
from django.utils.translation import activate
from django.db.models import Q



def index(request):
    activate('pt')

    stocks = Stock.objects.all()
    search_str = request.GET.get('search-string')
    if search_str:
        stocks = stocks.filter(
            Q(symbol__icontains=search_str) | 
            Q(name__icontains=search_str)
        )
    
    paginator = Paginator(stocks, 10)
    current_page = request.GET.get('page') if request.GET.get('page') else 1
    page_obj = paginator.get_page(current_page)

    context = {
        'current_page': int(current_page),
        'page': page_obj,
        'page_range': range(1, page_obj.paginator.num_pages),
        'search_str': search_str
    }

    return render(request, 'symbol_list.html', context)