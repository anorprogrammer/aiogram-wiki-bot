import wikipedia
from wikipedia import summary
wikipedia.set_lang("uz")

def wiki_result(message):
    result = summary(str(message))
    return result
