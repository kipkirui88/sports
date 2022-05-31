
from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data
from django.views.generic import ListView


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('predictions')
    else:
        form = DataForm()
    context = {
        'form': form,
    }      
    return render(request, 'index.html', context)      

class predictions(ListView):
    model = Data
    context_object_name = 'predicted_sports'
    template_name = 'predictions.html'