from mininet.node import Controller, RemoteController, OVSController, DefaultController
from mininet.net import Mininet
from mininet.topolib import TreeTopo
from mininet.link import TCLink,TCIntf
from mininet.log import setLogLevel, info
from mininet.util import dumpNodeConnections
from mininet.topo import Topo
from mininet.cli import CLI 

class SmartHome( Topo ):
    "Single Switch Topology"
    def __init__( self, count=1, **params ):
        Topo.__init__( self, **params )

        host = []
        switches = []
        for i in range(30):
            s = self.addSwitch('s%d' % i)
            switches.append(s)
            for j in range(6):
                t = self.addHost('h%d' % (i * 6 + j))
                host.append(t)
                self.addLink(t, s)

net = Mininet( topo=SmartHome(180))
net.start()
CLI(net)
net.stop()

