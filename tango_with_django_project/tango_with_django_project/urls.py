"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.urls import include, path
from django.contrib import admin
from rango import views
# from rango.views import index
from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/rango/'

urlpatterns = [
    path('', views.index, name='index'),
    path('rango/', include('rango.urls')),
    #以上映射将所有开头为 rango/ 的URL指向rango应用。
    path('admin/', admin.site.urls),
    #Add in this url pattern to override the default pattern in accounts.
    path('accounts/register/', MyRegistrationView.as_view(), name='registration_register'),
    path('rango/add_profile/',views.register_profile,name='register_profile'),
    path('accounts/',include('registration.backends.simple.urls')),
    ]

# 调试过程中可能遇到问题，因此在这里将调试True和False做出处理
from django.conf import settings # New Import
from django.conf.urls.static import static # New Import


if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

