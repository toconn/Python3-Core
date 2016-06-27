import re

def strip_tags(text):
    ''' Null safe tag remover.
        Converts 'text <tag>text</tag> text<br/>' to 'text text text'
    '''
    
    if text:
        return re.sub('<[^<]+?>', '', text)
    else:
        return text
