# Formula Parser

#### A formula parser for cumulant calculation.

This code is only a 'translator' for Yu Zhang's C++ code. 

Which can translate those very comlex formula in his code into the simple form for my Calculator.AdaptiveQuickSum method.

It is not quite a big project, however, I've learned a lot while I wrote this parser any way.

This program might not be able to be called a 'parser', however, there is a very simple tokenizer in it at least. :)

#### Useage:

```python3
from Formula_Parser import FormulaParser
fp = FormulaParser()
formula = 'your_formula'
fp.ReadFormula(formula)
fp.Tokenize()
fp.OpenBracket()
fp.Translate()
print(fp.output)
```