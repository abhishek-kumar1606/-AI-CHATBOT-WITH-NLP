#import the libraries
import nltk
from nltk.chat.util import Chat, reflections
import sys

print("Welcome to chatbot \n how can i help you..... ")
pairs=[
    ['my name is(.*)',['hii,%1']],
    ['(hii|hello|hola)',['hey','hii buddy','how are you']],
    ['(.)in(.)is fun',['%1 in %2 is indeed fun']],
    ['(.*)your name',['My name is S.N.O.W']],
    ['(.*)created you?',['Abhishek yadav created me....']],
    ['(.*)(location|city)',['Bihar madhubani']],
    ['how is weather in(.*)?',['The weather is amazing...']],
    ['(.*)help(.*)',['I can help you']]
]

reflections

my_dummy_reflections={
    'go': 'gone' ,
    'hello': 'hey, there'
}

chat=Chat(pairs,my_dummy_reflections)
chat.converse()
