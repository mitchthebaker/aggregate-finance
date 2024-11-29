## finance-aggregator

*old setup prior to configuring project with docker*
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

*new setup*
### Build/run via docker compose
```
# build containers
docker compose up --build

# simply run if containers are already built
docker compose up
```

### Inspect mongodb volume
```
docker volume ls
docker volume inspect mongo_data
```