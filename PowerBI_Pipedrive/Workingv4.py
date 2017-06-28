import json


with open('persons_table','r') as file:
    json_table_3 = json.load(file)

with open('deal_table','r') as file:
    json_table_1 =  json.load(file)

with open('organizations_table','r') as file:
    json_table_2 =  json.load(file)

deal_columns = json_table_1['columns']
org_columns = json_table_2['columns']

merger_columns = []

for x in deal_columns:
    # x['name'] = 'dxxx'+x['name']
    merger_columns.append(x)

special = ['Nature of Entity', 'Organisation Sector', 'State/county', 'Region', 'Country']
for y in org_columns:
    if y['name'] in special:
        # y['name'] = 'oxxx'+y['name']
        merger_columns.append(y)

json_table_4 = {'name':'mixed', 'columns':merger_columns}

with open('persons_table','r') as file:
    json_table_3_bu = json.load(file)

with open('deal_table','r') as file:
    json_table_1_bu =  json.load(file)

with open('organizations_table','r') as file:
    json_table_2_bu =  json.load(file)

json_tables = [json_table_1_bu, json_table_2_bu, json_table_3_bu, json_table_4]
#json_tables = [json_table_1_bu, json_table_2_bu, json_table_3_bu, json_table_4]
json_data_set = {'name':'Skylark_Official_Test', 'tables':json_tables}
json_string_dataset = json.dumps(json_data_set)

with open('DataSet','w') as file:
    json.dump(json_data_set,file)

with open('See_Dataset','w') as file:
    json.dump(json_data_set,file,indent=4)

with open('rows_deals','r') as file:
    deal_rows = json.load(file)

with open('rows_organizations','r') as file:
    org_rows = json.load(file)

deal_list = deal_rows['rows']
org_list = org_rows['rows']

merged_rows = []
for deal in deal_list:
    for org in org_list:
        if deal['org_name'] == org['Name']:
            x = {}
            for col in merger_columns:
                if col['name'] in special:
                    x[col['name']] = org[col['name']]
                else:
                    x[col['name']] = deal[col['name']]
            merged_rows.append(x)

merger_rows_final = {'rows':merged_rows}
with open('rows_merger','w') as r:
    json.dump(merger_rows_final,r)

with open('see_rows_merger','w') as r:
    json.dump(merger_rows_final,r,indent=4)
