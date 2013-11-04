from __future__ import print_function
import freeform
import conversion
import time

#this has been ported to python2.7 not sure if works on 2.6

def convert(orig_input_string):
    start_time = time.time()
    query = {}
    query['error'] = None
    query['input_string'] = orig_input_string
    
    results = freeform.analyze(orig_input_string)
    query['analyze_str'] = results[0]
    query['seperate_list'] = results[1]
    query['computable_format'] = freeform.format_q(query)
    try:
        query['result'] = conversion.simple_convert(query['computable_format'])
    except Exception,e:
        query['error'] = e

    query['time'] = time.time()-start_time
    return query

def main():
    print("Free form unit conversion.  Type 'exit' to quit.")
    print("(c) David Kircos 2013")
    while True:
        print(">>", end='')
        i = raw_input()
        if i == 'exit':
            break
        print(convert(i))

if __name__ == '__main__':
    main()