from kismetclient import Client as KismetClient
from kismetclient import handlers
import logging

log = logging.getLogger('kismetclient')
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)

# Connect to Kismet server
address = ('127.0.0.1', 2501)
k = KismetClient(address)

def handle_ssid(client, ssid, mac):
    print 'ssid spotted: "%s" with mac %s' % (ssid, mac)

# Register handlers that act on input from Kismet server
k.register_handler('SSID', handle_ssid)
k.register_handler('TRACKINFO', handlers.print_fields)

# Listen, carefully
try:
    while True:
        k.listen()
except KeyboardInterrupt:
    pprint(k.protocols)
    log.info('Exiting...')
