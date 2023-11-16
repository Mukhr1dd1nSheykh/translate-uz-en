from googletrans import Translator 
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def io():
    if request.form.get('suz'):
        suz = request.form.get('suz')
        translator = Translator()
        translate_channel = translator.translate(suz, src='uz', dest='en').text
        print(translate_channel)
    else:
        translate_channel = None
        suz = None
    return render_template('home.html',tarjima=translate_channel,suz=suz)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)