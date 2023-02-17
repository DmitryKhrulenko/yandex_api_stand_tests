import configuration
import requests
import data

def post_products_kits(product_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,  # подставялем полный url
                         json=product_ids)

response = post_products_kits(data.product_ids);
print(response.status_code)
print(response.json())


