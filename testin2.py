from stem import CircStatus
from stem.control import Controller

with Controller.from_port(port = 9051) as controller:
    controller.authenticate(password = 'my_password')
    #controller.signal()
    #controller.close()
for circ in controller.get_circuits():
    if circ.status != CircStatus.BUILT:
        continue  # skip circuits that aren't yet usable
        
    entry_fingerprint = circ.path[0][0]
    entry_descriptor = controller.get_network_status(entry_fingerprint, None)
        
    if entry_descriptor:
        print ("Circuit %s starts with %s" % (circ.id, entry_descriptor.address))
    else:
        print ("Unable to determine the address belonging to circuit %s" % circ.id)