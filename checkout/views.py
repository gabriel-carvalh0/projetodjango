from socket import CAN_EFF_FLAG
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404 
from django.views.generic import RedirectView

from django.forms import modelformset_factory

from django.urls import reverse

from django.contrib import messages

from catalog.models import Product
from .models import CartItem, CartItemManager


class CreateCartItemView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()
        cart_item, created = CartItem.objects.add_item(
            self.request.session.session_key, product
        )
        if created:
            messages.success(self.request, 'Produto adicionado com sucesso')
        else:
            messages.info(self.request, 'Produto atualizado com sucesso')
        return reverse('checkout:cart_item')


class CartItemView(TemplateView):

    template_name = 'checkout/cart.html'

    def get_context_data(self, **kwargs):
        context = super(CartItemView, self).get_context_data(**kwargs)
        CartItemFormSet = modelformset_factory(
            CartItem, fields=('quantity',), can_delete=True, extra=0
        )
        session_key = self.request.session.session_key
        if session_key:
            context['formset'] = CartItemFormSet(
                queryset=CartItem.objects.filter(cart_key=session_key)
            )
        else:
            context['formset'] = CartItemFormSet(queryset=CartItem.objects.none())
        return context

create_cartitem = CreateCartItemView.as_view()
cart_item = CartItemView.as_view()