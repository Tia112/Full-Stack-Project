from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from .models import Order


class OrderSummaryView(LoginRequiredMixin, View):
    """
    Class to render Order Summary Page
    """

    def get(self, *args, **kwargs):
        """
        :return: Order summary page with all relevant details like Cart
        """
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                "object": order
            }
            return render(self.request, "order_summary.html", context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")


def OrderHistory(request):
    """
    :param request: GET
    :return: Renders the all the previous orders done by the current user.
    """
    orders = Order.objects.filter(user=request.user)
    return render(request, "order_history.html", {"orders": orders})


def send_confirmation(email):
    """
    Utility function to send email after order is placed.
    :param email: User Email
    :return: None
    """
    context = {}
    txt_ = get_template("confirmed.txt").render(context)
    html_ = get_template("confirmed.html").render(context)
    subject = "Your Order was Successfull!!"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    sent_mail = send_mail(
        subject,
        txt_,
        from_email,
        recipient_list,
        html_message=html_,
        fail_silently=False,
    )
    return sent_mail


def OrderConfirm(request, orderid):
    """
    :param request: GET
    :param orderid: Order ID of current placed order
    :return: Renders confirmation page after mailing the current user.
    """
    orders = Order.objects.filter(orderid=orderid).first()
    email = orders.user.email
    send_confirmation(email=email)

    return render(request, "order_confirmed.html", {"order": orders})
