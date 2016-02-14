#!/c/Users/User/Anaconda2/python
import numpy
from pandas import DataFrame, Series

def test():
    frame = DataFrame(numpy.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
    format = lambda x: '%.2f' % x
    range = lambda x: x.max() - x.min()
    
    # http://stackoverflow.com/questions/19798153/difference-between-map-applymap-and-apply-methods-in-pandas/19798528#19798528
    print(frame.apply(range))
    print("")
    print(frame.applymap(format))
    print("")
    print(frame.apply(range).map(format))
    
    return frame

test()