from sslcommerz_lib import SSLCOMMERZ
from django.conf import settings

def sslcommerz_payment_gateway(request, cart_total):

    settings = {'store_id': 'Your Store Id',
                'store_pass': 'Your Store pass@ssl', 'issandbox': True}
    sslcommez = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = cart_total
    post_body['currency'] = "BDT"
    post_body['tran_id'] = "aofhoaiao"
    post_body['success_url'] = 'http://127.0.0.1:8000/'
    post_body['fail_url'] = 'http://127.0.0.1:8000/'
    post_body['cancel_url'] = 'http://127.0.0.1:8000/'
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

    response = sslcommez.createSession(post_body)
    return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]