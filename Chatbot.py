
data = {'hi':'hello sir','how are you':'i am fine','hey':'hi',}

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
					print('Bot: idk')
			except Exception as e:
				print('System Error:' + e)
			