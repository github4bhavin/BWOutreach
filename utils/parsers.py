import re

def city_parser_from_full_address(address):
    m = re.match(r'.*(avenue|street|ave|st) (.*), .*', address.lower())
    return m.groups(1)[1] if len(m.groups())>1 else None
    