def get_formatted_location(city, country, population=0):
	"""Generate a neatly formatted location name."""

	location_info = city + ', ' + country
	location_info = location_info.title()
	if population:
		location_info += ' - population ' + str(population)

	return location_info
