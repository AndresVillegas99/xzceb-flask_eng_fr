from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    text = translator.english_to_french(textToTranslate)
    return text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    text = translator.french_to_english(textToTranslate)
    return text

@app.route("/")
def renderIndexPage():
    f = open("index.html", "w")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
