from django.urls import path
from .views import PicsListView, PicsDetailView, PicsCreateView, PicsUpdateView, PicsDeleteView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', PicsListView.as_view(), name='blog-home'),
    path('pics/<int:pk>/', PicsDetailView.as_view(), name='post-detail'),
    path('pics/new/', PicsCreateView.as_view(), name='post-create'),
    path('pics/<int:pk>/update/', PicsUpdateView.as_view(), name='pics-update'),
    path('pics/<int:pk>/delete/', PicsDeleteView.as_view(), name='pics-delete'),
    path('about/', views.about, name='blog-about'),
    path('search/', views.search_results, name = 'search_results'),
    path('pics/<int:pics_id>', views.pics, name = 'news'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
