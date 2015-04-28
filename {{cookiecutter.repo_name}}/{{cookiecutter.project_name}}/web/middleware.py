import logging

from django.conf import settings

logger = logging.getLogger("requests-dev")


class LogRequests(object):
    def process_request(self, request):
        format_tuple = (request.method, request.get_full_path())
        logger.debug("- %s %s" % format_tuple)


class ReadOnly(object):
    def process_request(self, request):
        if settings.READ_ONLY and self.filter(request):
            self.respond(request)

    def filter(self, request):
        return False

    def respond(self, request):
        pass
