import demjson

json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
text = demjson.decode(json)
print (text)

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json = demjson.encode(data)
print (json)

open_cmd = input('Πατήστε enter για να εξέλθετε\n')
