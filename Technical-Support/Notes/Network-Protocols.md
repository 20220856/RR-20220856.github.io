# Computer Networks

### What is a Network?
A Network - at its simplest - is a connection between two or more destinations. Anything that can be identified as a single entity can be included within a network. A computer network is, specifically, a network involving the communications of a computer.

### Network Topologies
A network topology is how a network is organised and structured, and how they communicate. There are a variety of "templates" for network topologies; including "Star", "Mesh", "Bus", "Ring", and "Hybrid".

#### Star Topologies
A star topology involves a certain device at the center of the infrastructure to which other devices are connected, responsible for the communication between all computers/devices on the network. This comes with the drawbacks of lack of redundancy, inability for individual devices to communicate, and a high pressure on the reliability of the managing device. However, it also allows easy management of network routing by the central network "Switch" or "Router".

#### Mesh Topologies
Mesh topologies have direct connections between EVERY device on the network, without a central managing device. This may be benificial because of the direct connection between them (hence faster connection), but this is only effective for networks of few devices due to the logistical challenges of physically connecting all devices together with cabling.

#### Bus Topologies
A bus tolopology involves all devices on a network being connected to a central "bus" cable. 

#### Ring Topologies
Ring topologies involve all devices being connected on a network, but using other devices as intermediaries. This means that if - for example - device A and device C want to communicate, the information must pass through device B to reach its intended destination. This may be benificial due to the comparatively low infrastructure cost of a ring topology, but potentially detrimental due to its reliance on other devices to be online at all times for the function of the topology.

#### Hybrid Topologies
Hybrid topologies - as the name infers - is a combination between multiple topology infrastructures. This is likely to be the general structure within most networks, as a hybrid topology may bring the benefits of all whilst eliminating the negatives.

# Network Architecture
### Peer to Peer (P2P) Network
The main defining characteristic of a P2P network is that there is no central, managing device. They are linked together, with equal privilege and responsibilities in processing data. As it is generally structured as a mesh topology, it shares the benefits and drawbacks of it.

### Client-Server Network
A client-server model involves a central server, responsible for managing resources and distributing them to clients. The server is responsible for managing all connected resources. It is generally structured as a star topology, sharing its benefits and drawbacks.

### Network Sizes
#### LAN - Local Area Network
Local Area Networks are usually on a small scale (ie. within a building), thus do not require extensive infrastructure.
#### MAN - Metropolitan Area Network
within a city
#### WAN - Wide Area Network
between cities

# Data Transmission

### Circuit Switching vs Packet Switching
Circuit switching infrastructure is entirely physical, between the souce and destination. Once established, the entire line is available between exclusively the source and destination, and cannot be utilised by anything else until the connection has concluded. An excellent example of this is landline telephones - there is a physical infrastructure, and it there is a physical limitation to how many connections can be made at once. 

Packet switching infrastructure, instead, utilises a router to direct one packet at a time from the destination, to send through the path of least resistance to the destination. Routers send packets through pathways that have lower amounts of network traffic, to reduce latency within the network. Through this process, there is no bandwidth wastage, as network resources are only utilised when they are needed. They are entirely digital. The fact that significantly less physical infrastructure is used results in a vastly reduced operation cost.

### Protocols and Standards

#### TCP/IP - Transmission Control Protocol/Internet Protocol
TCP is a protocol responsible for ensuring that packets are both sent FROM one device, and received BY another device. When sending packets, TCP also sends requests to the destination to ensure they are received, and if they are not, it will resend the lost packet. The TCP/IP model was developed before the OSI model.

There are 5 layers in TCP/IP;
Application - Holds the combined functions of the Application, Presentation, and Session layers of OSI model.
Transport - TCP/UDP
Network - IP/etc.
Data Link - same as osi
Physical - same as osi

#### ETHERNET/802.3 Protocol
Ethernet communication is phyical only communication for the local area network. 

#### Wifi/802.11 Protocol
figure this out


### OSI (Open Systems Interconnection) Model
The OSI model is used as a template to show which protocols are used for sending information from one device to another, and the processes utilised by the different levels

There are 7 layers within the OSI model;
Application
Presentation
Session
Transport
Network
Data Link
Physical

# IP Addresses.

32 bits (4 bytes) made of network prefix & host number



to connect 2 different sites a ROUTER is used - connecting two sites together wirelessly. a SWITCH is used to manage internal networks. 

Information added on the source end by a level in the OSI model will be removed on the receiving end by the same corresponding level.

# REVIEW THIS https://miro.medium.com/max/1024/1*17Zz6v0HWIzgiOzQYmO6lA.jpeg


