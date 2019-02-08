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
    net.addHost('server')

    info('*** Creating links\n')
    info(net.addLink('server', switchb))
    info(net.addLink(switcha, switchb))
    for h in range(1, 46):
        net.addLink('h' + str(h), switcha)

def tester(host):
    info(host.cmd('python traffic.py &'))

def runEverything(net):
    for host in hosts[0:10]:
        t = Thread(target=tester, args=(host,))
        t.start()
        time.sleep(0.2)
    time.sleep(60)
    for host in hosts[10:26]:
        t = Thread(target=tester, args=(host,))
        t.start()
        time.sleep(0.2)
    time.sleep(60)
    for host in hosts[26:44]:
        t = Thread(target=tester, args=(host,))
        t.start()
        time.sleep(0.2)

if __name__ == '__main__':
    setLogLevel('info')
    "Create an empty network and then add nodes"
    net = Mininet()
    customtopo()
    
    info('*** Starting network\n')
    net.start()
    hosts = net.hosts
    
    time.sleep(2)
    # runEverything(net)
    th = Thread(target=runEverything, args=(net,))
    th.start()

    info('*** Running CLI\n')
    CLI(net)
    info('*** Stopping network')
    net.stop()
