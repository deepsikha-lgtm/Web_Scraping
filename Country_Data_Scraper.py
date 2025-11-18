# Required packages
#pip install beautifulsoup4 requests pandas openpyxl
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

def get_details(country_one):
    """Extract details from a single country element"""
    country_name = country_one.find('h3', class_='country-name').text.strip()
    capital_name = country_one.find('span', class_='country-capital').text
    population = country_one.find('span', class_='country-population').text
    area = country_one.find('span', class_='country-area').text
    return country_name, capital_name, population, area

def get_soup(url):
    """Takes URL and returns a soup object"""
    resp = requests.get(url)
    if resp.status_code == 200:
        return bs(resp.text, 'html.parser')
    else:
        print(f"Error: Unable to fetch the page. Status code: {resp.status_code}")
        return None

def get_countries(url):
    """Extract details from all the countries"""
    soup = get_soup(url)
    if soup is None:
        return []
    
    country_all = soup.find_all('div', class_="col-md-4 country")
    countries = []
    for country in country_all:
        countries.append(get_details(country))
    
    return countries

if __name__ == "__main__":
    url = 'https://www.scrapethissite.com/pages/simple/'
    
    print("Scraping country data...")
    countries = get_countries(url)
    
    if countries:
        print(f"Successfully scraped data for {len(countries)} countries")
        
   
        df = pd.DataFrame(countries, columns=['Country', 'Capital', 'Population', 'Area'])
        
    
        df['Population'] = pd.to_numeric(df['Population'])
        df['Area'] = pd.to_numeric(df['Area'])
        

        print("\nFirst 5 countries:")
        print(df.head())
        
    
        excel_filename = 'countries_data.xlsx'
        df.to_excel(excel_filename, index=False, engine='openpyxl')
        
        
        csv_filename = 'countries_data.csv'
        df.to_csv(csv_filename, index=False)
        
        print(f"\nData successfully saved to:")
        print(f"- {excel_filename} (Excel format)")
        print(f"- {csv_filename} (CSV format)")
        
  
        print(f"\nBasic Statistics:")
        print(f"Total countries: {len(df)}")
        print(f"Most populated country: {df.loc[df['Population'].idxmax(), 'Country']} ({df['Population'].max():,})")
        print(f"Largest country by area: {df.loc[df['Area'].idxmax(), 'Country']} ({df['Area'].max():,} km²)")
        
    else:
        print("No data was scraped. Please check the URL and try again.")