from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from cart.models import Cart
from .models import Order

class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self,request,*args,**kwargs):
		return super(login_required,self).dispatch(request,*args,**kwargs)


class CartOrderMixin(object):
	def get_order(self,*args,**kwargs):
		cart=self.get_cart()
		new_order_id=self.request.session.get('order_id')
		if new_order_id is None:
			new_order=Order.objects.create(cart=cart)
			self.request.session['order_id']=new_order.id
		else:
			new_order=Order.objects.get(id=new_order_id)
		return new_order


	def get_cart(self,*args,**kwargs):
		cart_id=self.request.session.get("cart_id")
		if cart_id == None:
			return redirect("cart")
		cart=Cart.objects.get(id=cart_id)
		if cart.item.count() <= 0:
			return None
		return cart