from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from threading import Thread

import time


def customtopo():
    info('*** Adding controller\n')
    c0 = net.addController(
        name='c0', controller=RemoteController, ip='192.168.58.129', port=6633)

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


def tester1(host):
    info(host.cmd('python traffic1.py &'))


def tester2(host):
    info(host.cmd('python traffic2.py &'))


def runEverything(net):
    for host in hosts[0:1]:
        t = Thread(target=tester, args=(host, ))
        t.start()
        time.sleep(0.2)

    time.sleep(60)
    info(hosts[45].cmd('hping3 10.0.0.46 -p 12345 -S -i u33000 -c 450'))
    info(hosts[44].cmd('hping3 10.0.0.46 -p 12345 -S -i u33000 -c 450'))
    time.sleep(10)

    for host in hosts[10:26]:
        t = Thread(target=tester1, args=(host, ))
        t.start()
        time.sleep(0.2)

    time.sleep(72)
    info(hosts[45].cmd('hping3 10.0.0.46 -p 12345 -S -i u14285 -c 1050'))
    info(hosts[44].cmd('hping3 10.0.0.46 -p 12345 -S -i u11111 -c 1350'))
    time.sleep(33)

    for host in hosts[26:44]:
        t = Thread(target=tester2, args=(host, ))
        t.start()
        time.sleep(0.2)

    time.sleep(600)
    
    for host in hosts[0:10]:
        t = Thread(target=tester, args=(host, ))
        t.start()
        time.sleep(0.2)
    for host in hosts[10:26]:
        t = Thread(target=tester1, args=(host, ))
        t.start()
        time.sleep(0.2)
    info(hosts[45].cmd('hping3 10.0.0.46 -p 12345 -S -i u10000 -c 1500'))
    info(hosts[44].cmd('hping3 10.0.0.46 -p 12345 -S -i u10000 -c 1500'))


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
    th = Thread(target=runEverything, args=(net, ))
    th.start()

    info('*** Running CLI\n')
    CLI(net)
    info('*** Stopping network')
    net.stop()
