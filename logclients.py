from kismetclient import Client as KismetClient
 
# Connect to the Kismet server.
address = ('127.0.0.1', 2501)
k = KismetClient(address)
 
# Sets are nice because they only keep unique data.
try:
    from sets import Set
    clients = Set()
except ImportError: # In python3 you don't have to explicitly import Sets
    clients = set()

def handle_client(client, **fields):
    # 0: Access Point, 1: Ad-Hoc, 2: Probe request, 3: Turbocell, 4: Data
    if int(fields['type']) in (0, 1):
        return None
    global clients
    l = len(clients)
    clients.add(fields['mac'])
    if l != len(clients):
        print ('-' * 80)
        print('New device detected:')
        for k, v in fields.items():
            print('%s: %s' % (k, v))
 
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
