# @SI_Copyright@
# @SI_Copyright@

import stack.commands.set.network

class Command(stack.commands.set.network.command):
	"""
	Sets the network name of a network.

        <arg type='string' name='network' optional='0' repeat='0'>
        The name of the network.
	</arg>
	
	<param type='string' name='name' optional='0'>
        Name that the named network should have.
	</param>
	
	<example cmd='set network name private name=data'>
        Changes the name of the "private" network to "data".
	</example>
	"""
                
        def run(self, params, args):

                (networks, name) = self.fillSetNetworkParams(args, 'name')
                if len(networks) > 1:
                        self.abort('must specify a single network')
			        	
        	for network in networks:
			self.db.execute("""
                        	update subnets set name='%s' where
				subnets.name='%s'
                                """ % (name, network))
