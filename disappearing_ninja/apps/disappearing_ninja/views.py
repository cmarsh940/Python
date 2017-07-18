from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	context = {}
	image_path = '../static/ninjas/image/tmnt.png'
	context['image'] = image_path
	return render(request, 'disappearing_ninja/index.html')

def ninja(request):
	context = {}
	image_path = '../static/ninjas/image/tmnt.png'
	context['image'] = image_path
	return render(request, 'disappearing_ninja/ninja.html')

def ninja_color(request, color):
	image_path = '../static/ninjas/image/'
	if color == "":
		image_path += '../static/ninjas/image/tmnt.png'
	if  color == "purple":
		image_path = "../static/ninjas/image/donatello.jpg"
	elif color == "blue":
		image_path = "../static/ninjas/image/leonardo.jpg"
	elif color == "red":
		image_path = "../static/ninjas/image/raphael.jpg"
	elif color == "orange":
		image_path = "../static/ninjas/image/michelangelo.jpg"
	else:
		image_path += '../static/ninjas/image/notapril.jpg'

	context= {
	"image": image_path
	}
	return render(request, "/ninja", context)