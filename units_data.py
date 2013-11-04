prefix_dict = {
    'yotta':'1000000000000000000000000',
    'zetta':'1000000000000000000000',
    'exa':'1000000000000000000',
    'peta':'1000000000000000',
    'tera':'1000000000000',
    'giga':'1000000000',
    'mega':'1000000',
    'kilo':'1000',
    'hecto':'100',
    'deka':'10',
    'deci':'0.1',
    'centi':'0.01',
    'milli':'0.001',
    'micro':'0.000001',
    'nano':'0.000000001',
    'pico':'0.000000000001',
    'femto':'0.000000000000001',
    'atto':'0.000000000000000001',
    'zepto':'0.000000000000000000001',
    'yocto':'0.000000000000000000000001',
    }

name_prefix_dict = {
    'km':'kilometers',
    'cm':'centimeters'
}
units_dict = {
    'celsius':{
        'function':'standard',
        'invfunction':'standard',
        'dimension':'[temperature]',
        } ,
    'fahrenheit':{
        'function':'(fahrenheit - 32) * 5/9',
        'invfunction':'celsius * 9/5 + 32',
        'dimension':'[temperature]',
        },
    'kelvin':{
        'function':'kelvin - 273.15',
        'invfunction':'celsius + 273.15',
        'dimension':'[temperature]',
        },
    'rankine':{
        'function':'(rankine - 491.67) * 5/9',
        'invfunction':'(celsius + 273.15) * 9/5',
        'dimension':'[temperature]',
        },                                                    
    'meter':{
        'function':'standard',
        'invfunction':'standard',
        'dimension':'[length]',
        },
    'foot':{
        'function':'foot * 1/3.280839895',
        'invfunction':'meter * 3.280839895',
        'dimension':'[length]',
        },
    'inch':{
        'function':'inch * 1/39.3701',
        'invfunction':'meter * 39.3701',
        'dimension':'[length]',
        },
    'mile':{
        'function':'mile * 1609.34',
        'invfunction':'meter * 1/1609.34',
        'dimension':'[length]',
        },
    'marathon':{
        'function':'marathon * 42194.988',
        'invfunction':'meter * 1/42194.988',
        'dimension':'[length]',
        },
    'second':{
        'function':'standard',
        'invfunction':'standard',
        'dimension':'[time]',
    },
    'minute':{
        'function':'minute * 60',
        'invfunction':'second / 60',
        'dimension':'[time]',
    },
    'hour':{
        'function':'hour * 60 * 60',
        'invfunction':'second / (60*60)',
        'dimension':'[time]',
    },
    'day':{
        'function':'day * 60 * 60 * 24',
        'invfunction':'second / (60*60*24)',
        'dimension':'[time]',
    },
    'fortnight':{
        'function':'fortnight * 60 * 60 * 24 * 7',
        'invfunction':'second / (60*60*24*7)',
        'dimension':'[time]',
    },
    'cubic_meter': {
        'function': 'standard', 
        'invfunction': 'standard', 
        'dimension': '[length]^3',
    }, 
    'meters_per_second': {'function': 'standard', 'dimension': '[length]/[time]', 'invfunction': 'standard'},
    'miles_per_hour': {'invfunction': 'meters_per_second/0.44704', 'dimension': '[length]/[time]', 'function': 'miles_per_hour*0.44704'},
    'knot': {'invfunction': 'meters_per_second/0.514444444', 'dimension': '[length]/[time]', 'function': 'knot*0.514444444'},
    'miles_per_second': {'invfunction': 'meters_per_second/1609.0', 'dimension': '[length]/[time]', 'function': 'miles_per_second*1609.0'},
    'meters_per_hour': {'invfunction': 'meters_per_second/0.0002778', 'dimension': '[length]/[time]', 'function': 'meters_per_hour*0.0002778'},
    'feet_per_second': {'function': 'feet_per_second*0.3048', 'dimension': '[length]/[time]', 'invfunction': 'meters_per_second/0.3048'},

}
#include repeats, might also want to remove code that looks directly for the name above because it provides less control, just a thought
name_dict = {


    'c':'celsius',
    'celsius':'celsius',
    'f':'fahrenheit',
    'fahrenheit':'fahrenheit',
    'k':'kelvin',
    'kelvin':'kelvin',
    'ra':'rankine',
    'rankine':'rankine',
    'r':'rankine',

    'm':'meter',
    'meters':'meter',
    'meter':'meter',
    'meters':'meter',
    'metre':'meter',
    'metres':'meter',

    'ft':'foot',
    'feet':'foot',
    'foot':'foot',
    'in':'inch',
    'inches':'inch',
    'inch':'inch',

    
    'mi':'mile',
    'mile':'mile',
    'miles':'mile',
    'marathon':'marathon',
    'marathons':'marathon',
    #add klick here! :)
    's':'second',
    'seconds':'second',
    'second':'second',
    'sec':'second',
    'sc':'second',
    'fortnight':'fortnight',
    'fortnights':'fortnight',
    'mn':'minute',
    'min':'minute',
    'minute':'minute',
    'minutes':'minute',
    'hr':'hour',
    'hour':'hour',
    'hours':'hour',
    'day':'day',
    'days':'day',
    
    #added to make tests more accuratly reflect actual progress
    'grams':'grams',
    'stone':'stone',
    'stones':'stone',
    'acre':'acre',
    'acres':'acre',
    #(re add these correctly later!)

    ###new ones added
    'meters_per_second': 'meters_per_second',
    'miles_per_hour': 'miles_per_hour',
    'mph': 'miles_per_hour',
    'knot': 'knot',
    'knots': 'knot',
    'mi/s': 'miles_per_second',
    'miles_per_second': 'miles_per_second',
    'miles/second': 'miles_per_second',
    'm/hr': 'meters_per_hour',
    'meters_per_hour': 'meters_per_hour',
    'mi/hr':'miles_per_hour',
    'm/s':'meters_per_second',
    'ft/s': 'feet_per_second',
    'feet_per_second': 'feet_per_second',




}


multiword_name_dict = {

    ###new ones added
    'm per s': 'meters_per_second',     #these dont work very well, an advanced engine would work much better :)
    'm / s': 'meters_per_second',
    'meters/second':'meters_per_second',
    'meters / second':'meters_per_second',
    'm per sec': 'meters_per_second',
    'meters per second': 'meters_per_second',
    'metres per second': 'meters_per_second',
    
    'mi / hr':'miles_per_hour',
    'miles / hour':'miles_per_hour',
    'miles/hour':'miles_per_hour',
    'mile per hour': 'miles_per_hour',
    'miles per hour': 'miles_per_hour',
    'mi per hr': 'miles_per_hour',
    'mi / s': 'miles_per_second',
    'mile per second': 'miles_per_second',
    'miles / second': 'miles_per_second',
    'miles per second': 'miles_per_second',
    'meter per hour': 'meters_per_hour',
    'm / hr': 'meters_per_hour',
    'meters per hr': 'meters_per_hour',
    'meters per hour': 'meters_per_hour',
    'ft / s': 'feet_per_second',
    'feet per second': 'feet_per_second',
    'foot per second': 'feet_per_second',
}

unit_type_standards = {
    '[length]/[time]':'meters_per_second',
    '[length]':'meter',
    '[time]':'second',
}

