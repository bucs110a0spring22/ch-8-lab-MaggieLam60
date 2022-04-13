#Part A
class StringUtility:
  
  
  def __init__(self, string):
    self.string=string
  '''
  general function description= is the init function
	args: self and string
	return: nothing, init
  
  '''
  def __str__(self):
    return self.string
  '''
  general function description= is the str function
	args: self 
	return: self.string
  
  '''
    
#Part B

  def vowels(self):
    '''
    general function description= returns the # of vowels less than 5
	args: (type) description= self
	return: (type) description= returns many and # of vowels
    '''
    vowels= ['a','e','o','i','u']
    number_of_vowels = 0
    for character in self.string:
      if character in vowels:
        number_of_vowels += 1  
    if number_of_vowels >= 5:
        return ("many")
    else: 
        return str(number_of_vowels)
  
  def bothEnds(self):
    '''
    general function description= adds the first and last 2 letters
	args: (type) description= self
	return: (type) description= returns '' and first and last 2 letters of word
    
    '''
    if len(self.string) <= 2:
      return "" 
    else:
      return self.string[0] + self.string[1] + self.string[-2] + self.string[-1]
        
  def fixStart(self):
    '''
    general function description= replaces char of 1st letter with *
	args: (type) description: self 
	return: (type) description: new string or self if less than 1
    '''
    if len(self.string) <= 1:
      return self.string
      
    firstletter = self.string[0]
    new_string = firstletter 
    
    for index in range(1,len(self.string)):
      if self.string[index] == firstletter:
        new_string+= '*'
      else:
        new_string += self.string[index]
        
    return new_string

  def asciiSum(self):
    '''
    general function description= adds the sum of the char
	args: (type) description= self
	return: (type) description= returns the sum of the char
    '''
    sum = 0
    for char in self.string:
      sum += ord(char)
    return sum
    
  def cipher(self):
    length = len(self.string)
    newString = ''
    for x in self.string:
        if(x.isalpha()):
            if( (ord(x) >= 97 and ord(x) <= 122) and (ord(x)+length > 122)  ):
                newString += chr( 96 + ((ord(x)+length)%122) )
            elif ( (ord(x) >= 65 and ord(x) <= 90) and (ord(x)+length > 90)  ):
                newString += chr( 64 + ((ord(x)+length)%90) )
            else:
                newString += chr((ord(x)+length)) 
        else:
            newString += x;
    return newString
    
    
  '''
  general function description= changes the letter in alphebetical order by the number of total 
	args: (type) description= self
	return: (type) description = returns new string made
'''
  