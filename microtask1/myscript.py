import argparse
import os
import json
import codecs
from perceval.backends.core.git import Git

parser = argparse.ArgumentParser(description = "Count commits in a git repo")
parser.add_argument("repo", help = "Repository url")
parser.add_argument("dir", help = "Directory for cloning the repository")
parser.add_argument("--print", action='store_true', help = "Print hashes")
args = parser.parse_args()

print(os.getcwd())
path = os.getcwd()
filepath = path + "/sample2.json"
newfile = open(filepath,'w')
filepath2 = path + "/timezones.json"
repo = Git(uri=args.repo, gitpath=args.dir)
count = 0
t_data = []
data = []
# with open(filepath2) as outfile:
time_data = json.load(codecs.open(filepath2, 'r', 'utf-8-sig'))
# json.loads(open(filepath2).read().decode('utf-8-sig'))
for p in time_data:
    st = p['WindowsTimeZones'][0]['Name']
    # print(st[4:10])
    p['TimeZone'] = st[4:7]+st[8:10]
    t_data.append(p)

with open(filepath2, 'w') as outfile:
        json.dump(t_data, outfile)

for x in repo.fetch():
    t_val = x['data']['AuthorDate'][-5:]
    list_of_countries = []
    for p in time_data:
        if t_val == p['TimeZone']:
            # print(t_val,p['TimeZone'],'afdf') 
            list_of_countries.append(p['CountryName'])
    x['data']['CountryName'] = list_of_countries
    x['data']['TimeZone'] = t_val
    print(x)
    data.append(x)
with open(filepath, 'w') as outfile:
        json.dump(data, outfile)
# for commit in repo.fetch():
#     if args.print:
#         print(commit['data']['commit'])
#     count += 1
# print("Number of commmits: %d." % count)

