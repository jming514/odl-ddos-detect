from mininet.topo import Topo
from mininet.util import irange

class MyTopo(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches
        switcha = self.addSwitch('s1')
        switchb = self.addSwitch('s2')

        for h in range(1, 46):
            self.addHost('h' + str(h))
            self.addLink('h' + str(h), switcha)
        
        self.addHost('server')

        # Add links
        self.addLink('server', switchb)
        self.addLink(switcha, switchb)



topos = {'mytopo': (lambda: MyTopo())}