from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import(
    ContactListView, ContactDetailView,
    ContactCreateView, ContactUpdateView, ContactDeleteView
)

urlpatterns = [
    path('', ContactListView.as_view(), name='contact-home'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('contact/new/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),
    path('cover/', views.cover, name='contact-cover'),  # For Logout template
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact-delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
