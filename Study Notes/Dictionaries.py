cars={
    "model": ["fiat","volvo","porsche"],
    "color": ["red","blue","green"]

}

print(f"the first car is: {cars["model"][0]} , and its color is: {cars['color'][0]} ")

prod_year = [1984,1999,2003]
cars["prod_year"] = prod_year

print(cars.keys(), type(cars.keys()))
for i in cars["model"]:
    print(i)


#del cars["model"]
#print("\n",cars)