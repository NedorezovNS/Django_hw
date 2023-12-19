"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path, re_path
from calculator.views import recipe_with_serve, recipe_book

urlpatterns = [
    path('', recipe_book),
    re_path(r'.', recipe_with_serve),
    path('omlet/', recipe_with_serve, name='omlet'),
    path('pasta/', recipe_with_serve, name='pasta'),
    path('buter/', recipe_with_serve, name='buter'),

]
