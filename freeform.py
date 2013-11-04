##if you ever really want this program to work properly you will have to use nltc


import string
from units_data import *
import re


def detect_si_prefix(word):
    "decides if a word in has a st prefix, returns 0 or multipliter"
    for prefix in list(prefix_dict):
        if prefix in word:
            possible_unit = word[len(prefix):]
            if possible_unit in name_dict:
                return float(prefix_dict[prefix])
    return 0

def standardize_numbers(list_words):
    "converts numbers in exp form to regular form"
    return_list = []
    for word_orig in list_words:
        word = word_orig.lower()
        if 'e' in word:
            word = word.replace('e', '**')
        if '^' in word:
            word = word.replace('^', '**')
        try:
            result = str(float(eval(word)))
        except:
            result = word_orig
        return_list.append(result)
    return return_list
    
def seperate(text):
    """Seperates numbers and units given together and punctuation, returns word list."""
    text = text.replace("(", "")
    text = text.replace(")", "")
    previous = ''
    working_text = ''
    for char in text:
        if previous in '0123456789-.':
            if char not in '0123456789-. )^*Ee':
                working_text = working_text + " "                   
        if previous in string.ascii_letters:
            if char in "?.,!":
                working_text = working_text + " "
        working_text = working_text + char
        previous = char
    word_list = working_text.split()
    ##known bug if input "10engergies or 10Energies to x"  does not split 10energies"
    return word_list

def analyze(text):
    text = text.lower()
    for unit in multiword_name_dict:
        if unit in text:
            if unit + "s" in text:
                text = text.replace(unit+"s", multiword_name_dict[unit], 1)
            else:
                text = text.replace(unit, multiword_name_dict[unit], 1)
            
    word_list = seperate(text)
    """Decides the meaning of each term, return metadata list."""
    word_list = standardize_numbers(word_list)
    output_str = ''
    for item in word_list:
        item_info = []
        ided = False
        if item in name_dict or (item[-1] == 's' and item[:-1] in name_dict) or item in units_dict or (item[-1] == 's' and item[:-1] in units_dict):
            item_info.append('unit')
            ided = True
        if item in ['?','.',',']:
            item_info.append('punctuation')
            ided = True
        if item in ['convert', 'converted', 'from', 'what', 'is', 'in', 'how', 'many', 'much','conversion','measured', 'degrees']:#maybe degrees shouln't be in here
            item_info.append('phrasing word')
            ided = True
        if item == 'per':
            item_info.append('per')
            ided = True
        if item == 'to':
            item_info.append('to')
            ided = True
        if item in ['a', 'an', 'one']:
            item_info.append('singlar')
            ided = True
        if item in list(prefix_dict):
            item_info.append('prefix')
            ided = True
        try:
            float(item)
            item_info.append('number')
            ided = True
        except: pass
        #tests for units if they are together
        if '/' in item:
            temp = item.split("/")
            units_count = 0
            for unit in temp:
                if unit in name_dict:
                    units_count += 1
            if units_count >= 2:
                item_info.append('complex unit')
                ided = True
        if detect_si_prefix(item) or item in name_prefix_dict:
                item_info.append('unit')
                ided = True
        if not ided:
            item_info.append('unknown')
        output_str = output_str + str(item_info)+";"

    output_str = output_str.replace("'", "")
    output_str = output_str[0:len(output_str)-1]
    
    return output_str, word_list

