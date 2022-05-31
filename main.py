import translator
import PySimpleGUI as gui

l = [[gui.Text("Pyg Latin Game")], 
     [gui.Input()],
     [gui.Text(size = (40, 1), key = '-OUTPUT-')],
     [gui.Button("OK")]]
window = gui.Window(title = "Hello World", layout = l, resizable = True)

while True:
  event, values = window.read()
  testWord = values[0]
  #testWord = input("Please enter a word: ")
  convertedWord = testWord.lower()
  wordArray = convertedWord.split(" ")
  #print (wordArray)

  # Creates the translator object to translate the inputted word(s)
  translatorObj = translator.Translator()

  if testWord.isalpha():
    # Determines which method to be utilized depending on the number of words present
    if (len(wordArray) > 1):
      window['-OUTPUT'].update("Translated Word: " + translatorObj.multiple_word_translate(wordArray))

    else:
      window['-OUTPUT-'].update("Translated Word: " + translatorObj.single_word_translate(testWord, convertedWord))

  else:
    window['-OUTPUT-'].update("Please type a word that does not include any numbers")
