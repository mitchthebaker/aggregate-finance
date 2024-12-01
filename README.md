## finance-aggregator
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
You'll log in using admin/pass as credentials, but please change these to something more secure.