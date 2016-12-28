# -*- coding: utf-8 -*-
import sys, codecs
from collections import defaultdict
from .tables import get_table

def fancymath_main():
    fin = sys.stdin
    fout = sys.stdout
    ferr = sys.stderr
    ferr.write(P + 'Reading from stdin, writing on stdout.')
    ferr.write(P + 'Assuming UTF-8 for both.\n')
    table = get_table()
    make_subs(table, fin, fout, ferr)

def make_subs(table, fin, fout, ferr):
    f = codecs.getreader('utf-8')(fin)
    s = f.read()

    counts = defaultdict(lambda: 0)
    for unicode_literal, latex_command in table:
        n = s.count(latex_command)
        if n > 0:
            counts[latex_command] += n
        s = s.replace(latex_command, unicode_literal)

    if not counts:
        ferr.write(P + 'No substitutions made.\n')
    else:
        latex2literal = dict( (_[1], _[0]) for _ in table)
        ferr.write(P + 'Substitutions:\n')
        for w in sorted(counts, key=lambda k: -counts[k]):
            ferr.write(P + '"%s" replaced %15s a total of %4d times\n' %
                        ("%3s" % latex2literal[w],"%15s" %w , counts[w]))
        ferr.write('\n\n')
    codecs.getwriter('utf-8')(fout).write(s)

P = 'fancymath: '

if __name__ == '__main__':
    fancymath_main()
