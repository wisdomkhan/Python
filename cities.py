cities = {
    'Norway': {'Country': 'Europe', 'Population': 5432580},
    'Ohio': {'Country': 'US', 'Population': 11689100},
    'Aizawl': {'Country': 'India', 'Population': 293416}
         }
for i, j in cities.items():
    print('CITY: ' + i + '\nCOUNTRY: ' + j['Country'] + '\nPOPULATION: ', j['Population'], '\n')
