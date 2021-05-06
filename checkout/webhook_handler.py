from django.http import HttpResponse


class StripeWH_Handler:
    """ Controls Stripe Webhook instances """

    def __init__(self, request):
        self.request = request

    def control_event(self, event):
        """ Controls a genetic/unknown/unexpected webhook event """

        return HttpResponse(
            content=f'webhook received: {event["type"]}',
            status=200)

    def control_payment_intent_success(self, event):
        """
        Handle the payment_intent.success webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def control_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
           