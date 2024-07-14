from django.shortcuts import render
#import time
from django.core.cache import cache
from .models import Dish
from .forms import SearchForm
from fuzzywuzzy import process

def search(request):
    form = SearchForm()
    results = []

    if 'query' in request.GET:
        #start_time = time.time()
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            cache_key = f'search_results_{query}'
            results = cache.get(cache_key)

            if not results:
                query = form.cleaned_data['query']
                dishes = Dish.objects.all()
                dish_names = [dish.name for dish in dishes]
                matches = process.extract(query, dish_names, limit=5)
                matched_dish_names = [match[0] for match in matches if match[1] > 50]
                results = Dish.objects.filter(name__in=matched_dish_names).order_by('-restaurant__aggregate_rating')
                cache.set(cache_key, results, 300)


            #print(f'Total time: {time.time() - start_time} seconds')
    return render(request, 'searchapp/search.html', {'form': form, 'results': results})
