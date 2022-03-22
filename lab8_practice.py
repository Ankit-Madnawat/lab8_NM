from ncclient import manager

m = manager.connect(host='198.51.100.1', port=22, username='ankit', password='lab8', hostkey_verify=False)
c = m.get_config(source='running')
print(c)