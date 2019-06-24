from django.shortcuts import render
import numba
from django.views.decorators.cache import cache_page
# Create your views here.

# @numba.jit
@cache_page(60 * 15)
def index(request):
    return render(request, 'app/ii.html')
