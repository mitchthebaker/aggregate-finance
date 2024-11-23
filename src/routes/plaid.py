import plaid
from plaid.api import plaid_api

import config

configuration = plaid.Configuration(
  host=plaid.Environment[config.PLAID_HOST]
  api_key={
    'clientId': config.PLAID_CLIENT_ID
    'secret': config.PLAID_SECRET
  }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)