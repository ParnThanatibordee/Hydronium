# Hydronium

## About The Project

The objective of the project is to track the plant's water consumption to study the behavior of the potted plants we want to monitor by plug the moisture sensor into the soil. We collect a status of rain, humidity in soil, light, CO2, so we can find the rate of water consumption of the rain and tell what time we should water the plants again. 

## Getting Started

### Prerequisites

| Name | Version |
|------|---------|
| DBUtils | any version |
| PyMySQL | any version |

### Installation
1. Clone this repository
2. Inside the project folder, create and activate a virtual environment
```
python3 -m venv env
. env/bin/activate          # macOS and Linux
env\Scripts\activate.bat    # Windows
```
3. Install required libraries
```
pip install -r requirements.txt
```

### Starting Server & Opening Index Page
1. Create config.py from config.py.example
```
OPENAPI_STUB_DIR = 'stub'
DB_HOST = <database hostname or ip address>
DB_USER = <database user>
DB_PASSWD = <database password>
DB_NAME = <database name>
```
2. Start the REST API server
```
python app.py
```
- Optionally test the API at http://localhost:8080/hydro/v1

3. Start openapi-to-graphql in another terminal with CORS (Cross-Origin Resource Sharing) enabled
```
openapi-to-graphql openapi/hydronium-api.yaml
```
- Open the page http://localhost:3000/graphql

4. Open the file html/index.html with your web browser


## References 
[10-visual](https://drive.google.com/file/d/1-hcvErypZvDCqL4tIDZYygWmtYvk6HU7/view)
