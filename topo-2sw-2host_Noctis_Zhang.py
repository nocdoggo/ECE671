"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        # Here, we need 6 nodes
        n1 = self.addHost( 'n1' )
        n2 = self.addHost( 'n2' )
        n3 = self.addHost( 'n3' )
        n4 = self.addHost( 'n4' )
        n5 = self.addHost( 'n5' )
        n6 = self.addHost( 'n6' )

        # Add 2 switches into the system
        switch1 = self.addSwitch( 'switch1' )
        switch2 = self.addSwitch( 'switch2' )

        # Don't think I need to change the remaining parts.
        # Add links
        self.addLink( n6, switch1 )
        self.addLink( n1, switch1 )
        self.addLink( n2, switch1 )

        self.addLink( n5, switch2 )
        self.addLink( n4, switch2 )
        self.addLink( n3, switch2 )

        self.addLink( switch1, switch2 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
