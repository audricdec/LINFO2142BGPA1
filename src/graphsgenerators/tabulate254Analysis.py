from tabulate import tabulate
from texttable import Texttable
from latextable import draw_latex

index = [2, 2, 254, 254, 254, 254, 254, 254, 254, 254, 254, 254]
data = [16, 15, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]
rows = [index, data]
print('Tabulate Table:')
print(tabulate(rows, headers='firstrow'))
table = Texttable()
table.set_cols_align(["c"] * 12)
table.set_deco(Texttable.HEADER | Texttable.VLINES)
print('\nTexttable Table:')
print(table.draw())

print(tabulate(rows, headers='firstrow', tablefmt='latex'))
print(draw_latex(table, caption='A comparison of rocket features.'))