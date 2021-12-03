from django.urls import path
from django.conf.urls import url

from . import views

#Unresolved reference issue with admin.site.urls
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('emp', views.emp),
    path('show',views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]
