## aggregate-finance
The idea here is to pull from various APIs (Bank of America, American Express, etc) to gather various payment details, which can then be auto populated into a spreadsheet for easier personal finance management.

### Build/run via docker compose
```
# build containers
docker compose up --build

# or run if containers are already built
docker compose up
```

### Inspect mongodb volume
```
docker volume ls
docker volume inspect mongo_data
```

### View swagger API documentation
http://0.0.0.0:3101/apidocs/

### View MongoDB Express admin interface
http://0.0.0.0:8081/

By default, the MongoDB Express URI is: mongodb://admin:pass@localhost:27017/db?ssl=false.
You'll log in using admin/pass as credentials, but change these to something more secure.

## Setup Google Sheets API integration
You'll need to create a GCP project along with a service account to query data from the Google Sheets API.

https://developers.google.com/sheets/api/guides/concepts
https://developers.google.com/workspace/guides/create-project
https://support.google.com/a/answer/7378726?hl=en

After you've created a service account, download the service account's private key JSON file to the /flask-api directory in this project locally.

For the spreadsheet you're querying you'll have to share access with the service account client email.