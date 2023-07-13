import configuration
import requests
import data

def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                        json=order_body)

def get_track_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_BY_TRACK + str(track))
