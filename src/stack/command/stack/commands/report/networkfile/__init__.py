# @SI_COPYRIGHT@
# @SI_COPYRIGHT@

import stack.commands
import string
import csv
import cStringIO

class Command(stack.commands.Command, stack.commands.HostArgumentProcessor):
	"""
	Outputs a network file in CSV format.
	<dummy />
	"""

	def doNetwork(self, csv_w):
		row = []

		output = self.call('list.network')

		for o in output:
			network = o['network']
			zone = o['zone']
			netmask = o['mask']
			mtu = o['mtu']
			dns = o['dns']
			address = o['address']
			gateway = o['gateway']
			pxe = o['pxe']
			row = [ network, address, netmask, gateway, 
				mtu, zone, dns, pxe]

			csv_w.writerow(row)

	def run(self, params, args):

		header = ['NETWORK', 'ADDRESS', 'MASK', 'GATEWAY', 
			'MTU', 'ZONE', 'DNS','PXE']

		# CSV writer requires fileIO.
		# Setup string IO processing
		csv_f = cStringIO.StringIO()
		csv_w = csv.writer(csv_f)
		csv_w.writerow(header)

		self.doNetwork(csv_w)

		# Get string from StringIO object
		s = csv_f.getvalue().strip()
		csv_f.close()

		self.beginOutput()
		self.addOutput('',s)
		self.endOutput()
