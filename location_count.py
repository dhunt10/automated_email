from first import getData

class locationManager():
    def __init__(self):
        """
	"""

    def getLocation(self):
        locations = []
        x = getData('Location').getData()
	for i in range(len(x['entry'])):
	    loc = x['entry'][i]['resource']['name']
	    locations.append(loc)
	return locations
