import os.path

from flask import Blueprint, request, jsonify
from flasgger import swag_from
from swagger import templates
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

google_api_blueprint = Blueprint('google-api', __name__)

@google_api_blueprint.route('/spreadsheet/<spreadsheet_id>', methods = ['GET'])
@swag_from(templates)
def spreadsheet(spreadsheet_id):
  #try:
  #  creds = None
  #  # The file token.json stores the user's access and refresh tokens, and is
  #  # created automatically when the authorization flow completes for the first
  #  # time.
  #  if os.path.exists("token.json"):
  #    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  #  # If there are no (valid) credentials available, let the user log in.
  #  if not creds or not creds.valid:
  #    if creds and creds.expired and creds.refresh_token:
  #      creds.refresh(Request())
  #    else:
  #      flow = InstalledAppFlow.from_client_secrets_file(
  #          "credentials.json", SCOPES
  #      )
  #      creds = flow.run_local_server(port=0)
  #    # Save the credentials for the next run
  #    with open("token.json", "w") as token:
  #      token.write(creds.to_json())
  #except Exception as e:
  #  return jsonify({"error": f"An error occurred when creating token.json: {str(e)}"}), 500
  
  try:
    SAMPLE_RANGE_NAME = "Sheet1!A2:F2"
    creds = Credentials.from_service_account_file('credentials.json', scopes = SCOPES)
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=spreadsheet_id, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    print(result)
    values = result.get("values", [])

    if not values:
      return jsonify({"message": "No data found from Google Sheets API"}), 200

    print("Name, Major:")
    for row in values:
      # Print columns A and E, which correspond to indices 0 and 4.
      print(f"{row}")
    
    return result
  except Exception as e:
    return jsonify({"error": f"An error occurred when calling Google Sheets API: {str(e)}"}), 500
