from units_data import *

#example inputs:
# [['345', 'feet/second'], 'meters/second']
# [['345', 'feet/second^2'], 'meters/second^2']
# [['10', 'C'], 'F']

#for testing a conversion of liner complexity is inputed

def get_formated_function(input_unit):
    conversion_function = units_dict[input_unit]['function']
    
    return conversion_function


def get_formated_invfunction(input_unit):
    invconversion_function = units_dict[input_unit]['invfunction']
    
    return invconversion_function


def simple_convert(input_simple):
    
    """runs a one directional conversion between the units it recieves in form [['10', 'C'], 'F']"""
    if not input_simple:
        return 0
    
    source_unit = input_simple[0][1].lower()
    source_value = input_simple[0][0]
    product_unit = input_simple[1].lower()
  
    if source_unit in name_prefix_dict:
        source_unit = name_prefix_dict[source_unit]
    for prefix in list(prefix_dict):
        if prefix in source_unit:
            if source_unit[len(prefix):] in units_dict:
                source_value = str(float(source_value) * float(prefix_dict[prefix]))
            if source_unit[len(prefix):] in name_dict:
                source_unit = name_dict[source_unit[len(prefix):]]
                source_value = str(float(source_value) * float(prefix_dict[prefix]))

    if product_unit in name_prefix_dict:
        product_unit = name_prefix_dict[product_unit]

    for prefix in list(prefix_dict):
        if prefix in product_unit:
            if product_unit[len(prefix):] in units_dict:
                source_value = str(float(source_value) / float(prefix_dict[prefix]))
            if product_unit[len(prefix):] in name_dict:
                product_unit = name_dict[product_unit[len(prefix):]]
                source_value = str(float(source_value) / float(prefix_dict[prefix]))

    if source_unit in units_dict:
        source_unit_function = units_dict[source_unit]['function']
    if source_unit in name_dict:
        source_unit = name_dict[source_unit]
        source_unit_function = units_dict[source_unit]['function']

    print(product_unit)
    if product_unit in units_dict:
        product_unit_invfunction = units_dict[product_unit]['invfunction']
    if product_unit in name_dict:
        product_unit = name_dict[product_unit]
        product_unit_invfunction = units_dict[product_unit]['invfunction']

    print(source_unit, source_value, product_unit)
    
    #check if source and prodcut are the same unit
    if source_unit == product_unit:
        return source_value, source_unit
    
    #check dimension compatibility
    if units_dict[source_unit]['dimension'] != units_dict[product_unit]['dimension']:
        return 'incompatable dimensions'
    
    #input unit is not standard
    if source_unit_function != 'standard':
        conversion_numarical_expression = get_formated_function(source_unit).replace(source_unit, source_value)
        median_value = eval(conversion_numarical_expression)
    #input unit is standard, return result
    elif source_unit_function == 'standard':
        conversion_numarical_expression = get_formated_invfunction(product_unit).replace(source_unit, source_value)
        product_value = eval(conversion_numarical_expression)
        return product_value, product_unit

    #if unit is standard return median_value
    if units_dict[product_unit]['function'] == 'standard':
        return median_value, product_unit

    #convert median value to prodcut_unit if not standard
    else:
        type_standard = unit_type_standards[units_dict[source_unit]['dimension']]
        conversion_numarical_expression_second = get_formated_invfunction(product_unit).replace(type_standard, str(median_value))
        product_value = eval(conversion_numarical_expression_second)
        return product_value, product_unit

