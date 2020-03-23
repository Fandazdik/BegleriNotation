import PySimpleGUI as sg

#Seperate values at : char into list
#Input:  ["'x:b1:712:', 'o:b1:712:'"]
#Output: ["'x", 'b1', '712', "', 'o", 'b1', '712', "'"]
def obfuscate(instruction_list):
    complete_list = []
    obfus_list = []
    instruction = ''
    
    #iterate through each instruction block in list
    for list_pos in range(len(instruction_list)):
        
        #iterate through each char in instruction block
        for symbol in instruction_list[list_pos]:

            if symbol != ':':
                instruction += symbol
            else:
                obfus_list.append(instruction)
                instruction = ''
                
        obfus_list.append(instruction)
        
    return obfus_list


#Separates input at [] and puts results into list
#Input: '[x:b1:712:][o:b1:712:]'
#Output: "['x:b1:712:', 'o:b1:712:']"
def separate(code):
    #init
    instruction_list = []
    get_loop_open = ''
    
    current_instruction = ''
    for n in code:
        if n == '[' :
            get_loop_open = True
            
        elif n == ']':
            get_loop_open = False
            instruction_list.append(current_instruction)
            current_instruction = ''
            
        elif get_loop_open == True:
            current_instruction += n

    return instruction_list

#Just a function to check if input is int type
#Input: 123
#Output:True
def isnum(text):
    
    try:
        if int(text) == str(text):
            return True
    except:
        return False
    
#Instructions to words
#Input: ['b1', 'x', 'Hb']
#Output:['ball one', 'hold', 'the back of the hand']
def verbose(obf):
    
    instructions = []
    for var in obf:
        #input(var)
        if isnum(var) == False:
            instructions.append(dict_symbols[var])
#            input(instructions)
        else:
            #if instructions refer to finger numbers
            finger_list = []
            for digit in var:
                #input(digit)
                finger_list.append(dict_symbols[digit])
                #input(finger_list)
            if len(var) != 1:
                fingers = ', '.join(finger_list[:-1])
                fingers += ', and ' + finger_list[-1]
                fingers = 'in ' + fingers
            #input(fingers)
            else:
                fingers = ''.join(finger_list)
                fingers = 'in ' + fingers
            instructions.append(fingers)
                
    return instructions


def conv(input_instr):

    instruction_list = []
    
    list_inst = separate(input_instr)

    instr = obfuscate(list_inst)
     
    text = verbose(instr)

    text = ' '.join(text)

    return text

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

test_instruction = '[x:b2:45:][&:][x:b1:23:]'


f = open('begleri.txt', 'r')
data = f.readlines()
#input(data)

move_names = {}
move_list = []
instruction_text = ''

for line in data:
    if line[0:6] == 'start ':
        name = line[6:-1]
    elif line[:3] == 'end':
        move_names[name] = "\n".join(move_list)
        move_list = []
    else:
        move_list.append(conv(line[0:-1]))
    
names = (list(move_names.keys()))
methods = list(move_names.values())

layout = [
    [sg.InputOptionMenu((names), key='__move__')],
    [sg.Multiline(default_text='Instructions Here', size=(70, 10), key='__instructions__')],
    [sg.Submit(), sg.Cancel()]
]
event = ''
window = sg.Window('Begleri', layout, return_keyboard_events = True)

#display window
while not(event is None):
    event, values = window.read()
    if event == 'Cancel' or event == None:
        window.close()
        break
    values_name = values['__move__']
    values_method = move_names[values_name]
    window['__instructions__'].update(values_method)