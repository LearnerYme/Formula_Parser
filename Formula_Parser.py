r'''
Formula Parser
by yghuang
April 24th, 2021

Announcement

This code is only a 'translator' for Yu Zhang's C++ code. 
Which can translate those very comlex formula in his code into the simple form for Calculator.AdaptiveQuickSum method.
It is not quite a big project, however, I've learned a lot while I wrote this parser any way.

Useage:
```
from Formula_Parser import FormulaParser
fp = FormulaParser()
formula = 'your_formula'
fp.ReadFormula(formula)
fp.Tokenize()
fp.OpenBracket()
fp.Translate()
print(fp.output)
```

then, you can see a very long string that can be copied & pasted into Calculator.AdaptiveQuickSum.

Any way, this program might be used only by myself. :)
'''

class Token():
    def __init__(self, value, kind):
        if kind not in ['Term', 'Power', 'Start', 'End', 'Coe', 'Add', 'Sub', 'Mul']:
            raise Exception('Invalid Token.')
        self.value = value
        self.kind = kind
        return
    
    def __str__(self):
        return '{} Token, value = {}'.format(self.kind, self.value)

class FormulaParser():
    def __init__(self):
        self.text = ''
        self.output = '('
        self.textlength = 0
        self.cursor = 0
        self.tokens = []
        self.tokens_openBrac = []
        return
    
    #===========================read the formula (character stream)
    def ReadFormula(self, text):
        r'''
        This method will load a character stream from a string (text).
        '''
        assert(type(text) is str)
        self.text = text.replace(' ', '')
        self.text = self.text.replace('pow', 'p')
        self.textlength = len(self.text)
        self.cursor = 0
        return    
    
    
    #===========================tokenize and methods needed, translate character stream into token stream 
    def Tokenize(self):
        r'''
        This method will translate the character stream (self.text) into token stream (self.tokens).
        '''
        while(self.cursor < self.textlength):
            c = self.PeekChar()
            if c == '(':
                self.tokens.append(self.GetStartToken())
            elif c == ')':
                self.tokens.append(self.GetEndToken())
            elif c == 'v':
                self.tokens.append(self.GetTermToken())
            elif c == 'p':
                self.tokens.append(self.GetPowerToken())
            elif c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                self.tokens.append(self.GetCoeToken())
            elif c == '+':
                self.tokens.append(self.GetAddToken())
            elif c == '-':
                self.tokens.append(self.GetSubToken())
            elif c == '*':
                self.tokens.append(self.GetMulToken())
            else:
                return
        
    def GetChar(self):
        r'''
        Return current character and move on the cursor.
        '''
        c = self.text[self.cursor]
        self.cursor += 1
        return c
    
    def PeekChar(self):
        r'''
        Check current character.
        '''
        if self.cursor < self.textlength:
            return self.text[self.cursor]
        else:
            return False
    
    def GetTermToken(self):
        c = self.GetChar()
        term = ''
        while(True):
            c = self.GetChar()
            if c == '[':
                continue
            elif c == ']':
                return Token(term, 'Term')
            elif c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                term += c
            else:
                raise Exception('GetTermToken met an error: invalid char "{}".'.format(c))    
    
    def GetPowerToken(self):
        c = self.GetChar()
        power = ''
        while(True):
            c = self.GetChar()
            if c == '(':
                continue
            elif c == 'v':
                term = self.GetTermToken()
            elif c == ',':
                continue
            elif c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                if self.PeekChar() == ')':
                    power += c
                    power = int(power)
                    self.GetChar()
                    return Token((term.value, power), 'Power')
                else:
                    power += c
            else:
                raise Exception('GetPowerToken met an error: invalid char "{}".'.format(c))
                
    def GetStartToken(self):
        c = self.GetChar()
        if c == '(':
            return Token('', 'Start')
        else:
            raise Exception('GetStartToken met an error: invalid char "{}".'.format(c))
            
    def GetEndToken(self):
        c = self.GetChar()
        if c == ')':
            return Token('', 'End')
        else:
            raise Exception('GetEndToken met an error: invalid char "{}".'.format(c))
            
    def GetCoeToken(self):
        coe = ''
        while(True):
            c = self.PeekChar()
            if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                c = self.GetChar()
                coe += c
            elif c == '*':
                coe = int(coe)
                return Token(coe, 'Coe')
                     
    def GetAddToken(self):
        c = self.GetChar()
        if c == '+':
            return Token('', 'Add')
        else:
            raise Exception('GetAddToken met an error: invalid char "{}".'.format(c))

    def GetSubToken(self):
        c = self.GetChar()
        if c == '-':
            return Token('', 'Sub')
        else:
            raise Exception('GetSubToken met an error: invalid char "{}".'.format(c))
            
    def GetMulToken(self):
        c = self.GetChar()
        if c == '*':
            return Token('', 'Mul')
        else:
            raise Exception('GetMulToken met an error: invalid char "{}".'.format(c))

    #===========================open the bracket and derive such form: Coe*Power*Power*... + Coe*Power*... + ... 
    def OpenBracket(self):
        r'''
        Multiple the coefficient into the bracket. Return another token stream.
        After this, the new token stream will only have 'Coe', 'Add' and 'Power' tokens.
        '''
        currentCoe = 1
        innerCoe = 1
        inBracket = False
        isolateCoe = True
        tokens_openBrac = []
        self.tokens_openBrac = []
        for item in self.tokens:
            k = item.kind
            if inBracket:
                if k == 'Sub':
                    innerCoe = -1
                    tokens_openBrac.append(Token('', 'Add'))
                    isolateCoe = True
                elif k == 'Add':
                    innerCoe = 1
                    tokens_openBrac.append(Token('', 'Add'))
                    isolateCoe = True
                elif k == 'Coe':
                    innerCoe *= item.value
                    isolateCoe = True
                elif k == 'Term':
                    if isolateCoe:
                        #if there are multi-terms with the same coefficient, only one coe. token will be added.
                        tokens_openBrac.append(Token(innerCoe*currentCoe, 'Coe'))
                        isolateCoe = False
                    tokens_openBrac.append(Token((item.value, 1), 'Power'))
                elif k == 'Power':
                    if isolateCoe:
                        tokens_openBrac.append(Token(innerCoe*currentCoe, 'Coe'))
                        isolateCoe = False
                    tokens_openBrac.append(Token(item.value, 'Power'))
                elif k == 'End':
                    inBracket = False
                    isolateCoe = True
                    currentCoe = 1
            else:
                if k == 'Sub':
                    currentCoe *= -1
                    tokens_openBrac.append(Token('', 'Add'))
                elif k == 'Add':
                    currentCoe *= 1
                    tokens_openBrac.append(Token('', 'Add'))                   
                elif k == 'Coe':
                    currentCoe *= item.value
                elif k == 'Start':
                    inBracket = True
                elif k == 'Term':
                    tokens_openBrac.append(Token((item.value, 1), 'Power'))
                elif k == 'Power':
                    tokens_openBrac.append(Token(item.value, 'Power'))
        #delete double Adds
        cur = 'Start'
        for item in tokens_openBrac:
            new = item.kind
            if new == 'Add' and cur == 'Add':
                continue
            else:
                self.tokens_openBrac.append(item)
            cur = item.kind
        return
    
    #===========================translate the new token stream into Calculator.AdaptiveQuickSum (iterm, ..., coe, power, ...)
    def Translate(self):
        r'''
        As the tokens_openBrac show such list [coe, power, power, add, coe, ...].
        Splite by 'Add' tokens, and derive several terms (iterm1, ..., coe, power1, ...).
        Form a long string.
        '''
        tmpList = []
        resultList = []
        for item in self.tokens_openBrac:
            k = item.kind
            if k == 'Add':
                resultList.append(self.FormOneTuple(tmpList))
                tmpList = []
            else:
                tmpList.append(item)
        resultList.append(self.FormOneTuple(tmpList))
        #from the resultList, form the string we need
        for item in resultList:
            self.output += item
            self.output += ', '
        self.output = self.output.rstrip(', ')
        self.output += ')'
        return
            
    def FormOneTuple(self, tmpList):
        r'''
        Using a list of tokens, form a tuple (as a string).
        Note that the list is gotten from the spltings from 'Add' tokens.
        The list has such elements: [coe, power1, power2, ...]
        '''
        text = '('
        coe = tmpList.pop(0).value
        termList = []
        powerList = []
        for item in tmpList:
            tmpTerm, tmpPower = item.value
            #Note that the value[0] is string and value[1] is int.
            termList.append(tmpTerm)
            powerList.append(tmpPower)
        for item in termList:
            text += item
            text += ', '
        text += str(coe)
        text += ', '
        for item in powerList:
            text += str(item)
            text += ', '
        text = text.rstrip(', ')
        text += ')'
        return text
        
