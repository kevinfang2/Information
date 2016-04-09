for x in xrange(1,100):
	printthing = ''
	if x % 3 == 0:
		printthing += 'Fizz'
	if x % 5 == 0:
		printthing += 'buzz'	
	print printthing or x