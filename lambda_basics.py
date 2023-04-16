import json

def sum(a,b):
    return a+b
    
def lambda_handler(event, context):
    m = event['m']
    n = event['n']
    result = sum(m,n)
    print( "Sum of {} and {} is {}".format(m,n,result) )
