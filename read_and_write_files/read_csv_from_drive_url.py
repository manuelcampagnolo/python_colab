import pandas as pd

# https://towardsdatascience.com/read-data-from-google-sheets-into-pandas-without-the-google-sheets-api-5c468536550
# link obtido no share do ficheiro na drive
sheet_url = 'https://docs.google.com/spreadsheets/d/1Eq28NJ4cfw_Djy3M25gPMbNiH9TG_9DvMqfVLGt0QrQ/edit?usp=sharing'
url_1 = sheet_url.replace('/edit?', '/export?format=csv&')
print(url_1)
pd.read_csv(url_1)
