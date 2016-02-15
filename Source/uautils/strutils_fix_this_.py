#////////////////////////////////////////////
#// Returns the text before the search string
#// Or returns the whole string if not found.
#////////////////////////////////////////////

def before (text, subtext):
    
    index = text.find (subtext)
    
    if (index > -1): 
        return text [:index]
    else:
        return text


#////////////////////////////////////////////
#// Returns substring info
#////////////////////////////////////////////

def findSubstringList (text, searchStartIndex, startText, endText):
    
    # Returns information a about a section of text.
    # Searches beginning at startIndex.
    # Searches for text between startText and endText
    
    # returns starting position, length, end position + 1, text.
    
    textActual = None
    textIndex  = -1
    endIndex   = -1
    nextIndex  = -1
    
    startIndex = text.find (startText, searchStartIndex)
    
    if startIndex > -1:
        
        endIndex = text.find (endText, startIndex)
    
        if endIndex > -1:
            
            textIndex  = startIndex + len (startText)
            textActual = text [textIndex: endIndex]
            nextIndex  = endIndex + len (endText)
    
    stringInfoList = [startIndex, textIndex, nextIndex, textActual]
    
    return stringInfoList


#////////////////////////////////////////////
#// Returns the location after the string
#////////////////////////////////////////////

def findAfter (text, searchText, startIndex = 0):
    
    findValue = text.find (searchText, startIndex)
    
    if findValue > -1:
        
        findValue = findValue + len (searchText)
        
    return findValue

    
#////////////////////////////////////////////
#// Returns Indented String List
#////////////////////////////////////////////

def indentStringList (stringList, indent):
    
    indentList = []
    
    for item in stringList:
        
        indentList.append (indent + item)
        
    return indentList



#////////////////////////////////////////////
#// Safe replace
#////////////////////////////////////////////

def replace (text, searchText, replaceText):
    
    if (text is not None):
        if (isinstance (replaceText, int)):    
            text = text.replace (searchText, str (replaceText))
        else:
            text = text.replace (searchText, replaceText)
    # Else
        # Return text.
    
    return text


#////////////////////////////////////////////
#// Sort a string list (case insensitive).
#////////////////////////////////////////////

def sortStringList (stringList):

    stringList.sort (key=str.lower)


#////////////////////////////////////////////
#// Returns a stripped or empty string.
#////////////////////////////////////////////

def stripString (text):

    if text:

        return text.strip()

    return ''


#////////////////////////////////////////////
#// Return a list of non empty tokens
#////////////////////////////////////////////

def tokenizeList (text, splitText):

    tokenList = text.split (splitText)

    tokenListClean = []

    for tokenItem in tokenList:

        if tokenItem != '':

            tokenListClean.append (tokenItem)

    return tokenListClean
