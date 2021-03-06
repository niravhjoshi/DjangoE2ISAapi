"""DjangoE2ISAapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
from .restconf import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^',include('persons.api.urls'),name='home'),
    url(r'^api/persons/',include('persons.api.urls'),name='HOME'),
    url(r'^api/eartypes/',include('earningtype.api.urls')),
    url(r'^api/exptypes/',include('expensetype.api.urls')),
    url(r'^api/invtypes/',include('investmtype.api.urls')),
    url(r'^api/auth/',include('accounts.api.urls')),
    url(r'^api/EarningsEntry/',include('Earnings.api.urls')),
    url(r'^api/ExpensesEntry/',include('Expenses.api.urls')),
    url(r'^api/InvestmentsEntry/',include('Investment.api.urls')),
    url(r'^api/SharesEntry/',include('Shares.api.urls')),
    # url(r'^api/Expenses/',include('Expenses.api.urls')),
    # url(r'^api/Investments/',include('Investment.api.urls')),
    # url(r'^api/Shares/',include('Shares.api.urls')),


]