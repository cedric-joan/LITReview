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
    path('ticket/add/', website.views.create_ticket, name='create_ticket'),
    path('ticket/<int:ticket_id>', website.views.view_ticket, name='view_ticket'),
    path('ticket/<int:ticket_id>/edit', website.views.edit_ticket, name='edit_ticket'),
    path('ticket/<int:ticket_id>/delete', website.views.delete_ticket, name='delete_ticket'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )