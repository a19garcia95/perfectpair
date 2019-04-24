from django.db.models import Q
from .models import Shoe
from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.


def shoe_list(request):

	shoe_list = Shoe.objects.all()

	context = {

		'shoe_list': shoe_list,
	}

	return render(request, 'shoe/shoe_list.html', context)


def liked_list(request):


	shoe_list = Shoe.objects.all()

	context = {

		'shoe_list': shoe_list,
	}

	return render(request, 'shoe/liked_list.html', context)


def cart_list(request):

	return render(request, 'shoe/cart_list.html', {})



def gender_male(request):


	shoe_list = Shoe.objects.all()

	context = {

		'shoe_list': shoe_list,
	}

	return render(request, 'shoe/gender_male.html', context)


def gender_female(request):


	shoe_list = Shoe.objects.all()

	context = {

		'shoe_list': shoe_list,
	}

	return render(request, 'shoe/gender_female.html', context)


def search(request):
	
	q = request.GET.get('q')
	
	if q:
		products = Shoe.objects.filter(name__icontains=q)
		context = {'query': q, 'products': products}
		template = 'shoe/gender_male.html'

	elif q == '':
		template = 'home.html'
		context = {}
	else:
		template = 'home.html'
		context = {}
	return render(request, template, context)

def add_to_cart(request, shoe_id):
	shoe = get_object_or_404(Shoe, pk=shoe_id)

	context = {"shoe":shoe}

	

	return render(request, template, context)






































