"""
Wrapper around csv.reader that receives a list of parsers, each specifying 
how to parse each column.
"""

def parse_row(input_row, parsers):
    """given a list of parsers (some of which may be None), apply the 
    appropriate one to each element of the input_row"""
    
    return [try_or_none(parser)(value) if parser is not None else value
            for value, parser in zip(input_row, parsers)]
    
def parse_rows_with(reader, parsers):
    """wrap a reader to apply the parsers to each of its rows"""
    for row in reader:
        yield parse_row(row, parsers)
        
def try_or_none(f):
    """wraps f to return None if f raises an exception assumes f takes only 
    one input"""
    def f_or_none(x):
        try: return f(x)
        except: return None
    
    return f_or_none