import csv

examples_file = 'Examples.csv'
entries_file = 'Entriesnodu.csv'

#The entries dict for search
entries = {}

#entry-id dict to build the entries search dict
entries_ids = {}

#build the entries search dict
with open(entries_file) as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        melingoId = row["MelingoId"]
        entry = row["Entry"]
        entries_ids[melingoId] = entry
        entries[entry] = row
        entries[entry]["examples"] = []

with open(examples_file) as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        melingoId = row["MelingoID"]
        if melingoId in entries_ids:
            e = entries_ids[melingoId]
            entries[entries_ids[melingoId]]["examples"].append(row["Text"])

#search entry
def search_entry(entry):
    if entry in entries:
        return entries[entry]["examples"]
    return ["Not exist"]

#tests
example_result = search_entry("blanket")
assert example_result == ['If it is cold tonight', 'a <b>blanket</b> of fog concealed the view of the harbor',
                          "It's going to get cold tonight so you may need extra <b>blankets</b>."]
