from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from app.myschedule import getDailySchedule, resetCount, getCount

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def getRequestschedule():
    nrfc, nincidents, nalerts, l = None, None, None, None
    form = LoginForm()
    if request.args.get('reset'):
        print("RESET")
        resetCount()
        return render_template('login.html',  title='AMS', form=form, messages=['Count  Reset'])

    if request.args.get('showcount'):
        ct = getCount()
        countstr = []
        for k,v in ct.items():
            countstr.append( '{}: {}'.format(k, v))
        
        return render_template('login.html',  title='AMS', form=form, messages=countstr)

    if request.args.get('nrfc'):
        nrfc = int(request.args.get('nrfc').strip())

    if request.args.get('nincidents'):
        nincidents = int(request.args.get('nincidents').strip())
    
    if request.args.get('nalerts'):
        nalerts = int(request.args.get('nalerts').strip())

    if request.args.get('people'):
        lstr = request.args.get('people')
        l = lstr.split(',') 
        l = [int(ls.strip()) for ls in l]
    if nrfc and nincidents and nalerts and l:
        print('nrfc: ', nrfc)
        print('nincidents: ', nincidents)
        print('nalerts: ', nalerts)
        print('list: ', l) 

        sch, count = getDailySchedule(nincidents, nrfc, nalerts, l)

        incstr = "Incident: " + ', '.join(sch['incident'])
        servstr = "RFC: " + ', '.join(sch['service'])
        alertstr = "Alert: " + ', '.join(sch['alert'])
        countstr = []
        for k,v in count.items():
            countstr.append( '{}: {}'.format(k, v))
        print(sch)
        return render_template('login.html',  title='AMS', form=form, messages=[incstr, servstr, alertstr, '===================== Counts ===================== '] + countstr)
    return render_template('login.html',  title='AMS', form=form, messages=[])
