from bs4 import BeautifulSoup
import requests
import csv

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

def get_data(rows) -> list:
  column_dict = {}
  data_list = []
  columns = fields(rows)
  for column in columns:
    column_dict[column] = ''

  for row in rows:
    cells = row.find_all('td')

    index = 0
    for cell in cells:
      column_dict[columns[index]] = cell.text 
      index += 1
      index = index % len(columns)
      if index == 0:
        column_dict = {}
        data_list.append(column_dict)
  return data_list

def data_to_csv(rows, filename: str):
  columns = fields(rows)
  data = get_data(rows)
  if columns == None:
    print("Error: Can't create a csv from an empty list.")
    return None
  try:
      with open(filename, 'w') as csvfile:
          writer = csv.DictWriter(csvfile, fieldnames=columns)
          writer.writeheader()  
          writer.writerows(data)
  except IOError:
      print("I/O error")