from django.http import HttpResponse


class StripeWH_control:
    """ Controls Stripe Webhook instances """

    def __init__(self, request):
        self.request = request

    def control_event(self, event):
        """ Controls a genetic/unknown/unexpected webhook event """

        return HttpResponse(
            content=f'webhook received: {event["type"]}',
            status=200)
           