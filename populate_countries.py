import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'countries_project.settings')
django.setup()

from countries_app.models import Country

countries = [
   "Albania", "Andorra", "Australia", "Brazil", "Belgium", "Canada", "China",
   "France", "Germany", "India", "Indonesia", "Ireland", "Italy", "Japan",
   "Kenya", "Luxembourg", "Mexico", "New Zealand", "Nigeria", "Portugal",
   "Russia", "South Africa", "South Korea", "Spain", "Sweden", "Thailand",
   "Ukraine", "United Kingdom", "United States of America", "Vietnam", "Zambia"
]

for country_name in countries:
   Country.objects.get_or_create(name=country_name)

print("Countries have been added to the database.")
   