import string
import random
from django.conf import settings

from sslcommerz_lib import SSLCOMMERZ


def unique_trangection_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    return ''.join(random.choice(chars) for _ in range(size))

def sslcommerz_payment_gateway(request, cart, user):
    
    settings = {'store_id': 'Your Store ID',
                'store_pass': 'Your Store Pass', 'issandbox': True}


    # settings = {'store_id': 'graph5f0ae5eb36392',
    #         'store_pass': 'graph5f0ae5eb36392@ssl', 'issandbox': True}            
    sslcommez = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = cart.total
    post_body['currency'] = "BDT"
    post_body['tran_id'] = unique_trangection_id_generator()
    post_body['success_url'] = 'https://gainskill.herokuapp.com/payment/success/'
    post_body['fail_url'] = 'https://gainskill.herokuapp.com/payment/faild/'
    post_body['cancel_url'] = 'https://gainskill.herokuapp.com/carts/'
    post_body['emi_option'] = 0
    post_body['cus_name'] = request.data["full_name"]
    post_body['cus_email'] = request.data["email"]
    post_body['cus_phone'] = request.data["phone"]
    post_body['cus_add1'] = request.data["address"]
    post_body['cus_city'] = request.data["address"]
    post_body['cus_country'] = 'Bangladesh'
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"

    # OPTIONAL PARAMETERS
    post_body['value_a'] = user.id
    post_body['value_b'] = cart.id




    response = sslcommez.createSession(post_body)
    return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]