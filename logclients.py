from kismetclient import Client as KismetClient
from kismetclient import handlers
 
# Connect to the Kismet server.
address = ('127.0.0.1', 2501)
k = KismetClient(address)
 
# Sets are nice because they only keep unique data.
try:
    from sets import Set
    clients = Set()
except Exception: # In python3 you don't have to explicitly import Sets
    clients = set()
 
def handle_client(client, mac):
    global clients
    clients.add(mac)
 
k.register_handler('CLIENT', handle_client)                       
 
try:
    print('Logging wireless network clients.')
    while True:
        k.listen()
except KeyboardInterrupt:
    print('Clients:')
    for i, client in enumerate(clients, start=1):
        print('%d. MAC: %s' % (i, client))
    print('%d unique clients have been seen.' % len(clients))
