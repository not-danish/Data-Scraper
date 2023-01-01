import requests
from bs4 import BeautifulSoup

def make_request(link: str):
  # Make a request to the webpage
  return requests.get(link).text
  
def get_table_rows(link: str, div_class: str):
  # Parse the HTML content of the page
  soup = BeautifulSoup(make_request(link), 'html.parser')
  # Find the table with the class "wikitable sortable"
  table = soup.find('table', class_ = div_class)
  # Find all the rows in the table
  rows = table.find_all('tr')
  return rows

def print_rows(rows):
  # Loop through the rows and print the text of each cell
  list_1 = []
  for row in rows:
    cells = row.find_all('th')
    for cell in cells:
      print(cell.text)

def fields(rows) -> list:
  field_list = []
  for row in rows:
    cells = row.find_all('th')
    for cell in cells:
      field_list.append(cell.text)
  return field_list