def format_q(query):
    contents_metadata_string = query['analyze_str'].replace(";","")
    contents_metadata_list = query['analyze_str'].split(";")
    contents_data_list = query['seperate_list']

    location_possible_complex_units = []
    if "[unit][per][unit]" in contents_metadata_string:
        for n in range(0, len(contents_metadata_list)-2):
            if contents_metadata_list[n] == "[unit]" and contents_metadata_list[n+1] == "[per]" and contents_metadata_list[n+2] =="[unit]":
                location_possible_complex_units.append(n)

    if location_possible_complex_units:
        #print("Places where there is a possible complex unit:", location_possible_complex_units)
        pass
    

    #print("List:", contents_metadata_list)
    #print("String:", contents_metadata_string)
    
    count_numbers = contents_metadata_list.count("[number]")
    count_units = contents_metadata_list.count("[unit]") + contents_metadata_list.count("[complex unit]") #does not include [unit, phrasing word]
    count_unitorphrasing = contents_metadata_list.count("[unit, phrasing word]")

    contains_in = False
    for item in contents_metadata_list:
        if item.count(",") != 0:
            contains_in = True

    contains_a = False
    if '[singlar]' in contents_metadata_list:
        contains_a = True

    contains_to = False
    if '[to]' in contents_metadata_list:
        contains_to = True

    contains_prefix = False
    if '[prefix]' in contents_metadata_list:
        contains_prefix = True

    contains_complex_units = False
    if '[complex unit]' in contents_metadata_list:
        contains_complex_units = True
            
    #print("contains in:", contains_in)
    #print("Contains singularity:", contains_a)
    #print("Number count:", count_numbers)
    #print("Unit count:", count_units)
    #print("Count [unit, phrasing word]", count_unitorphrasing)

    def unit_name_std(psuedo_comp):
        try:
            psuedo_comp[0][1] = name_dict[psuedo_comp[0][1].lower()]
            psuedo_comp[1] = name_dict[psuedo_comp[1].lower()]
            return psuedo_comp
        except KeyError:
            return psuedo_comp

    def return_info(regex, meta_string, data_list):
        def string_to_list_position(string, l_start):
            """Counts [ in a string which reps a list and returns the list position of that item"""
            b_count = 0
            a = 0
            for letter in string:
                if a > l_start:
                    break
                a += 1
                if letter == '[':
                    b_count+=1
            return b_count-1
                    
        regex_comp = re.compile(regex)
        for m in regex_comp.finditer(meta_string):
            if m.group():
                try:
                    #print('number:', m.start('number'), m.end('number'), 'unit1:', m.start('uone'), m.end('uone'), 'unit2:', m.start('utwo'), m.end('utwo'), m.group('number','uone','utwo'))
                    #print("number spot:", string_to_list_position(meta_string, m.start('number')))


                    res_number = data_list[string_to_list_position(meta_string, m.start('number'))]
                except IndexError:
                    res_number = '1.0'

                #print("start uspot:", string_to_list_position(meta_string, m.start('uone')))
                #print("end unispot:", string_to_list_position(meta_string, m.start('utwo')))
                res_bunit = data_list[string_to_list_position(meta_string, m.start('uone'))]
                res_funit = data_list[string_to_list_position(meta_string, m.start('utwo'))]
        try:              
            return unit_name_std([[res_number, res_bunit], res_funit])
        except:
            return 0
        
    ided = False
    
    if count_numbers == 1 and not contains_complex_units:
        if count_units == 2:
            #if not contains_in:
            if not contains_prefix:
                ided = True
                #print("this one is easy")
                # possible regex  ((?P<utwo>\[unit.*?\]).*(?P<number>\[number\])(?P<uone>\[unit.*?\]))?
                # and the reverse ((?P<number>\[number\])(?P<uone>\[unit.*?\]).*(?P<utwo>\[unit.*?\]))?"
                result_try = return_info(r"((?P<utwo>\[unit.*?\]).*(?P<number>\[number\]).*?(?P<uone>\[unit.*?\]))?", contents_metadata_string, contents_data_list)
                if result_try:
                    return result_try
                return return_info(r"((?P<number>\[number\]).*?(?P<uone>\[unit.*?\]).*(?P<utwo>\[unit.*?\]))?", contents_metadata_string, contents_data_list)
            if contains_prefix:
                #print("contains prefix, needs some modifications")
                #need to think about a way of solving this!!
                pass
            """
            if contains_in:
                ided = True
                
                result_try = return_info(r"((?P<utwo>\[unit.*?\]).*(?P<number>\[number\])(?P<uone>\[unit.*?\]))?", contents_metadata_string, contents_data_list)
                if result_try:
                    return result_try
                return return_info(r"((?P<number>\[number\])(?P<uone>\[unit.*?\]).*(?P<utwo>\[unit.*?\]))?", contents_metadata_string, contents_data_list)
            
                #should be same as above
                #print("this one is just as easy, we are just being carfull")
"""
        if count_units == 1:
            if contains_in:
                ided = True

                #(\[number\]\[unit.*?\].*?\[unit.*?\])?

                #print("this one we know how to do")
                result_try = return_info(r"((?P<utwo>\[unit.*?\]).*(?P<number>\[number\]).*?(?P<uone>\[unit.*?\]))?", contents_metadata_string, contents_data_list)
                if result_try:
                    return result_try
                return return_info(r"((?P<number>\[number\]).*?(?P<uone>\[unit.*?\]).*(?P<utwo>\[unit.*?\]))?", contents_metadata_string, contents_data_list)

            if not contains_in:
                ided = True
                #print("not sure how to handle this input/ or if it would ever happen in a vaild input")

    if count_numbers == 0 and not contains_complex_units:
        if count_units == 1:
            if count_unitorphrasing == 1:
                ided = True

                #print("how many in per foot?, we got this kind")
                #((?P<uone>\[unit.*?\]).*?per.*?(?P<utwo>\[unit.*?\]))?

                return return_info(r"((?P<utwo>\[unit.*?\]).*?\[per\].*?(?P<uone>\[unit.*?\]))?", contents_metadata_string, contents_data_list)
                
            if count_unitorphrasing == 2:
                ided = True
                #(\[unit.*?\].*?\[singlar\].*?\[unit.*?\])?
                #print("how many in in a foot?, we can do this one too")
                return return_info(r"((?P<utwo>\[unit.*?\]).*?\[singlar\].*?(?P<uone>\[unit.*?\]))?", contents_metadata_string, contents_data_list)
        if count_units == 2:
            
            if not contains_in and not contains_to:
                ided = True
                #\[unit.*?\].*?\[per\].*?\[unit.*?\])?
                #print("and in format unit per unit, very easy solve")
                return return_info(r"((?P<utwo>\[unit.*?\]).*?\[per\].*?(?P<uone>\[unit.*?\]))?", contents_metadata_string, contents_data_list)
            if contains_in:
                if contains_a:
                    ided = True
                    #(\[unit.*?\].*?\[singlar\].*?\[unit.*?\])?
                    #print("can be done :)")
                    result_try = return_info(r"(\[singlar\](?P<uone>\[unit.*?\]).*(?P<utwo>\[unit.*?\]))?", contents_metadata_string, contents_data_list)
                    if result_try:
                        return result_try
                    return return_info(r"((?P<utwo>\[unit.*?\]).*?\[singlar\].*?(?P<uone>\[unit.*?\]))?", contents_metadata_string, contents_data_list)
            
            if contains_to:
                ited = True

                return return_info(r"((?P<uone>\[unit.*?\]).*?\[to\].*?(?P<utwo>\[unit.*?\]))?", contents_metadata_string, contents_data_list)
            #not sure if this is safe, lets see if it causes problems
            return return_info(r"((?P<uone>\[unit.*?\]).*(?P<utwo>\[unit.*?\]))?", contents_metadata_string, contents_data_list)

    if location_possible_complex_units or contains_complex_units and not ided:
        ided = True #temp
        #print("It contains complex units, and can be evaled here")

    if not ided:
        #print("This one is weird and needs a further look!-------------------------------------------------------ERRRORROROORORO")
        pass

    return 0 #end of def format

    
            
        
"""
a = [1, [2,3], 2]
for x in a:
    if x == 2:
    print(True)
    
	try:
		print(2 in x)
	except: pass
	"""
