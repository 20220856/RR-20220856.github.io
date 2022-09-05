# Network Devices / Domain Name Systems

### Network Bridge
A network bridge has one input and one output - it is used to isolate network traffic and computers from the wider network - this is known as a "Collision Domain". This is generally used to save on bandwidth, but it can also filter network traffic that needs to pass through itself, allowing things through when needed. Bridges work at the SECOND level of the OSI model (Media Access Control - or MAC)

### Network Switch
Switches are layer 2 devices (MAC)
Store and Forward mode checks the entire sent packet of data to ensure the integrity of the data. It is more suited to large local area networks to ensure that errors are not propagated across the network. 

### Routers
Routers operate at the third OSI layer (Network layer), and use different protocols to route packets correctly from source to destination. They have a proper routing table which is updated in realtime, but also make the decision through which channels to send packets to ensure the data arrives at the destination as soon as possible. This may involve sending data through a geographically longer, but less network congested channel - etc. 

# Network Operating System
A network operating system is software that runs on a server and enables it to manage data, users, groups, security, applications and other networking functions for the entire network. It allows multiple clients to share resources. A Network operating system must be able to perform multiple processes at once, and accomplish this with scheduling software that is built directly into the execution environment. It allocates internal processor time, memory, and other limited facets of the system to clients that need it, in a manner that allows them to share the resources.
