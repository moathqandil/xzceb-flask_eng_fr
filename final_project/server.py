from machinetranslation import translator
from flask import Flask, render_template, request
import machinetranslation
import json


app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    FranchText = machinetranslation.translator.english_to_french(textToTranslate)
    return FranchText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    EnglishText = machinetranslation.translator.french_to_english(textToTranslate)
    return EnglishText

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
