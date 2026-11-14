from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now


class SessionCheckRequests(MiddlewareMixin):
    SESSION_KEY = 'limit_logs'
    seconds = 60
    max_requests = 10

    def process_request(self, request):
        current_time = now().timestamp()
        start = current_time - self.seconds

        recent_requests = [
            crrnt_time for crrnt_time in request.session.get('SESSION_KEY', [])
            if crrnt_time > start
        ]

        if len(recent_requests) > self.max_requests:
            return HttpResponse('No more tries for the next 60s', status=429)

        recent_requests.append(current_time)
        request.session[self.SESSION_KEY] = recent_requests


        