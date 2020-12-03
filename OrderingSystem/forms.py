from django import forms
from django.core.exceptions import ValidationError


class TestForm(forms.Form):
    test_field = forms.IntegerField(label="Enter number")
    check = forms.BooleanField(required=False)

    def clean_return(self):
        data = self.cleaned_data['test_field']
        return data


class ItemRequestForm(forms.Form):
    item_quantity = forms.IntegerField(label="Qty:", max_value=20)
    add_to_order = forms.IntegerField(label="Add to Order #:")

    def clean_return(self):
        data = self.cleaned_data['item_quantity']
        return data

    def clean_order(self):
        data = self.cleaned_data['add_to_order']
        return data


class NewOrderForm(forms.Form):
    new_order_num = forms.IntegerField(label="New Order Number: ")

    def clean_return(self):
        data = self.cleaned_data['new_order_num']
        return data


class SearchBoxForm(forms.Form):
    search_field = forms.CharField(label="Search:")

    def clean_return(self):
        data = self.cleaned_data['search_field']
        return data


CATEGORY_CHOICES = (
    ("Appetizers", "Appetizers"),
    ("Desserts", "Desserts"),
    ("Drinks", "Drinks"),
    ("Main Dishes", "Main Dishes"),
)


class CategoryForm(forms.Form):
    category_choice = forms.ChoiceField(label="Display Category", choices=CATEGORY_CHOICES)

    def clean_return(self):
        data = self.cleaned_data['category_choice']
        return data


class PaymentForm(forms.Form):
    payment_order = forms.IntegerField(label="Verify Order Number", required=True)
    payment_send = forms.BooleanField(label="Send Payment?", required=True)

    def clean_return(self):
        data = self.cleaned_data['payment_order']
        return data
