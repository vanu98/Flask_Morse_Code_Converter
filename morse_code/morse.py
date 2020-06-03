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
from flask import *
app =Flask(__name__)

@app.route('/')
def page():
	return render_template('log.html')

@app.route('/convert', methods=['POST', 'GET'])
def convert():
	if request.method == 'POST':
		result = request.form
		a = result.values()
		a = list(a)
		dec = str(a[0])
		decc = decrypt(dec)
		return render_template('result.html', result=decc)

def decrypt(message): 
   
    message += ' '
  
    decipher = '' 
    citext = '' 
    for letter in message: 

        if (letter != ' '): 
 
            i = 0
            citext += letter 

        else: 

            i += 1
  
 
            if i == 2 : 
  
                decipher += ' '
            else:  
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT 
                .values()).index(citext)] 
                citext = '' 
  
    return decipher
if __name__ == '__main__':
   app.run(debug = True)