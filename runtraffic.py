from mininet.cli import CLI
from mininet.net import Mininet


for h in net.hosts:
    h.cmd('/mininet/custom/traffic.py &')
