import csv
import pprint as pp
def get_id(q):
    # gets the id
    if q[0].isdigit():
        # address case
        return addr_to_id[q]
    elif q[0]=='(' or q[0] == '[':
        # long lat case
        return q            
    else:
        # name case
        return name_to_id[q]

# load data
csv_data = "sample_csv.csv" # change this
name_to_id = {}
addr_to_id = {}
count = 1
with open(csv_data, mode='r', encoding='utf-8', errors='ignore', newline='') as f:
    csv_file = csv.reader(f, delimiter=',', quotechar='"')
    for r in csv_file:
        if count == 1:
            count += 1 # skip the first line
        else:
            name_to_id[r[5]] = r[2] # add name and id into dict
            # addr = " ".join((r[24].split())) # process the address
            addr_to_id[r[24]] = r[2] # add address and id into dict

# ask for input
query = input("Please enter name or address: ")
print("Your answer to that is:",get_id(query))