from csv import reader
from collections import defaultdict
ex = reader(open('exam2.csv'))
next(ex)
ex = list(ex)

def calculate_avg(ex):
    people = {}
    for i in ex:
        try:
            int(row[14])
            row[13],row[14] = row[14],""
        except:
            pass 
    for row in ex:
        if row[1] != '':
            for i, x in enumerate(row[2:]):
                try:
                    people[row[1]] = people.get(row[1], {'quiz':[], "midterm":0})
                    if i == 10:
                        people[row[1]]['midterm'] = float(x)
                    else:
                        people[row[1]]['quiz'].append(float(x))
                except:
                    people[row[1]]['quiz'].append(0)
                    continue
    v = []
    # text = "AVERAGE\n"
    for i,x in people.items():
        sor = sorted(x['quiz'], reverse = True)[:7]
        su = ((sum(sor)/6)*0.7) + (x['midterm']*0.075)//0.075
        v.append((i,su))
        # text+=f"{i} - {su}\n"
    return v
print(calculate_avg(ex))

         