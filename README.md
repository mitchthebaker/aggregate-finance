## finance-aggregator


old setup prior to trying redis for plaid access key cache
### Setup virtualenv and install dependencies

```
pip3 install virtualenv
virtualenv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

### Run development server

```
python3 src/server.py
```

new setup
### Build/run via docker compose
```
docker compose up --build

# or simply
docker compose up
```