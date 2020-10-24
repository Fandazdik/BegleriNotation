# BegleriNotation
An applet to convert a custom Begleri notation into easy to read text

Note: PySimpleGUI is required

# Notation
The notation can be found in the .py file, but is included here for reference:
```python
dict_symbols = {
    'x' : 'hold',
    'o' : 'open',
    '~' : 'throw around',
    '.' : 'to',
    '|' : 'hangs from',
    'b1' : 'ball one',
    'b2' : 'ball two',
    'Hb' : 'the back of the hand',
    'Hf' : 'the front of the hand',
    'Hv' :'bottom of hand',
    'H^' : 'top of hand',
    'Hb^' : 'the top of the back of the hand',
    'Hbv' : 'the bottom of the back of the hand',
    'Hf^' : 'the top of the front of the hand',
    'Hfv' : 'the bottom of the front of the hand',
    '7' : 'palm',
    '1' : 'thumb',
    '2' : 'index',
    '3' : 'middle',
    '4' : 'ring',
    '5' : 'pinkie',
    '&' : 'and',
    '=' : 'while',
    '' : '',
    ';' : '\n',
    '*' : 'wait until',
    'stloop' : 'Loop begins here:',
    'endloop' : 'Loop ends here',
    'swap' : 'Repeat with ball 1 and ball 2 swapped'
    }
 ```
 
 # begleri.txt
Enter in the notation formatted like so:
```
start Name_Of_Move
[foo:bar:baz]
end
start Another_Move_Here
[more:instructions:here]
end
```

There are some example moves included.
