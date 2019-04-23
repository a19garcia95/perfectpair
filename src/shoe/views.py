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


