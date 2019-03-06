#!/usr/bin/python3
print('lorem')
import etcd
print('ipsum')
is_ready = False
print('dolor')
client = etcd.Client(host='etcd', port=2379)
print('sit')
while not is_ready:
    print('amet')
    print(is_ready)
    print("dupa")
    try:
        print('dupa')
        os.environ['POSTGRES_USER'] = client.read('/db_data/user').value
        print('i tak dalej')
        os.environ['POSTGRES_DB'] = client.read('/db_data/user').value
        os.environ['POSTGRES_PASSWORD'] = client.read('/db_data/pswd').value
        is_ready = True
    except:
    	is_ready = False

print(is_ready)
if is_ready:
    os.execvp('docker-entrypoint.sh', ('docker-entrypoint.sh', *sys.argv[1:]))
