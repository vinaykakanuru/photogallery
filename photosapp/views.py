from django.shortcuts import render, redirect
from photosapp.models import Category, Photo

# Create your views here.


def home(request):
    category = request.GET.get('category')

    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name__icontains=category)

    categories = Category.objects.all()
    return render(request, 'photosapp/home.html', {'categories': categories, 'photos': photos})


def view_photo(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photosapp/photo.html', {'photo': photo})


def add_photo(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        # image = request.FILES.get('image') # for single image upload from template
        images = request.FILES.getlist('images')

        print('data', data)
        print('images', images)
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != "":
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        for image in images:
            Photo.objects.create(
                category=category, description=data['description'], image=image)

        return redirect('home')

    return render(request, 'photosapp/add.html', {'categories': categories})
