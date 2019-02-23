import json

data = {str(k): str(k**2) for k in range(1, 11)}
print('Тип: {0}\tЗначение: {1}'.format(type(data), data))

data_json = json.dumps(data)
print('Тип: {0}\tЗначение: {1}'.format(type(data_json), data_json))

data_json_loads = json.loads(data_json)
print('Тип: {0}\tЗначение: {1}'.format(type(data_json_loads), data_json_loads))
