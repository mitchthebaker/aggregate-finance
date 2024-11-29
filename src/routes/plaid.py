from plaid.api import plaid_api
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.transactions_sync_request import TransactionsSyncRequest
from plaid.model.products import Products
from flask import Blueprint
from extensions import cache

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

@plaid_blueprint.route('/set_access_token', methods=['POST'])
# add uri parameter for custom institution id, initial products
def set_access_token():
  FIRST_PLATYPUS_BANK = 'ins_109508'
  pt_request = SandboxPublicTokenCreateRequest(
    institution_id = FIRST_PLATYPUS_BANK,
    initial_products = [Products('transactions')]
  )
  pt_response = client.sandbox_public_token_create(pt_request)
  public_token = pt_response["public_token"]

  exchange_request = ItemPublicTokenExchangeRequest(public_token=public_token)
  exchange_response = client.item_public_token_exchange(exchange_request)

  cache.set('plaid_access_token', exchange_response.access_token)
  json_string = json.dumps(exchange_response.to_dict(), default=str)
  return json_string

@plaid_blueprint.route('/set_transaction_sync', methods=['POST'])
def set_transaction_sync():
  #cursor = cache.get('cursor')
  cursor = ''

  # New transaction updates since "cursor"
  added = []
  modified = []
  removed = [] # Removed transaction ids
  has_more = True

  # Iterate through each page of new transaction updates for item
  while has_more:
    request = TransactionsSyncRequest(
      access_token=cache.get('plaid_access_token'),
      cursor=cursor,
    )
    response = client.transactions_sync(request)

    # Add this page of results
    added.extend(response['added'])
    modified.extend(response['modified'])
    removed.extend(response['removed'])

    has_more = response['has_more']

    # Update cursor to the next cursor
    cursor = response['next_cursor']

  pages = {
    'cursor': cursor,
    'added': added,
    'modified': modified,
    'removed': removed,
  }
  cache.set('pages', pages)
  json_string = json.dumps(response.to_dict(), default=str)
  return json_string
