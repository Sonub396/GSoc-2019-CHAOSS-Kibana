### GSOC 2019

#### Micro Task 1:

- Added a custom timezones.json file with all the country names/codes and their respective timezones(source:[here](https://stackoverflow.com/questions/1234563/country-to-timezone-mapping-database))
- Wrote a python script(myscript.py)for taking the utc timezone for every author/user from the object obj['data']['AuthorDate'] field with the help of perceval repo.fetch()
- Indexed the newly created country and timezone fields into new elastic indexes (using createindex.py)
- Created a dashboard git-country-dashboard.json
