from mininet.topo import Topo
from mininet.util import irange

class MyTopo(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches

        hosts = [self.addHost('h%d' % h) for h in irange(1, 45)]
        # hosta = self.addHost('h1')
        # hostb = self.addHost('h2')
        # hostc = self.addHost('h3')
        # hostd = self.addHost('h4')
        # hoste = self.addHost('h5')
        # hostf = self.addHost('h6')

        switcha = self.addSwitch('s1')
        switchb = self.addSwitch('s2')

        # Add links
        for i in hosts:
            self.addLink(hosts[i], switcha)
        
        self.addLink(switcha, switchb)
        # self.addLink(hosta, switcha)
        # self.addLink(hostb, switcha)
        # self.addLink(hostc, switcha)
        # self.addLink(hostd, switcha)
        # self.addLink(hoste, switcha)
        # self.addLink(hostf, switcha)


topos = {'mytopo': (lambda: MyTopo())}