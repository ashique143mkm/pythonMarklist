from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')
	
@app.route("/generate")
def generate():
    return render_template('index.html')

@app.route("/send",methods=['POST','GET'])
def send():
    if(request.method=='POST'):
        name=request.form['name']
        regno=request.form['regno']
        semester=request.form['semester']
        collage=request.form['collage']
        s1n=request.form['s1n']
        a=request.form['s1m']
        b=request.form['s1tm']
        s2n=request.form['s2n']
        c=request.form['s2m']
        d=request.form['s2tm']
        s3n=request.form['s3n']
        e=request.form['s3m']
        f=request.form['s3tm']
        s4n=request.form['s4n']
        g=request.form['s4m']
        h=request.form['s4tm']
        
        s1m=int (a)
        s1tm=int (b)
        s2m=int (c)
        s2tm=int (d)
        s3m=int (e)
        s3tm=int (f)
        s4m=int (g)
        s4tm=int (h)
       

        

        w=(s1m/s1tm)*100
        x=(s2m/s2tm)*100
        y=(s3m/s3tm)*100
        z=(s4m/s4tm)*100

        subjectlist=[w,x,y,z]

        resultlist=[]

        for i in subjectlist:
                if i>=96 and i<100:
                        
                        grade='S'
                        result='Pass'
                
                elif i>=91 and i<95:
                        
                        
                        grade='A+'
                        result='Pass'
                
                elif i>=86 and i<90:
                        
                        grade='A'
                        result='Pass'

                elif i>=81 and i<85:
                        
                        grade='B+'
                        result='Pass'

                elif i>=76 and i<80:
                        
                        grade='B'
                        result='Pass'

                elif i>=71 and i<75:
                        
                        grade='C+'
                        result='Pass'

                elif i>=66 and i<=70:
                        
                        grade='C'
                        result='Pass'

                elif i>=61 and i<=75:
                        
                        grade='D+'
                        result='Pass' 

                elif i>=56 and i<=60:
                        
                        grade='D'
                        result='Pass'

                elif i>=50 and i<=55:
                        
                        grade='E'
                        result='Pass'      
                
                else:
                        grade='U'
                        result='Fail'
                
                resultlist.append(grade)
                resultlist.append(result)

        for j in resultlist:

            if j=='Fail':
                semesterresult='Fail'
                semvalue='Fail'
                break
            else:
                semesterresult='PASS'
                semvalue='Pass'

        
        return render_template('/generate.html',getname=name,getregno=regno,getsemester=semester,getcollage=collage,sb1n=s1n,sb1m=s1m,sb1tm=s1tm,sb2n=s2n,sb2m=s2m,sb2tm=s2tm,sb3n=s3n,sb3m=s3m,sb3tm=s3tm,sb4n=s4n,sb4m=s4m,sb4tm=s4tm,semresult=semesterresult,list=resultlist,jojo=semvalue)
    
if(__name__=='__main__'):
        app.run(debug=True)




        