from itertools import product
from urllib import response
from django.db.models import F

from .models import CartItem


def cart_item_middleware(get_response):
    def middleware(request):
        session_key = request.session.session_key
        response = get_response(request)
        if session_key != request.session.session_key:
            CartItem.objects.filter(cart_key=session_key).update(
                cart_key = request.session.session_key
            )
        return response
    return middleware