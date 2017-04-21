# from itertools import chain, islice
# import  sys
import codecs

# def chunks(iterable, n):
#    "chunks(ABCDE,2) => AB CD E"
#    iterable = iter(iterable)
#    while True:
#        # store one line in memory,
#        # chain it to an iterator on the rest of the chunk
#        yield chain([next(iterable)], islice(iterable, n-1))

# l = 30*10**6
# file_large = 'MAG/PaperAuthorAffiliations/PaperAuthorAffiliations.txt'
# with codecs.open(file_large, encoding="utf-8") as bigfile:
#     for i, lines in enumerate(chunks(bigfile, l)):
#         file_split = '{}.{}'.format(file_large, i)
#         with codecs.open(file_split, 'w', encoding="utf-8") as f:
#             print(lines)
#             f.writelines(lines)


from itertools import izip_longest

def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

n = 10000000

file = 'PaperAuthorAffiliations'
directory='MAG/' + file + '/'
big_filename = file + '.txt'

with codecs.open('{}{}'.format(directory,big_filename), encoding="utf-8") as f:
    for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
    	print i
        with codecs.open(directory + 'splits/small_file_{0}'.format(i * n), 'w', encoding="utf-8") as fout:
            fout.writelines(g)