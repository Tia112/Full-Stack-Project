from django import forms
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField

PAYMENT_TYPEs = (("S", "Stripe"),)


class CheckoutForm(forms.Form):
    """
    Checkout form for placing Order
    """
    street_address1 = forms.CharField(required=False)
    street_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label="(select country)").formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            "class": "custom-select d-block w-100",
        }))
    post_code = forms.CharField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_TYPEs)


class PaymentForm(forms.Form):
    """
    Payment form for making the payment
    """
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)
