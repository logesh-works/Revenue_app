from .models import AcademicSession, AcademicTerm
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """
    Middleware to redirect unauthenticated users to the login page.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is not authenticated and the requested URL is not the login page
        if not request.user.is_authenticated and not request.path == reverse('login'):
            return redirect('login')
        return self.get_response(request)
    
class SiteWideConfigs:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_session = AcademicSession.objects.get(current=True)
        current_term = AcademicTerm.objects.get(current=True)

        request.current_session = current_session
        request.current_term = current_term

        response = self.get_response(request)

        return response
