from functools import reduce


spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [obj['name'] for obj in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [obj for obj in spicy_foods if obj['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    ## Joining with string
    ## list1 = " geeks "
    ## print("$".join(list1))
    # PRINTS $g$e$e$k$s$ so joining strings with "\n" joins them through newlines.
    ## Without the join to treat this output like a string, this creates a generator func which we don't want. 
    print("\n".join((f"{obj['name']} ({obj['cuisine']}) | Heat Level: {'🌶' * obj['heat_level']}") for obj in spicy_foods))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [obj for obj in spicy_foods if obj['cuisine'] == cuisine.title()][0]

def print_spiciest_foods(spicy_foods):
    print("\n".join([f"{obj['name']} ({obj['cuisine']}) | Heat Level: {'🌶' * obj['heat_level']}" for obj in spicy_foods if obj['heat_level'] > 5]))

def get_average_heat_level(spicy_foods):
    ## functools.reduce(function, iterable, initial)
    ## x is assigned the initial value 0 while y is the current element in target list/array 
    ## Therefore, 0 + 9 occurs. Since x is the accumulator, it carries the previous result into
    ## the next iteration of reduce so 9 + 3 occurs.
    return int((reduce(lambda x,y: x + y['heat_level'], spicy_foods, 0)) / len(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods


print(create_spicy_food(spicy_foods,{
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    } ))