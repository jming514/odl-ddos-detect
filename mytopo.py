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
        self.addLink('server', switchb)

        

        # Add links
        # for i in hosts:
        #     self.addLink(hosts[i], switcha)
        
        self.addLink(switcha, switchb)
        # self.addLink(hosta, switcha)
        # self.addLink(hostb, switcha)
        # self.addLink(hostc, switcha)
        # self.addLink(hostd, switcha)
        # self.addLink(hoste, switcha)
        # self.addLink(hostf, switcha)


topos = {'mytopo': (lambda: MyTopo())}