## Some details

BACnet devices use the Who-Is request to translate device identifiers into network addresses. This is very similar to a decentralized DNS service, but the names are unsigned integers. The request is broadcast on the network and the client waits around to listen for I-Am messages. The source address of the I-Am response is “bound” to the device identifier and most communications are unicast thereafter.
