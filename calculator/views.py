from django.shortcuts import render
from .models import Consumer
from calculator_python import calculator

def view1(request):
    if request.method == "POST":
        consumo = request.POST.get('consumo',[])
        taxa = float(request.POST.get('taxa', 0))
        tipo_tarifa = request.POST.get('tipo_tarifa', '')

        consumers = Consumer.objects.all()

        for consumer in consumers:
            annual_savings, monthly_savings, applied_discount, coverage = calculator([consumo], taxa, tipo_tarifa)
            
            consumer.annual_savings = annual_savings
            consumer.monthly_savings = monthly_savings
            consumer.applied_discount = applied_discount
            consumer.coverage = coverage
            
            consumer.save()

        context = {'consumers': consumers}
        return render(request, 'calculator/list.html', context)
    else:
        return render(request, 'calculator/list.html', {})


# TODO: Your create view should do the following tasks
"""Create a view to perform inclusion of consumers. The view should do:
-> Receive a POST request with the data to register
-> If the data is valid (validate document), create and save a new Consumer object associated with the right discount rule object
-> Redirect to the template that list all consumers

Your view must be associated with an url and a template different from the first one. A link to
this page must be provided in the main page.
"""


def view2():
    if request.method == "POST":
        consumo = request.POST.get('consumo',[])
        taxa = float(request.POST.get('taxa', 0))
        tipo_tarifa = request.POST.get('tipo_tarifa', '')

        consumers = Consumer.objects.all()

        for consumer in consumers:
            annual_savings, monthly_savings, applied_discount, coverage = calculator([consumo], taxa, tipo_tarifa)
            
            consumer.annual_savings = annual_savings
            consumer.monthly_savings = monthly_savings
            consumer.applied_discount = applied_discount
            consumer.coverage = coverage
            
            consumer.save()

        context = {'consumers': consumers}
        return render(request, 'calculator/list.html', context)
    else:
        return render(request, 'calculator/list.html', {})
    pass

