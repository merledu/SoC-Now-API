# SoC-Now API

This repo contains the Flask REST API for the SoC or Component Generation API calls on SoC-Now Generator

## How to Use:

Prerequisites:
```ruby
pip install flask
pip install flask_restful
```

Run the API Server
```ruby
python main.py
```


## How to Send API Requests

Sample Put Request for sending SoC Configs.
```bash
http://127.0.0.1:5000/soc/3?coreISA=64&coreExt=['i','m','f']&devices=['gpio', 'spi', 'uart']&bus=wb
```

Sample Get Request
```bash
http://127.0.0.1:5000/soc/3
```
