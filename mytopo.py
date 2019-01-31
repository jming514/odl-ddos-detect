from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from threading import Thread

import time


def customtopo():
    info('*** Adding controller\n')
    c0 = net.addController(name='c0', controller=RemoteController, ip='192.168.58.129', port=6633)

    info('*** Adding switches\n')
    switcha = net.addSwitch('s1')
    switchb = net.addSwitch('s2')

    info('*** Adding hosts\n')
    for h in range(1, 46):
        net.addHost('h' + str(h))
        # net.addLink('h' + str(h), switcha)
    net.addHost('server')

    info('*** Creating links\n')
    net.addLink('server', switchb)
    net.addLink(switcha, switchb)
    for h in range(1, 46):
        net.addLink('h' + str(h), switcha)

def tester(host):
    info(host.cmd('ifconfig'))

def runEverything(net):
    for host in hosts[:-1]:
        t = Thread(target=tester, args=(host,))
        t.start()
        time.sleep(.1)

    hosts[-1].cmd('python server.py')

if __name__ == '__main__':
    setLogLevel('info')
    "Create an empty network and then add nodes"
    net = Mininet()
    customtopo()
    info('*** Starting network\n')
    net.start()
    hosts = net.hosts
    time.sleep(2)
    runEverything(net)
    info('*** Running CLI\n')
    CLI(net)
    info('*** Stopping network')
    net.stop()
    


# def runEverything():
#     topo = MyTopo(Topo)
#     net = Mininet(topo)
#     net.start()
#     hosts = net.hosts
#     # hosts[-1].cmd('python server.py &')
#     for host in hosts:
#         host.cmd('pingall')
    
    
# if __name__ == '__main__':
#     runEverything()