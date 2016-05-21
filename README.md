# productAPI
An API endpoint for product and category management

## Route List :

#### Show all product :
```
/api/products
```
#### Filter all product with color, size and price range:
```
/api/products?color=color&size=size&minPrice=minPrice&maxPrice=maxPrice
```
#### Filter all product with color, size and price less than:
```
/api/products?color=color&size=size&maxPrice=maxPrice
```
#### Filter all product with color, size and price more than:
```
/api/products?color=color&size=size&minPrice=minPrice
```
#### Filter all product with color, size:
```
/api/products?color=color&size=size
```
#### Filter all product with color and price range:
```
/api/products?color=color&minPrice=minPrice&maxPrice=maxPrice
```
#### Filter all product with color and price less than:
```
/api/products?color=color&maxPrice=maxPrice
```
#### Filter all product with color and price more than:
```
/api/products?color=color&minPrice=minPrice
```
#### Filter all product with size and price range:
```
/api/products?color=color&minPrice=minPrice&maxPrice=maxPrice
```
#### Filter all product with size and price less than:
```
/api/products?color=color&maxPrice=maxPrice
```
#### Filter all product with size and price more than:
```
/api/products?color=color&minPrice=minPrice
```
#### Filter all product with color:
```
/api/products?color=color
```
#### Filter all product with size:
```
/api/products?color=color
```
#### Filter all product with price less than:
```
/api/products?maxPrice=maxPrice
```
#### Filter all product with price more than:
```
/api/products?minPrice=minPrice
```
#### Filter all product with price range:
```
/api/products?minPrice=minPrice&maxPrice=maxPrice
```

#### Filter product with Categories:
```
/api/products/categories/{categories}
```
#### For filtering product categories with price, color, and size just like filtering all product
for example below will show filtered product categories with color:
```
/api/products/categories/{categories}?color=color
```
