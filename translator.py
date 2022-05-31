class Translator:

  # Translates a single inputted word according to PygLatin rules
  def single_word_translate(self, testWord, convertedWord):

    if convertedWord.find("a", 0, 1) != -1 or convertedWord.find("e", 0, 1) != -1 or convertedWord.find('i', 0, 1) != -1 or convertedWord.find('o', 0, 1) != -1 or convertedWord.find("u", 0, 1) != -1:
      return (testWord + '-yay')

    elif convertedWord.find('y', 0, 1) != -1:
      return (testWord[1:] + '-yay')

    else:
      ending = '-' + convertedWord[0] + 'ay'
      return (testWord[1:] + ending)

  # Translates multiple words according to PygLatin rules
  def multiple_word_translate(self, wordArray):
  
    outputString = ''
    for w in wordArray:  
      if w.find("a", 0, 1) != -1 or w.find("e", 0, 1) != -1 or w.find('i', 0, 1) != -1 or w.find('o', 0, 1) != -1 or w.find("u", 0, 1) != -1:
        outputString += w + '-yay '

      elif w.find('y', 0, 1) != -1:
        outputString += w[1:] + '-yay '

      else:
        outputString += w[1:] + '-' + w[0] + 'ay '

    return(outputString)