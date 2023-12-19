from django.urls import path, include
from .views import StatusApiView , StatusDetailApiView

                    #StatusListSearchApiView, 
                    
                    # StatusCreateApiView , 
#                    StatusRetrieveApiView,
                    # StatusUpdateApiView,
                    # StatusDeleteApiView,
                  # )

urlpatterns = [
   # path('get_status/list/', StatusListSearchApiView.as_view()),
    path('get_status/list/', StatusApiView.as_view()),
  #  path('create/', StatusCreateApiView.as_view()),
    path('get_status/list/<int:pk>/', StatusDetailApiView.as_view()),
   # path('get_status/<int:pk>/update/', StatusUpdateApiView.as_view()),
   # path('get_status/<int:pk>/delete/', StatusDeleteApiView.as_view()),
]


# /api/get_status/list/  -- all statuses
# /api/create/ -- create a new status
# /api/get_status/2/ -- get info of specific story/status
# /api/get_status/1/update/ -- update specific status 
# /api/get_status/1/delete/ -- delete specific status