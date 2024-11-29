from plaid.api import plaid_api
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.products import Products
from flask import Blueprint

import plaid
import json
import config

plaid_blueprint = Blueprint('plaid', __name__)

configuration = plaid.Configuration(
  host=plaid.Environment.Sandbox,
  api_key={
    'clientId': config.PLAID_CLIENT_ID,
    'secret': config.PLAID_SECRET
  }
)
api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

@plaid_blueprint.route('/get_access_token', methods=['GET'])
def get_access_token():
  FIRST_PLATYPUS_BANK = 'ins_109508'
  pt_request = SandboxPublicTokenCreateRequest(
    institution_id = FIRST_PLATYPUS_BANK,
    initial_products = [Products('transactions')]
  )
  pt_response = client.sandbox_public_token_create(pt_request)
  public_token = pt_response["public_token"]

  exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token)
  exchange_response = client.item_public_token_exchange(exchange_request)
  json_string = json.dumps(exchange_response.to_dict(), default=str)
  return json_string