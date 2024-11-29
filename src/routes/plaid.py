import plaid
from plaid.api import plaid_api
from flask import Blueprint, jsonify, request

import config

plaid_blueprint = Blueprint('plaid', __name__)

configuration = plaid.Configuration(
  host=config.PLAID_HOST,
  api_key={
    'clientId': config.PLAID_CLIENT_ID,
    'secret': config.PLAID_SECRET
  }
)
api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

@plaid_blueprint.route('/get_public_token', methods=['GET'])
def get_public_token():
  print("in get public token")
  FIRST_PLATYPUS_BANK = 'ins_109508'
  pt_request = SandboxPublicTokenCreateRequest(
    institution_id = FIRST_PLATYPUS_BANK,
    initial_products = [Products('transactions')]
  )
  pt_response = client.sandbox_public_token_create(pt_request)
  # The generated public_token can now be
  # exchanged for an access_token
  exchange_request = ItemPublicTokenExchangeRequest(
      public_token=pt_response['public_token']
  )
  exchange_response = client.item_public_token_exchange(exchange_request)
  return exchange_response