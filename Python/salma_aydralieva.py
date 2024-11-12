from csv import reader
from collections import defaultdict
def get_average_score(file):
    ex = reader(open(file))
    ex = list(ex)
    people = {}
    for i,x in enumerate(ex[0]):
        if x == 'names':
            name_id = i
        if x == '10/14/2024':
            mid_id = i
        if x == 'id':
            idd = i
    for row in ex[1:]:
        if row[1] != '':
            for i, x in enumerate(row):
                try:
                    people[row[name_id]] = people.get(row[name_id], {'quiz':[], "midterm":0})
                    if i == mid_id:
                        people[row[name_id]]['midterm'] = float(x)
                    elif idd == i:
                        continue
                    else:
                        people[row[name_id]]['quiz'].append(float(x))
                except:
                    people[row[name_id]]['quiz'].append(0)
                    continue
    v = []
    for i,x in people.items():
        sor = sorted(x['quiz'], reverse = True)[:7]
        su = round((((sum(sor)/7)*0.7) + (x['midterm']*0.075))/0.775)
        v.append((i,su))
    return v
print(get_average_score('exam_final.csv'))

# my_name = 'Salma Aydralieva'
# from csv import reader
# def get_average_score(filename):
#     with open(filename) as fid:
#         r = reader(fid)
#         '''YOUR CODE HERE'''
        
#         ###return [(None, None)]

# from csv import reader, writer
# scores = get_average_score("exam4.csv")
# d = {name:score for name, score in scores}
# out = []
# with open('result.csv') as fid:
#     r = reader(fid)
#     out.append(list(next(r)) + [my_name])
#     for i in r:
#         res = i + [d.get(i[0],'')]
#         out.append(res)
# with open('result.csv', 'w', newline='') as fid:
#     w = writer(fid)
#     w.writerows(out)
