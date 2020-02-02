from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='index-home'),
    path('login/', views.user_login, name='user-auth'),
    path('home/', views.user_home, name='user-home'),
    path('claim_age/', views.claim_age, name='claim-age'),
    path('claim_address/', views.claim_address, name='claim-address'),
    path('claim_degree/', views.claim_degree, name='claim-degree'),
    path('verify_age/<str:info>', views.verify_age, name='verify-age'),
    path('verify_address/<str:info>', views.verify_address, name='verify-address'),
    path('verify_degree/<str:info>', views.verify_degree, name='verify-degree'),
    path('add_documents/', views.add_documents, name='add-documents'),
    path('add_documents/confirm', views.add_documents_confirm, name='add-documents-confirm'),
    path('view_documents/', views.view_documents, name='view-documents'),
    path('university/', views.view_university, name='university-home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)