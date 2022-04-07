table = [(pas1,log1),(pas2,log2)]
for i in table:
    if i[1] = request.form['email']:
        table.append((request.form['email'],request.form['password']))
def filters():
    filt = 0
    for i in table:
        if i[1] == request.form['email']:
            x = 1
    if x == 0:
        table.append((request.form['email'],request.form['password']))
    else:
        print('error')
