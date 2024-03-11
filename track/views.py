from django.shortcuts import render, redirect
from .models import food_item, consume
# Create your views here.


def home(request):
    if request.method == 'POST':
        food_name = request.POST.get("consume_food", "")
        consumed_food = food_item.objects.get(name=food_name)
        user = request.user
        Consume = consume(name=user, food=consumed_food)
        Consume.save()
        food = food_item.objects.all()
    else:
        food = food_item.objects.all()
    consumer = consume.objects.filter(name=request.user)
    return render(request, 'track/home.html', {'food': food, 'consumer': consumer})


def delete_item(request, id):
    food = consume.objects.get(id=id)
    food.delete()
    return redirect('home')
