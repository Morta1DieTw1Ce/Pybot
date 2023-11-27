
data = {'hi':'hello boss','how are you':'i am fine','hey':'hi',}

while True:
	You = input('You:').lower()
	if You:
		if You == 'exit':
			break
		else:
			try:
				if You in data:
					print('Bot:' + data[You])
				else:
					print('Bot: i can not understand what are you trying to say?')
			except Exception as e:
				print('System Error:' + e)
			
