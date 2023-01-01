from tabulate import tabulate
from texttable import Texttable
from latextable import draw_latex

index01 = [3, 1, 2, 4, 5, 7, 8, 9, 6, 10, 14, 15, 11, 19, 12, 30, 23, 20, 16, 13, 21, 24, 18, 49, 25, 17]
data01 = [372294, 743855, 442417, 189916, 138551, 35732, 23683, 18967, 52431, 21192, 8027, 5476, 9381, 121, 3020, 39, 700, 680, 722, 1940, 61, 291, 238, 36, 3, 49]
index02 = [3, 1, 2, 4, 5, 7, 8, 9, 6, 10, 14, 15, 11, 19, 12, 30, 17, 20, 16, 13, 21, 24, 49, 25, 18]
data02 = [376807, 728722, 447596, 190038, 133500, 36790, 22841, 20280, 55199, 22564, 6336, 4797, 9832, 103, 2813, 42, 127, 955, 818, 1929, 9, 407, 35, 3, 21]
index03 = [3, 1, 2, 4, 5, 7, 8, 9, 6, 10, 14, 15, 11, 19, 16, 12, 30, 18, 17, 20, 13, 24, 254, 23, 49, 25, 26]
data03 = [379788, 708224, 435942, 183985, 130698, 34261, 22646, 19072, 56530, 21550, 6558, 5096, 9047, 421, 931, 2127, 42, 54, 91, 897, 1672, 362, 2, 243, 34, 2, 15]
index04 = [2, 3, 1, 4, 5, 7, 8, 9, 6, 10, 14, 15, 11, 19, 12, 18, 17, 16, 13, 30, 20, 24, 254, 49, 25, 50]
data04 = [443998, 391174, 728928, 194375, 137380, 34749, 24391, 22635, 54768, 23046, 6444, 4751, 10002, 188, 1758, 54, 91, 747, 1977, 9, 449, 218, 3, 36, 3, 15]
index05 = [2, 3, 1, 4, 5, 7, 8, 9, 6, 10, 14, 15, 11, 19, 12, 18, 20, 16, 13, 30, 24, 21, 254, 49, 25, 17, 50]
data05 = [463388, 397647, 740586, 194653, 138382, 36502, 25430, 26385, 57082, 22599, 5883, 5624, 9396, 192, 1967, 55, 467, 559, 2031, 9, 221, 11, 3, 34, 53, 39, 20]
index06 = [2, 3, 1, 4, 5, 7, 8, 9, 6, 10, 15, 11, 19, 12, 18, 16, 14, 13, 30, 20, 21, 254, 24, 49, 22, 25, 17]
data06 = [468483, 393767, 727674, 194337, 134026, 40398, 24916, 25361, 57785, 22751, 5298, 9766, 188, 2109, 57, 630, 3151, 1800, 9, 465, 5, 3, 381, 3, 5, 52, 39]
index07 = [2, 3, 1, 6, 4, 5, 7, 8, 9, 10, 11, 15, 19, 12, 14, 18, 16, 13, 34, 30, 20, 21, 254, 24, 99, 49, 22, 25, 17]
data07 = [490935, 399657, 745220, 59014, 205332, 132508, 37256, 24849, 24996, 23228, 9603, 5534, 171, 2157, 2415, 58, 689, 2035, 3, 8, 381, 5, 3, 354, 1, 31, 5, 53, 39]
index08 = [2, 3, 1, 4, 5, 7, 8, 9, 6, 10, 11, 15, 19, 12, 14, 18, 13, 16, 17, 30, 20, 21, 254, 24, 49, 22, 25]
data08 = [471743, 390499, 712852, 196714, 128186, 34996, 25876, 22916, 57029, 23544, 8975, 5406, 69, 1985, 2359, 57, 2602, 666, 90, 9, 359, 4, 4, 243, 30, 4, 51]
index09 = [2, 3, 1, 4, 5, 7, 8, 9, 10, 6, 11, 15, 13, 19, 14, 18, 16, 12, 27, 30, 20, 21, 254, 24, 23, 22, 49, 17, 25, 31]
data09 = [503463, 402603, 733707, 211219, 131816, 37720, 29371, 24144, 25127, 63921, 9220, 4865, 2947, 71, 1916, 60, 666, 1816, 73, 10, 196, 89, 4, 324, 52, 55, 33, 253, 67, 14]
index10 = [2, 3, 1, 4, 5, 7, 8, 9, 10, 6, 11, 15, 13, 19, 12, 14, 18, 16, 30, 21, 254, 24, 23, 20, 22, 25, 49, 17, 31]
data10 = [518267, 408742, 764668, 217680, 130692, 39232, 30109, 26435, 26258, 64013, 9138, 4950, 2961, 119, 2710, 2175, 278, 725, 11, 100, 4, 495, 55, 182, 66, 74, 33, 39, 53]
index11 = [1, 3, 2, 4, 5, 7, 8, 9, 10, 6, 15, 13, 11, 12, 14, 16, 23, 20, 17, 30, 21, 254, 24, 18, 19, 25, 49, 22]
data11 = [755797, 402295, 516097, 214667, 129995, 40404, 31343, 27294, 27407, 62846, 4576, 2909, 9034, 2695, 1956, 666, 108, 192, 94, 10, 45, 4, 595, 2, 178, 75, 33, 13]
index12 = [1, 3, 2, 4, 5, 7, 8, 9, 10, 6, 15, 13, 11, 12, 14, 18, 16, 17, 24, 20, 30, 254, 19, 49, 22, 21, 25, 65]
data12 = [762836, 406869, 514887, 221273, 135168, 39810, 28255, 25481, 29023, 60917, 4254, 3245, 9111, 2083, 1890, 163, 1453, 95, 1596, 409, 11, 4, 77, 32, 5, 5, 7, 4]

