def next(month):
	return (month[0] if month[1] < 12 else month[0] + 1, month[1] + 1 if month[1] < 12 else 1)