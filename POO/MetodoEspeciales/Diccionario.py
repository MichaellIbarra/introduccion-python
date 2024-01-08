personas = {'Michaell': 'Martinez', 'Juan': 'Perez'}
# print(personas.get('Juan'))
# print(personas.items())
# print(personas.keys())
# print(personas.values())
personas.pop('Juan')
personas.clear()
for c,v in personas.items():
    print(c,v)
    
