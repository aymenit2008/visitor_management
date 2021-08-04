from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Document"),
			"items": [
				{
					"type": "doctype",
					"name": "Trans YM",
					"onboard": 1,
				}
			]
			
		}
	]
