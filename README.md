# smartmove API
A RESTful API to retrieve property price statistics in Ireland and the UK. 

This API is being built as part of my final year software project, Smartmove, a data platform that enables businesses and consumers to gain insight into the property market in Ireland and the UK. The project features a Data Warehouse, RESTful API and an in-depth [data analysis using R](https://github.com/AnthonyBloomer/smartmove-data-analysis).

[You can find the database schema, SQL procedures and other load scripts needed here.](https://github.com/AnthonyBloomer/smartmove-load-scripts)

## Installation

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python app.py
```

## Endpoints

### Charts

Get JSON data that can easily be consumed by the Google Charts API.

#### Line Chart

This endpoint returns the average sale price for each year for a given county.

```shell
curl -X GET --header 'Accept: application/json' 'http://0.0.0.0:33507/api/v1/charts/<county_name>'
```

> The above command returns JSON structured like this:

```json
{
  "cols": [
    {
      "id": "Year",
      "label": "Year",
      "type": "number"
    },
    {
      "id": "Price",
      "label": "Price",
      "type": "number"
    }
  ],
  "rows": [
    {
      "c": [
        {
          "v": 2010
        },
        {
          "v": 333401
        }
      ]
    }
  ]
}
```

##### HTTP Request

`GET http://0.0.0.0:33507/api/v1/charts/<county_name>`

##### Query Parameters

| Parameter  | Description                                  |
|------------|----------------------------------------------|                         
| county_name    | The county name.                         |
| api_key    | Your API Key.                                |

#### Pie Chart

This endpoint returns the average sale price for each county.

```shell
curl -X GET --header 'Accept: application/json' 'http://0.0.0.0:33507/api/v1/charts/counties/average-sale-price'
```

> The above command returns JSON structured like this:

```json
{
  "cols": [
    {
      "id": "County",
      "label": "County",
      "type": "string"
    },
    {
      "id": "Price",
      "label": "Price",
      "type": "number"
    }
  ],
  "rows": [
    {
      "c": [
        {
          "v": "Dublin"
        },
        {
          "v": 355355.15
        }
      ]
    }
  ]
}
```

##### HTTP Request

`http://0.0.0.0:33507/api/v1/charts/counties/average-sale-price`

##### Query Parameters

| Parameter  | Description                                  |
|------------|----------------------------------------------|                         
| county_name    | The county name.                         |
| api_key    | Your API Key.                                |


### Counties

Get property sale statistics for each county.

#### Get All Counties

This endpoint retrieves a list of county sale statistics.

```shell
curl -X GET --header 'Accept: application/json' 'http://0.0.0.0:33507/api/v1/counties/'
```

> The above command returns JSON structured like this:

```json
[
  {
    "average_sale_price": "131576.43",
    "county_name": "Carlow",
    "id": "1",
    "total_number_of_sales": "2424"
  }
]
```

##### HTTP Request

`GET http://0.0.0.0:33507/api/v1/counties/`

##### Query Parameters

| Parameter  | Description                                  |
|------------|----------------------------------------------|
| sort_by    | The sort type.                               |
| sort_order | The sort order.                              |
| api_key    | Your API key.                                |

#### Get County By ID

This endpoint retrieves a county by ID

```shell
curl -X GET --header 'Accept: application/json' 'http://0.0.0.0:33507/api/v1/counties/<id>'
```

> The above command returns JSON structured like this:

```json
{
  "average_sale_price": "100182.68",
  "county_name": "Cavan",
  "id": "2",
  "total_number_of_sales": "3842"
}
```

##### HTTP Request

`GET http://0.0.0.0:33507/api/v1/counties/<id>`

##### Query Parameters

| Parameter  | Description                                  |
|------------|----------------------------------------------|
| id         | The county Identifier.                       |
| api_key    | Your API key.                                |

#### County comparison


This endpoint compares sale statistics between two counties.

```shell
curl -X GET --header 'Accept: application/json' 'http://0.0.0.0:33507/api/v1/counties/compare?county1=<county1>&county1=<county2>'
```

> The above command returns JSON structured like this:

```json
[
  {
    "average_sale_price": "196669.81",
    "county_name": "Cork",
    "id": 6,
    "total_number_of_sales": "25367"
  },
  {
    "average_sale_price": "355355.15",
    "county_name": "Dublin",
    "id": 9,
    "total_number_of_sales": "75449"
  }
]
```

##### HTTP Request

`GET http://0.0.0.0:33507/api/v1/counties/compare?county2=<county2>&county1=<county1>`

##### Query Parameters

| Parameter  | Description                                  |
|------------|----------------------------------------------|
| api_key    | Your API key.                                |
| county1    | The first county                             |
| county2    | The second county                            |


#### County Statistics by Year

This endpoint retrieves county sale statistics for a given county name and year.

```shell
curl -X GET --header 'Accept: application/json' 'http://0.0.0.0:33507/api/v1/counties/<county>/<year>'
```

> The above command returns JSON structured like this:

```json
[
  {
    "average_sale_price": "412000",
    "county_name": "Dublin",
    "id": "42",
    "total_number_of_sales": "14592",
    "year": "2016"
  }
]
```

##### HTTP Request

`GET http://0.0.0.0:33507/api/v1/counties/<county>/<year>`

##### Query Parameters

| Parameter  | Description                                  |
|------------|----------------------------------------------|
| api_key    | Your API key.                                |
| county   | The county name                      |
| year    | The year                           |


### Properties

Get property sales statistics.

#### Get All Properties

This endpoint retrieves all properties.

```shell
curl -X GET --header 'Accept: application/json' 'http://0.0.0.0:33507/api/v1/properties/'
```

> The above command returns JSON structured like this:

```json
[
  {
    "address": "5 Braemor Drive, Churchtown, Co.Dublin",
    "county_name": "Dublin",
    "date_time": "2010-01-01 00:00:00",
    "description": "Second-Hand Dwelling house /Apartment",
    "id": "1",
    "latitude": "53.3498",
    "longitude": "-6.26031",
    "price": "343000.00",
    "sale_type": "1"
  }
]
```

##### HTTP Request

`GET http://0.0.0.0:33507/api/v1/properties/`

##### Query Parameters

| Parameter  | Description                                  |
|------------|----------------------------------------------|
| page       | The page number.                             |
| api_key    | Your API key.                                |
| from_date  | The year to retrieve property listings from. |
| to_date    | The year to retrieve property listings to.   |
| country_id | The country ID.                              |
| sale_type  | The property sale type.                      |


#### Get Property By ID

This endpoint retrieves a property by ID

```shell
curl -X GET --header 'Accept: application/json' 'http://0.0.0.0:33507/api/v1/properties/<id>'
```

> The above command returns JSON structured like this:

```json
{
  "address": "5 Braemor Drive, Churchtown, Co.Dublin",
  "county_name": "Dublin",
  "date_time": "2010-01-01 00:00:00",
  "description": "Second-Hand Dwelling house /Apartment",
  "id": "1",
  "latitude": "53.3498",
  "longitude": "-6.26031",
  "price": "343000.00",
  "sale_type": "1"
}
```

###### HTTP Request

`GET http://0.0.0.0:33507/api/v1/properties/<id>`

###### Query Parameters

| Parameter  | Description                                  |
|------------|----------------------------------------------|
| id         | The Property Identifier.                     |
| api_key    | Your API key.                                |


#### Search Properties

This endpoint retrieves property listings for the given search query.

```shell
curl -X GET --header 'Accept: application/json' 'http://0.0.0.0:33507/api/v1/properties/search/<search_term>'
```

> The above command returns JSON structured like this:

```json
[
  {
    "address": "5 Braemor Drive, Churchtown, Co.Dublin",
    "county_name": "Dublin",
    "date_time": "2010-01-01 00:00:00",
    "description": "Second-Hand Dwelling house /Apartment",
    "id": "1",
    "latitude": "53.3498",
    "longitude": "-6.26031",
    "price": "343000.00",
    "sale_type": "1"
  },
  {
    "address": "1 Meadow Avenue, Dundrum, Dublin 14",
    "county_name": "Dublin",
    "date_time": "2010-01-04 00:00:00",
    "description": "Second-Hand Dwelling house /Apartment",
    "id": "3",
    "latitude": "53.3498",
    "longitude": "-6.26031",
    "price": "438500.00",
    "sale_type": "1"
  }
]
```

##### HTTP Request

`GET http://0.0.0.0:33507/api/v1/properties/search/<search_term>`

##### Query Parameters

| Parameter  | Description                                  |
|------------|----------------------------------------------|
| page       | The page number.                             |
| api_key    | Your API key.                                |
| from_date  | The year to retrieve property listings from. |
| to_date    | The year to retrieve property listings to.   |
| country_id | The country ID.                              |
| sale_type  | The property sale type.                      |
| search_term | The search query                            |


## Examples

You can find some JavaScript and Python examples in the [examples](https://github.com/AnthonyBloomer/smartmove-api/tree/master/examples) folder.

## Rate Limits

The Smartmove API includes rate limiting. The API allows 2,000 requests per day and 100 requests per hour.

## Online Demo

Currently migrating from local machine to Heroku and right now is incomplete   
No API key is required to run the API methods.

[View on Heroku](https://smartmove-api.herokuapp.com)
