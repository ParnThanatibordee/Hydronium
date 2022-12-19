# Hydronium

## List of team members
1. Thanatibordee Sihaboonthong 6310545299
2. Noppharut Kongsakdinasarn 6310546376
3. Bhokin Watanapitak 6310546392  
Kasetsart University, Faculty of Engineering, Department of Software and Knowledge Engineering 

## About The Project

The objective of the project is to track the plant's water consumption to study the behavior of the potted plants we want to monitor by plug the moisture sensor into the soil. We collect a status of rain, humidity in soil, light, CO2, so we can find the rate of water consumption of the rain and tell what time we should water the plants again. 

## Features
1. Calculate the water consumption of potted plants.
2. Displays sensor data (Primary and Secondary Data) over time.
3. Tell users when to water the plants again.

## Getting Started

### Prerequisites

| Name | Version |
|------|---------|
| DBUtils | 3.0.2 or any version |
| PyMySQL | 1.0.2 or any version |
| flask_cors | 3.0.10 or any version |
| connexion | >= 2.6.0 |
| connexion[swagger-ui] | >= 2.6.0 |
| python_dateutil | >= 2.6.0 |
| setuptools | >= 21.0.0 |
| swagger-ui-bundle | >= 0.0.2 |
| python | 3.10.8 or any version |

### Installation
1. Clone this repository
2. Inside the project folder, create and activate a virtual environment
```
python -m venv env
. env/bin/activate          # macOS and Linux
env\Scripts\activate    # Windows
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
- Optionally test the API at http://localhost:8080/hydro/v1/ui

3. Start openapi-to-graphql in another terminal with CORS (Cross-Origin Resource Sharing) enabled
```
openapi-to-graphql --cors -u http://localhost:8080/hydro/v1 openapi/hydronium-api.yaml
```
- Open the page http://localhost:3000/graphql

4. Open the file html/index.html with your web browser


## References 
[10-visual](https://drive.google.com/file/d/1-hcvErypZvDCqL4tIDZYygWmtYvk6HU7/view)  
[ResearchGate](https://www.researchgate.net/post/How-can-I-convert-Satellite-Soil-Moisture-data-m3-m3-into-mm)  
[QuickDatabaseDiagrams](https://app.quickdatabasediagrams.com/#/d/JN17kg)
