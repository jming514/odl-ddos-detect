from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):
        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches
        hosta = self.addHost('h1')
        hostb = self.addHost('h2')
        hostc = self.addHost('h3')
        hostd = self.addHost('h4')
        hoste = self.addHost('h5')
        hostf = self.addHost('h6')
        switcha = self.addSwitch('s1')

        # Add links
        self.addLink(hosta, switcha)
        self.addLink(hostb, switcha)
        self.addLink(hostc, switcha)
        self.addLink(hostd, switcha)
        self.addLink(hoste, switcha)
        self.addLink(hostf, switcha)


topos = {'mytopo': (lambda: MyTopo())}