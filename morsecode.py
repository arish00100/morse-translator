# Python program to implement Morse Code Translator
#	Decoding

# Dictionary representing the morse code chart
import winsound,time
from threading import Timer
import pyttsx3



MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'}

# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
	keys=MORSE_CODE_DICT.keys()
	cipher = ''
	for letter in message:
		if letter != ' ':
			if letter in keys:
				cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			cipher += '/ '
	return cipher

def emptyfun():
	pass

def playdot(timeunit,frequency):
	winsound.Beep(int(frequency),int(timeunit*1000))
	# t=Timer(timeunit,emptyfun)
	# t.start()
	time.sleep(timeunit)


def playdash(timeunit,frequency):
	winsound.Beep(int(frequency),int(timeunit*3*1000))
	# t=Timer(timeunit,emptyfun)
	# t.start()
	time.sleep(timeunit)


def playsound(morse,timeunit,frequency):
	# timeunit=0.1	#0.5second
	# frequency=1000
	multiplier=0
	for symbol in morse:
		multiplier=0
		if(symbol=='.'):
			# multiplier=1
			# winsound.Beep(int(frequency),int(timeunit*1000))
			playdot(timeunit,frequency)
		elif(symbol=='-'):
			# multiplier=3
			playdash(timeunit,frequency)
		elif(symbol==' '):
			time.sleep(timeunit*3)
			# continue
			# t=Timer(timeunit*3,emptyfun)
			# t.start()
			continue
		elif(symbol=='/'):
			time.sleep(timeunit)
			continue
			# t=Timer(timeunit,emptyfun)
			# t.start()
			# continue
		else:
			pass
		
		# winsound.Beep(int(frequency),int(timeunit*multiplier*1000))
		# time.sleep(timeunit)
		# t=Timer(timeunit,emptyfun)



# Function to decrypt the string
# from morse to english
# def decrypt(message):
# 	# extra space added at the end to access the
# 	# last morse code
# 	message += ' '

# 	decipher = ''
# 	citext = ''
# 	for letter in message:

# 		# checks for space
# 		if (letter != ' '):

# 			# counter to keep track of space
# 			i = 0

# 			# storing morse code of a single character
# 			citext += letter

# 		# in case of space
# 		else:
# 			# if i = 1 that indicates a new character
# 			i += 1

# 			# if i = 2 that indicates a new word
# 			if i == 2 :

# 				# adding space to separate words
# 				decipher += ' '
# 			else:

# 				# accessing the keys using their values (reverse of encryption)
# 				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
# 				.values()).index(citext)]
# 				citext = ''

# 	return decipher

CODE_REVERSED = {value:key for key,value in MORSE_CODE_DICT.items()}

def decrypt(morse):
	text=''
	keys=CODE_REVERSED.keys()
	words=morse.split('/')
	# print(words)
	for word in words:
		letters=word.strip().split(' ')
		# print(letters)
		for letter in letters:
			if letter.strip() in keys:
				text+=CODE_REVERSED[letter]
		text+=' '
	return text

def speak(text):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)
	engine.say(text)
	engine.runAndWait()