sorted_index01, sorted_data01 = [x[0] for x in sorted(zip(index01, data01))], [x[1] for x in sorted(zip(index01, data01))]
sorted_index02, sorted_data02 = [x[0] for x in sorted(zip(index02, data02))], [x[1] for x in sorted(zip(index02, data02))]
sorted_index03, sorted_data03 = [x[0] for x in sorted(zip(index03, data03))], [x[1] for x in sorted(zip(index03, data03))]
sorted_index04, sorted_data04 = [x[0] for x in sorted(zip(index04, data04))], [x[1] for x in sorted(zip(index04, data04))]
sorted_index05, sorted_data05 = [x[0] for x in sorted(zip(index05, data05))], [x[1] for x in sorted(zip(index05, data05))]
sorted_index06, sorted_data06 = [x[0] for x in sorted(zip(index06, data06))], [x[1] for x in sorted(zip(index06, data06))]
sorted_index07, sorted_data07 = [x[0] for x in sorted(zip(index07, data07))], [x[1] for x in sorted(zip(index07, data07))]
sorted_index08, sorted_data08 = [x[0] for x in sorted(zip(index08, data08))], [x[1] for x in sorted(zip(index08, data08))]
sorted_index09, sorted_data09 = [x[0] for x in sorted(zip(index09, data09))], [x[1] for x in sorted(zip(index09, data09))]
sorted_index10, sorted_data10 = [x[0] for x in sorted(zip(index10, data10))], [x[1] for x in sorted(zip(index10, data10))]
sorted_index11, sorted_data11 = [x[0] for x in sorted(zip(index11, data11))], [x[1] for x in sorted(zip(index11, data11))]
sorted_index12, sorted_data12 = [x[0] for x in sorted(zip(index12, data12))], [x[1] for x in sorted(zip(index12, data12))]


# table = [["Length",sorted_index01[:10]],["Count",sorted_data01[:10]]]
# print(tabulate(table,tablefmt="latex"))
rows = [sorted_index01[:10], sorted_data12[:10]]
print('Tabulate Table:')
print(tabulate(rows, headers='firstrow'))
table = Texttable()
table.set_cols_align(["c"] * 10)
table.set_deco(Texttable.HEADER | Texttable.VLINES)
print('\nTexttable Table:')
print(table.draw())

print(tabulate(rows, headers='firstrow', tablefmt='latex'))
print(draw_latex(table, caption='A comparison of rocket features.'))