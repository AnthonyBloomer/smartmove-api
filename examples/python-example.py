import requests
from urllib import quote_plus

# Get all properties

req = requests.get('http://0.0.0.0:33507/api/v1/properties')
req = req.json()

for p in req:
    print p['address']
    print p['county_name']
    print p['price']

# Get Property by ID

req = requests.get('http://0.0.0.0:33507/api/v1/properties/1')
req = req.json()

print req['id']
print req['address']
print req['price']

# Compare two counties average sale price.

req = requests.get('http://0.0.0.0:33507/api/v1/counties/compare', params={
    'county1': 'Dublin',
    'county2': 'Cork'
})

req = req.json()

for r in req:
    print 'County: %s, Average Sale Price %s' % (r['county_name'], r['average_sale_price'])

# Search example
req = requests.get('http://0.0.0.0:33507/api/v1/properties/search/' + quote_plus('Dublin City'), params={
    'sale_type': 1,
    'from_date': 2015,
    'to_date': 2015
})

req = req.json()
for r in req:
    print r['address']
    print r['price']
    print r['date_time']
