from django.shortcuts import render
from gallery.models import Images
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from .forms import NameForm
# Create your views here.
from django.conf import settings

@csrf_exempt
def upload_files(request):
    try:
        if request.method == 'POST':
            upload_obj = Images(category=request.POST["title"],image=request.FILES["image"])
            upload_obj.save()
            return HttpResponse('successfully uploaded')
        else:
            return HttpResponse("Unsuccessfull")
    except Exception as e:
        print(str(e))
        return HttpResponse("Exception "+str(e))
@csrf_exempt
def get_images(request):
    try:
        if request.method == 'POST':
            category = request.POST['category']
            print(category)
            if category !="All Categories":
                categorized_objs = Images.objects.filter(category=category)
            elif category=="All Categories":
                categorized_objs = Images.objects.all()
            print(categorized_objs)
            data = list(categorized_objs.values())
            print(data)
            return JsonResponse({"data":data})
    except Exception as e:
        print(str(e))
        return HttpResponse("Not working"+str(e))
@csrf_exempt
def test_api(request):
    print(settings.MEDIA_ROOT)
    obj = Images.objects.all()
    print(list(obj.values()))
    return HttpResponse("test_working")

