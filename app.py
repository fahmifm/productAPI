#app.py
import falcon
import json
from pymongo import MongoClient
from bson.json_util import dumps

#Connect DB
DB_HOST = 'localhost'
DB_PORT = 27017
client = MongoClient(DB_HOST, DB_PORT)

db = client.product
Items = db.items

# Class for API route
class Filter:
 
    def on_get(self, req, resp):

        params = req.params
        
        if params:
            # Filter by color, size, and price range
            if all (i in params for i in ('color','size','minPrice','maxPrice')):
                cursor = Items.find({ 'color' : params['color'], 'size' : params['size'], 'price' : { '$gt': int(params['minPrice']), '$lt': int(params['maxPrice']) }})
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by color, size and price less than
            elif all (i in params for i in ('color','size','maxPrice')):
                cursor = Items.find({ 'color' : params['color'], 'size': params['size'], 'price' : { '$lt': int(params['maxPrice'])}  })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by color, size and price greater than
            elif all (i in params for i in ('color','size','minPrice')):
                cursor = Items.find({ 'color' : params['color'], 'size': params['size'], 'price' : { '$gt': int(params['minPrice'])}  })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by color, size
            elif all (i in params for i in ('color','size')):
                cursor = Items.find({ 'color' : params['color'], 'size': params['size']  })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by color and price range
            elif all (i in params for i in ('color','minPrice','maxPrice')):
                cursor = Items.find({ 'color' : params['color'], 'price' : { '$lt': int(params['maxPrice']), '$gt': int(params['minPrice']) }})
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by color and price less than
            elif all (i in params for i in ('color','maxPrice')):
                cursor = Items.find({ 'color' : params['color'], 'price' : { '$lt': int(params['maxPrice']) }})
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by color and price greater than
            elif all (i in params for i in ('color','minPrice')):
                cursor = Items.find({ 'color' : params['color'], 'price' : { '$gt': int(params['minPrice'])}  })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by size and price range
            elif all (i in params for i in ('color','minPrice','maxPrice')):
                cursor = Items.find({ 'size' : params['size'], 'price' : { '$lt': int(params['maxPrice']), '$gt': int(params['minPrice']) }})
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by size and price less than
            elif all (i in params for i in ('size','maxPrice')):
                cursor = Items.find({ 'size' : params['size'], 'price' : { '$lt': int(params['maxPrice'])}  })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by size and price greater than
            elif all (i in params for i in ('size','minPrice')):
                cursor = Items.find({ 'size' : params['size'], 'price' : { '$gt': int(params['minPrice'])}  })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by size
            elif 'size' in params:
                cursor = Items.find({ 'size' : params['size'] })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by color
            elif 'color' in params:
                cursor = Items.find({ 'color' : params['color'] })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by price less than
            elif 'maxPrice' in params:
                cursor = Items.find({ 'price' : { '$lt': int(params['maxPrice'])} })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by price more than
            elif 'minPrice' in params:
                cursor = Items.find({ 'price' : { '$gt': int(params['minPrice'])} })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by price in range
            elif all (i in params for i in ('maxPrice','minPrice')):
                cursor = Items.find({ 'price' : {'$gt': int(params['minPrice']), '$lt': int(params['maxPrice']) }})
                result = list(cursor)
                resp.body = dumps(result)

        else:

            # Show all products
            cursor = Items.find()
            result = list(cursor)
            resp.body = dumps(result)


class FilterCategory:

    def on_get(self, req, resp, category):

        params = req.params
        
        if params:
            # Filter by category, color, size, and price range
            if all (i in params for i in ('color','size','minPrice','maxPrice')):
                cursor = Items.find({ 'parent' : category, 'color' : params['color'], 'size' : params['size'], 'price' : { '$gt': int(params['minPrice']), '$lt': int(params['maxPrice']) }})
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by category, color, size and price less than
            elif all (i in params for i in ('color','size','maxPrice')):
                cursor = Items.find({ 'parent' : category, 'color' : params['color'], 'size': params['size'], 'price' : { '$lt': int(params['maxPrice'])}  })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by category, color, size and price greater than
            elif all (i in params for i in ('color','size','minPrice')):
                cursor = Items.find({ 'parent' : category, 'color' : params['color'], 'size': params['size'], 'price' : { '$gt': int(params['minPrice'])}  })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by category, color, size
            elif all (i in params for i in ('color','size')):
                cursor = Items.find({ 'parent' : category, 'color' : params['color'], 'size': params['size']  })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by category, color and price range
            if all (i in params for i in ('color','minPrice','maxPrice')):
                cursor = Items.find({ 'parent' : category, 'color' : params['color'], 'price' : { '$gt': int(params['minPrice']), '$lt': int(params['maxPrice']) }})
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by category, color and price less than
            elif all (i in params for i in ('color','maxPrice')):
                cursor = Items.find({ 'parent' : category, 'color' : params['color'], 'price' : { '$lt': int(params['maxPrice']) }})
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by category, color and price greater than
            elif all (i in params for i in ('color','minPrice')):
                cursor = Items.find({ 'parent' : category, 'color' : params['color'], 'price' : { '$gt': int(params['minPrice'])}  })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by category, size and price range
            if all (i in params for i in ('size','minPrice','maxPrice')):
                cursor = Items.find({ 'parent' : category, 'size' : params['size'], 'price' : { '$gt': int(params['minPrice']), '$lt': int(params['maxPrice']) }})
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by category, size and price less than
            elif all (i in params for i in ('size','maxPrice')):
                cursor = Items.find({ 'parent' : category, 'size' : params['size'], 'price' : { '$lt': int(params['maxPrice'])}  })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by category, size and price greater than
            elif all (i in params for i in ('size','minPrice')):
                cursor = Items.find({ 'parent' : category, 'size' : params['size'], 'price' : { '$gt': int(params['minPrice'])}  })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by category, size
            elif 'size' in params:
                cursor = Items.find({ 'parent' : category, 'size' : params['size'] })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by category, color
            elif 'color' in params:
                cursor = Items.find({ 'parent' : category, 'color' : params['color'] })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by category, price less than
            elif 'maxPrice' in params:
                cursor = Items.find({ 'parent' : category, 'price' : { '$lt': int(params['maxPrice'])} })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by category, price more than
            elif 'minPrice' in params:
                cursor = Items.find({ 'parent' : category, 'price' : { '$gt': int(params['minPrice'])} })
                result = list(cursor)
                resp.body = dumps(result)

            # Filter by category,  price in range
            elif all (i in params for i in ('maxPrice','minPrice')):
                cursor = Items.find({ 'parent' : category, 'price' : {'$gt': int(params['minPrice']), '$lt': int(params['maxPrice']) }})
                result = list(cursor)
                resp.body = dumps(result)

        else:

            # Show all products with category
            cursor = Items.find({ 'parent' : category })
            result = list(cursor)
            resp.body = dumps(result)

# API route :
api = falcon.API()

# Return all products
api.add_route('/api/products', Filter())

# Return products with filtered category
api.add_route('/api/products/category/{category}', FilterCategory())