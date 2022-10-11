import yaml

data = yaml.safe_load(open('/home/danilo/Documentos/Joshua---Assistente-Virtual/nlu/train.yml', 'r', encoding='utf-8').read())

for command in data['commands']:
    print(command)