from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings

import authentication.views
import website.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.LoginPageView.as_view(), name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('flux/', website.views.flux_page, name='flux-page'),
    path('create_ticket/add/', website.views.create_ticket, name='create_ticket'),
    path('view_ticket/<int:ticket_id>/', website.views.view_ticket, name='view_ticket'),
    path('update_ticket/<int:ticket_id>/update/', website.views.update_ticket, name='update_ticket'),
    path('create_review/add/', website.views.create_review, name='create_review'),
    path('create_review_from_ticket/<int:ticket_id>/', website.views.create_review_from_ticket, name='create_review_from_ticket'),
    path('update_review/<int:review_id>/', website.views.update_review, name='update_review'),
    path('follow_users/', website.views.follow_users, name='follow_users'),
    path('delete_follow_users/<int:user_id>/', website.views.delete_follow_users, name='delete_follow_users'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )