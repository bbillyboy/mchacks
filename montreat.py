import pandas as pd
businesses = pd.read_csv('businesses.csv')
violations = pd.read_csv('violations.csv')
restaurants = businesses["name"].tolist()
open_restaurants = businesses.loc[businesses['statut'] == "Fermé"]["name"].tolist()
open_violations = violations.loc[violations['etablissement'].isin(open_restaurants)]["etablissement"].tolist()
open_violations_desc = violations.loc[violations['etablissement'].isin(open_restaurants)]["description"].tolist()
violations_list = violations["etablissement"].tolist()
to_display = []
for business in open_restaurants:
    if business not in violations_list:
        to_display.append(business)

import requests

API_KEY_g = 'YOUR-API-KEY'

def get_keywords(text):
    url = "https://api.twinword.com/api/text/classify/latest/"

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    params = {
        'apikey': API_KEY_g,
        'text': text,
    }

    response = requests.post(url, headers=headers, params=params)
    result = response.json()

    return result

def search_restaurants(api_key, location, radius, keyword='restaurant'):
    endpoint = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'key': api_key,
        'query': f'{keyword} in {location}',
        'radius': radius
    }

    response = requests.get(endpoint, params=params)
    results = response.json().get('results', [])

    return results

def search_groceries(api_key, location, radius, keyword='grocery store'):
    endpoint = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'key': api_key,
        'query': f'{keyword} in {location}',
        'radius': radius
    }

    response = requests.get(endpoint, params=params)
    results = response.json().get('results', [])

    return results

def search_butchers(api_key, location, radius, keyword='butcher'):
    endpoint = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'key': api_key,
        'query': f'{keyword} in {location}',
        'radius': radius
    }

    response = requests.get(endpoint, params=params)
    results = response.json().get('results', [])

    return results

def search_pharma(api_key, location, radius, keyword='pharmacy'):
    endpoint = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'key': api_key,
        'query': f'{keyword} in {location}',
        'radius': radius
    }

    response = requests.get(endpoint, params=params)
    results = response.json().get('results', [])

    return results

def search_cafes(api_key, location, radius, keyword='cafe'):
    endpoint = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'key': api_key,
        'query': f'{keyword} in {location}',
        'radius': radius
    }

    response = requests.get(endpoint, params=params)
    results = response.json().get('results', [])

    return results

def search_delis(api_key, location, radius, keyword='deli'):
    endpoint = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'key': api_key,
        'query': f'{keyword} in {location}',
        'radius': radius
    }

    response = requests.get(endpoint, params=params)
    results = response.json().get('results', [])

    return results


def extract_restaurant_info(restaurant):
    info = {
        'name': restaurant['name'],
        'address': restaurant['formatted_address'],
        'rating': restaurant.get('rating', 'N/A'),
        'price_level': restaurant.get('price_level', 'N/A'),
        'cuisine': ', '.join(restaurant['types']) if 'types' in restaurant else 'N/A'
    }
    return info

def extract_groceries_info(groceries):
    info = {
        'name': groceries['name'],
        'address': groceries['formatted_address'],
        'rating': groceries.get('rating', 'N/A'),
        'price_level': groceries.get('price_level', 'N/A'),
        'cuisine': ', '.join(groceries['types']) if 'types' in groceries else 'N/A'
    }
    return info

def extract_butcher_info(butcher):
    info = {
        'name': butcher['name'],
        'address': butcher['formatted_address'],
        'rating': butcher.get('rating', 'N/A'),
        'price_level': butcher.get('price_level', 'N/A'),
        'cuisine': ', '.join(butcher['types']) if 'types' in butcher else 'N/A'
    }
    return info

def extract_pharma_info(pharma):
    info = {
        'name': pharma['name'],
        'address': pharma['formatted_address'],
        'rating': pharma.get('rating', 'N/A'),
        'price_level': pharma.get('price_level', 'N/A'),
        'cuisine': ', '.join(pharma['types']) if 'types' in pharma else 'N/A'
    }
    return info

def extract_cafe_info(cafe):
    info = {
        'name': cafe['name'],
        'address': cafe['formatted_address'],
        'rating': cafe.get('rating', 'N/A'),
        'price_level': cafe.get('price_level', 'N/A'),
        'cuisine': ', '.join(cafe['types']) if 'types' in cafe else 'N/A'
    }
    return info

def extract_deli_info(deli):
    info = {
        'name': deli['name'],
        'address': deli['formatted_address'],
        'rating': deli.get('rating', 'N/A'),
        'price_level': deli.get('price_level', 'N/A'),
        'cuisine': ', '.join(deli['types']) if 'types' in deli else 'N/A'
    }
    return info

if __name__ == "__main__":
    text = input("Hi, I'm the Montreat Man, how can I help you find small, eco-friendly businesses in Montreal?")

    keys = get_keywords(text)
    api_key = 'YOUR-API-KEY'
    location = 'Montreal'
    
    if keys is not None:
        print(f"Keywords: {keys}")
    else:
        print("Unable to fulfill request, please try entering a different instruction")
    print(keys)

    imp_keys = [key for key in keys['keywords']]


    if 'nearby' in imp_keys or 'near' in imp_keys:
      radius = 1000
    else:
      radius = 5000

    if 'grocery' in imp_keys or 'groceries' in imp_keys:
      res = search_groceries(api_key, location, radius)
    elif 'butcher' in imp_keys or 'butchers' in imp_keys:
      res = search_butchers(api_key, location, radius)
    elif 'pharmacy' in imp_keys or 'pharmacies' in imp_keys:
      res = search_pharma(api_key, location, radius)
    elif 'cafe' in imp_keys or 'cafes' in imp_keys:
      res = search_cafes(api_key, location, radius)
    elif 'deli' in imp_keys or 'delis' in imp_keys:
      res = search_delis(api_key, location, radius)
    else:
      res = search_restaurants(api_key, location, radius)

    df = pd.DataFrame()

    if res:
      for index, business in enumerate(res, start=1):
        if 'grocery' in imp_keys:
          info = extract_groceries_info(business)
        elif 'butcher' in imp_keys:
          info = extract_butcher_info(business)
        elif 'pharmacy' in imp_keys:
          info = extract_pharma_info(business)
        elif 'cafe' in imp_keys:
          info = extract_cafe_info(business)
        elif 'deli' in imp_keys:
          info = extract_deli_info(business)
        else:
          info = extract_restaurant_info(business)

        df = df.append(info, ignore_index=True)

if 'cheap' in imp_keys:
  df = df[df['price_level'] == 1]

if 'fancy' in imp_keys or 'expensive' in imp_keys:
  df = df[df['price_level'] == 3]

if 'bad' in imp_keys:
  df = df[df['rating'] <= 2]

if 'good' in imp_keys or 'quality' in imp_keys:
  df = df[df['rating'] >= 4.5]

if df.empty:
  print("No businesses found!")
  exit()

def condition(x):
    if x.lower() in open_violations:
        return 'Yes'
    else:
        return 'No'

# Apply the condition to create a new column
df['Warnings'] = df['name'].apply(condition)

