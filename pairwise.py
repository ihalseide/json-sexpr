# Python 3

def pairwise (iterable):
    '''Iterate in pairs, such that [a, b, c, d, ...] becomes [(a, b), (c, d), ...]
    * See also: https://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list'''
    i = iter(iterable)
    return zip(i, i)
