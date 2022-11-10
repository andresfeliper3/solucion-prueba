import json
import requests
from jinja2 import Environment, FileSystemLoader, PackageLoader, select_autoescape
API = 'https://catfact.ninja'
# GET request
response = requests.get(f'{API}/facts')
json_data = json.loads(response.text)
cat_facts = json_data['data']

# template
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
template = env.get_template('hello.html')

# output
output = template.render(data=cat_facts)
print(output)
