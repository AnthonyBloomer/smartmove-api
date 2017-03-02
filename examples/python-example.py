import requests

# Get all properties

req = requests.get('http://0.0.0.0:33507/properties')
req = req.json()

for p in req:
    print p['address']
    print p['county_name']
    print p['price']

# Get Property by ID

req = requests.get('http://0.0.0.0:33507/properties/1')
req = req.json()

print req['id']
print req['address']
print req['price']

# Compare two counties average sale price.

req = requests.get('http://0.0.0.0:33507/counties/compare', params={
    'county1': 'Dublin',
    'county2': 'Cork'
})

req = req.json()

for r in req:
    print 'County: %s, Average Sale Price %s' % (r['county_name'], r['average_sale_price'])
