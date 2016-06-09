from flask import Flask, jsonify, render_template
from kjvbot_app import markovbot
from random import choice

app = Flask(__name__)

@app.route('/')
def start():
    verse = kjvbot()
    return render_template('index.html', verse=verse)

def kjvbot():
    w = ["the", "them", "thee", "him"]
    l = ["looked", "saw", "beheld", "heard"]
    x = [["Woe", "unto", choice(w), "kjv_prophets.txt"], 
         ["And", "the", "priest", "kjv.txt"], 
         ["And", "I", choice(l), "kjv_revelation.txt"], 
         ["Behold", ",", "I", "kjv.txt"], 
         ["And", "to", "the", "kjv.txt"], 
         ["And", "he", "answered", "kjv_gospels.txt"],
         ["In", "the", "beginning", "kjv.txt"]]
    
    [word1, word2, word3, fileid] = choice(x)
    
    utterance = markovbot.markovize(word1, word2, word3, fileid, char_limit=125)
    
    verse = '“' + utterance + '”'
      
    return verse

@app.route('/new_verse')
def get_new_verse():
    verse = kjvbot()
    return jsonify(verse=verse)

if __name__ == '__main__':
    app.run(debug=True)