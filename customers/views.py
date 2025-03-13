from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from .forms import CustomerForm
from .models import Customer

# Create your views here.
@require_http_methods(['GET'])
def index(request):
    customers = Customer.objects.all()
    return render(request, 'customers/index.html', {'customers': customers})


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == 'GET':
        form = CustomerForm(instance=customer)
        return render(request, 'customers/update.html', {'customer': customer, 'form': form})

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('customers:update', kwargs={'pk': pk}))
        return render(request, 'customers/update.html', {'customer': customer, 'form': form})
