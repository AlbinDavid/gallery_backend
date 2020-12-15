

from django.urls import path
from gallery import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path("test/",views.test_api),
            path("upload_image/",views.upload_files),
            path("get_images/",views.get_images)]
