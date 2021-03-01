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
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")


def OrderHistory(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_history.html', {'orders': orders})

def send_confirmation(email):
    context = {}
    txt_ = get_template("confirmed.txt").render(context)
    html_ = get_template("confirmed.html").render(context)
    subject = 'Your Order was Successfull!!'
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
    orders = Order.objects.filter(orderid=orderid).first()
    email = orders.user.email
    send_confirmation(email=email)

    return render(request, 'order_confirmed.html', {'order': orders})