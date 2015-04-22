from django.conf import settings

import keen
import logging


def keen_hit(type, resource, request):
    if not settings.KEEN_DEBUG:
        ip = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')
        try:
            keen.add_event(
                "api_hit".format(resource),
                {
                    "url": request.path,
                    "type": "{0}".format(type),
                    "resource": resource,
                    "ip_address": ip,
                    "user_agent": user_agent
                }
            )
        except:
            logging.warning("Couldn't send event to keen")
            pass
