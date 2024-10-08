from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import SimpleTestCase, override_settings
from django.urls import path

def response_error_handler(request, exception=None):
    return HttpResponse("Error handler content", status=403)

def permission_denied_view(request):
    raise PermissionDenied

urlpatterns = [
    path("403/", permission_denied_view),
]

handler403 = response_error_handler

@override_settings(ROOT_URLCONF=__name__)
class CustomErrorHandlerTests(SimpleTestCase):
    def test_handler_renders_template_response(self):
        response = self.client.get("/403/")
        # Assert that the response contains the custom error handler content
        self.assertContains(response, "Error handler content", status_code=403)
