from .urls import urlpatterns as base_urlpatterns
from .api import urlpatterns as api_urlpatterns

urlpatterns = []
urlpatterns += base_urlpatterns
urlpatterns += api_urlpatterns
