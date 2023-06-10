from deep_translator import MyMemoryTranslator

def english_to_french(english_text): 
    '''translate from franch to engish '''
    #write the code here
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    print(french_text) # print the output
    return french_text # return the french txt

def french_to_english(french_text): 
    ''' translate from franch to english '''
    #write the code here
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    print(english_text)
    return english_text

