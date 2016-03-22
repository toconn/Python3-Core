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

def index_after (text, search_text, start_index = 0):
    '''Find the index location just after search text
       Not found returns -1
    '''
    
    # Find search text:
    find_index = text.find(search_text, start_index)
    
    if find_index > -1:
        # Move indet to after search text:
        find_index = find_index + len(search_text)
        
    return find_index

    
#////////////////////////////////////////////
#// Returns Indented String List
#////////////////////////////////////////////

def indent_list (strings, indent):
    
    return [indent + item for item in strings]

