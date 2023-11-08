import requests
import time
import pandas

#Ievadīt API key
GOOGLE_API_KEY = 'YOUR_API_KEY  ' 

# Funkcija, kura requesto Google API datus par konkrētu adresi un atgriež no json tikai Lat, Long
def extract_lat_long_via_address(address_or_zipcode):
    lat, lng = None, None
    api_key = GOOGLE_API_KEY
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{base_url}?address={address_or_zipcode}&key={api_key}"
    r = requests.get(endpoint)
    if r.status_code not in range(200, 299):
        return None, None
    try:
        results = r.json()['results'][0]
        lat = results['geometry']['location']['lat']
        lng = results['geometry']['location']['lng']
    except:
        pass
    #Sleep ir, lai neizauktu parāk daudz liekus request taupot API resursus
    time.sleep(1)
    return lat, lng


df = pandas.read_csv('./CSV_adreses.csv', sep=';')
rows = len(df)  # šis nosaka cik csv failā ir rindas
print(rows)
result = df.iloc[0, 0] # Šis lasa csv tabulai, 1 rindu, kolnā (Adreses pieraksts) datus jeb Lielirbes iela
result = df.iloc[1, 0] # Šis lasa csv tabulai, 2 rindu, kolnā (Adreses pieraksts) datus jeb Zaļā iela
print(result)



i = 0
while i < rows:
  print(i)
  result = df.iloc[i, 0]
  #extract_lat_long_via_address("Raiņa bulvāris 8, Centra rajons, Rīga, LV-1050")
  address_lat, address_lng = extract_lat_long_via_address(result)
  print(address_lat)
  print(address_lng)
  #ieraksta csv lat un long
  df.iloc[i,1] = address_lat
  df.iloc[i,2] = address_lng
  #saglabā ierakstu csv failā
  df.to_csv('./CSV_adreses.csv', sep=';', index= False)
  i=i+1
  
