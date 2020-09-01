# all the imports
#econding: utf-8
# import json
import os
import buildResum
import newspc
# import xlwt
# import xlrd
# import sqlite3



from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, send_from_directory, make_response
from modle import StudentInfomation, TeacherInformation, StudentResume, StudentTerm
from exts import db

import config



app = Flask(__name__)
app.config.from_object(config)
app.secret_key='djskla'
db.init_app(app)
weather = newspc.getweather()




@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


@app.route('/',methods=['GET','POST'])
def hello_world():
    #增
    # studentInfomation1 = StudentInfomation(Student_ID='1600130614',Student_Name='侯潇洋',Student_Ph_Num='15115146509'
    #                                        ,Student_email='1263896586@qq.com',Student_class='软工六班',Student_password='123456')
    # db.session.add(studentInfomation1)
    # db.session.commit()
    #查
    # result = StudentInfomation.query.filter(StudentInfomation.Student_ID=='1600130614').all()/.first()
    # studentInfomation1 = result[0]
    # print(studentInfomation1.Student_ID,studentInfomation1.Student_Name,
    #       studentInfomation1.Student_Ph_Num,studentInfomation1.Student_email,
    #       studentInfomation1.Student_class,studentInfomation1.Student_password)

    #改
    # studentInfomation1 = StudentInfomation.query.filter(StudentInfomation.Student_ID == '1600130614').first()
    # studentInfomation1.Student_ID = '1600130611'
    # db.session.commit()

    #删
    # studentInfomation1 = StudentInfomation.query.filter(StudentInfomation.Student_ID == '1600130611').first()
    # db.session.delete(studentInfomation1)
    # db.session.commit()
    return render_template('Login.html')


@app.route('/teacher_index/',methods=['GET','POST'])
def teacher_index():

    firstpagenew,secendpagenew,threepagenew=newspc.getphoto()

    pagephoto = {'firstpagenew': firstpagenew, 'secendpagenew': secendpagenew, 'threepagenew': threepagenew}

    weathers = newspc.getweather()

    news1,news2,news3= newspc.getnews()

    news = {'news1': news1, 'news2': news2, 'news3': news3}



    return render_template('teacher_index.html',weathers=weathers,news=news,pagephoto=pagephoto)


@app.route('/Login/',methods=['GET','POST'])
def Login():

    weathers = newspc.getweather()

    news1,news2,news3= newspc.getnews()

    news = {'news1': news1, 'news2': news2, 'news3': news3}

    firstpagenew, secendpagenew, threepagenew = newspc.getphoto()

    pagephoto = {'firstpagenew': firstpagenew, 'secendpagenew': secendpagenew, 'threepagenew': threepagenew}

    if request.method=='GET':


        return render_template('Login.html')
    else:
        print('进入post方法')

        theID=request.form.get('theID')

        password = request.form.get('password')

        if len(theID)==6:

            result = TeacherInformation.query.filter(TeacherInformation.Teacher_ID == theID,
                                                     TeacherInformation.Teacher_password==password).all()
            if result:

                    # session['user_id']=result.Teacher_ID
                    # session.permanent=True
                    print('教师登录成功')

                    teacherInformation1 = result[0]

                    session['user_id']=teacherInformation1.Teacher_ID

                    return render_template('teacher_index.html',weathers=weathers,news=news,pagephoto=pagephoto)


            else:

                print('用户名或密码错误，请核对后输入')

                return render_template('login.html')

        else:

            if len(theID) == 10:

                result = StudentInfomation.query.filter(StudentInfomation.Student_ID==theID,
                                                        StudentInfomation.Student_password==password).all()
                if result:
                        # session['user_id'] = result.Teacher_ID
                        # session.permanent = True
                        studentInfomation1 = result[0]

                        print('学生登录成功',studentInfomation1.Student_ID)

                        session['user_id'] = studentInfomation1.Student_ID

                        return render_template('student_index.html',weathers=weathers,news=news,pagephoto=pagephoto)

                else:
                    print('用户名或密码错误，请核对后输入')

                    return render_template('login.html')
            else:
                print("请输入正确的学号或工号")

                return render_template('login.html')


@app.route('/Regist/',methods=['GET','POST'])
def Regist():

    if request.method == 'GET':

        classmassage =StudentTerm.query.filter(StudentTerm.class_ID!=None).all()

        Studen_class_list = []

        list_lenght = len(classmassage)

        for class_list in range(len(classmassage)):

            class_name = classmassage[class_list].class_Name

            Studen_class_list.append(class_name)

        listlenght = len(Studen_class_list)

        print(Studen_class_list)

        return render_template('register.html',Studen_class_list=Studen_class_list,listlenght=listlenght)

    else:


        if request.form.get('identity')=='teacher':

            print('是老师')

            Teacher_ID = request.form.get('theID')

            Teacher_Name = request.form.get('thename')

            Teacher_Ph_Num = request.form.get('thephone')

            Teacher_class = request.form.get('theclass')

            Teacher_email = request.form.get('theemail')

            Teacher_password = request.form.get('thepassword')

            Teacher_password2 = request.form.get('thepassword2')

            studentInfomation = StudentInfomation.query.filter(

                StudentInfomation.Student_Ph_Num == Teacher_Ph_Num).first()

            if studentInfomation:

                return u'该手机号码已被注册，请更换手机号码！'

            else:
                if Teacher_password != Teacher_password2:

                    return u'两次密码不相等，请核对后再填写！'
                else:

                    teacherInfomation = TeacherInformation(Teacher_ID=Teacher_ID,

                                                          Teacher_Name=Teacher_Name,

                                                          Teacher_Ph_Num=Teacher_Ph_Num,

                                                          Teacher_class=Teacher_class,

                                                          Teacher_email=Teacher_email,

                                                          Teacher_password=Teacher_password)

                    db.session.add(teacherInfomation)

                    db.session.commit()

                    return render_template('success.html')


        else :

            print('是学生')

            Student_ID = request.form.get('theID')

            Student_Name = request.form.get('thename')

            Student_Ph_Num = request.form.get('thephone')

            Student_class = request.form.get('theclass')

            Student_email = request.form.get('theemail')

            Student_password = request.form.get('thepassword')

            Student_password2 = request.form.get('thepassword2')


            studentInfomation = StudentInfomation.query.filter(StudentInfomation.Student_Ph_Num==Student_Ph_Num).first()

            if studentInfomation:

                return u'该手机号码已被注册，请更换手机号码！'

            else:

                if Student_password !=Student_password2:

                    return u'两次密码不相等，请核对后再填写！'

                else:

                    studentInfomation =StudentInfomation(Student_ID=Student_ID,

                                                         Student_Name=Student_Name,

                                                         Student_Ph_Num=Student_Ph_Num,

                                                         Student_class=Student_class,

                                                         Student_email=Student_email,

                                                         Student_password=Student_password)

                    db.session.add(studentInfomation)

                    db.session.commit()

                    return render_template('success.html')


@app.route('/student_index/',methods=['GET','POST'])
def student_index():

    if request.method=='GET':

        weathers = newspc.getweather()

        news1, news2, news3 = newspc.getnews()

        weathers = newspc.getweather()

        firstpagenew, secendpagenew, threepagenew = newspc.getphoto()

        pagephoto = {'firstpagenew': firstpagenew, 'secendpagenew': secendpagenew, 'threepagenew': threepagenew}

        print(weathers)

        news ={'news1':news1,'news2':news2,'news3':news3}

        return render_template('student_index.html',weathers=weathers,news=news,pagephoto=pagephoto)


@app.route('/logout/')
def logout():

    session.clear()

    return redirect(url_for('hello_world'))


@app.route('/student_Resum/',methods=['GET','POST'])
def student_Resum():

    if request.method == 'GET':

        user_id  = session.get('user_id')

        path = 'static/Student_Resum/'+user_id

        path = path.strip()

        path = path.rstrip("\\")

        isExists = os.path.exists(path)

        user_resum_name = path + '/' + user_id + '.xls'

        print(user_resum_name)

        user_resumExists = os.path.exists(user_resum_name)

        if not isExists:

            os.makedirs(path)

            print(path + ' 创建成功')

        else:

            print(path + ' 目录已存在')

            print(user_resumExists)

        if user_resumExists == False:

            user_resum = open(user_resum_name, 'wb')

            user_resum.close()

            print(' 创建成功')

        else:

            print(user_resum_name+ '已存在')


        xlsSize = os.path.getsize('C:\\Users\\Administrator\\PycharmProjects\\Student_plan_System\\static\\Student_Resum\\' + user_id + '\\' + user_id + '.xls')

        print(xlsSize)

        if xlsSize<1:

            base_massage ="无"

            personal_summary = "无"

            edu_Experience = "无"

            item_Experience = "无"

            other_honor = "无"

        else:

            base_massage, personal_summary, edu_Experience, item_Experience,\
            other_honor=buildResum.getResum(user_id)


        student_Resums = {'base_massage':base_massage,

                          'personal_summary':personal_summary,

                          'edu_Experience':edu_Experience,

                          'item_Experience':item_Experience,

                          'other_honor':other_honor}




        return render_template('student_Resum.html',student_Resums = {'base_massage':base_massage,
                          'personal_summary':personal_summary,
                          'edu_Experience':edu_Experience,
                          'item_Experience':item_Experience,
                          'other_honor':other_honor},weather=weather)


@app.route('/view_Resum/',methods=['GET','POST'])
def view_Resum():

    if request.method == 'GET':

        Student_ID = session.get('user_id')

        io =  r'static/Student_Resum/' + Student_ID + '/' + Student_ID + '.docx'

        resum = buildResum.viewResum(io)


    return render_template('View_Student_Resum.html',resums = {'resum': resum},weather=weather)


@app.route('/get_student_resum/',methods=['GET','POST'])
def get_student_resum():

    if request.method=='GET':

        return render_template('student_Resum.html')
    else:

        print('进入else')

        Student_ID = session.get('user_id')


        base_massage= request.form.get('base_massage')

        personal_summary = request.form.get('personal_summary')

        edu_Experience = request.form.get('edu_Experience')

        item_Experience = request.form.get('item_Experience')

        other_honor = request.form.get('other_honor')

        xlsSize=os.path.getsize(r'static/Student_Resum/'+Student_ID+'/'+Student_ID+'.xls')

        print(xlsSize)

        if xlsSize > 0:

            buildResum.updateResum(base_massage,personal_summary,edu_Experience,item_Experience,other_honor,Student_ID)

        else:

            buildResum.addResum(base_massage,personal_summary,edu_Experience,item_Experience,other_honor,Student_ID)




        print('showResum方法使用成功')


        io=buildResum.useResum(base_massage,personal_summary,edu_Experience,item_Experience,other_honor,Student_ID)

        Student_Resum_address = io

        print('useResum方法使用成功')

        result = StudentInfomation.query.filter(StudentInfomation.Student_ID == Student_ID).all()

        studentInfomation1 = result[0]

        Student_Name= studentInfomation1.Student_Name

        Student_Ph_Num= studentInfomation1.Student_Ph_Num

        Student_email= studentInfomation1.Student_email

        Student_The_hitnum ='0'

        Student_discuss_address =''

        studentresums = StudentResume.query.filter(StudentResume.Student_Name==Student_Name).all()

        if studentresums :

            pass

        else:
            studentresums = StudentResume(Student_Name=Student_Name,

                                          Student_Ph_Num=Student_Ph_Num,

                                          Student_email=Student_email,

                                          Student_Resum_address=Student_Resum_address,

                                          Student_The_hitnum=Student_The_hitnum,

                                          Student_discuss_address=Student_discuss_address)
            db.session.add(studentresums)

            db.session.commit()


        return render_template('student_Resum.html',student_Resums = {'base_massage':base_massage,
                          'personal_summary':personal_summary,
                          'edu_Experience':edu_Experience,
                          'item_Experience':item_Experience,
                          'other_honor':other_honor},weather=weather)


@app.route('/get_others_resum/',methods=['GET','POST'])
def get_others_resum():

    if request.method=='GET':

        result = StudentResume.query.order_by(-StudentResume.Student_The_hitnum).all()

        Studen_resum_list = []

        list_lenght=len(result)

        for resum_list in range(len(result)):

            Student_name = result[resum_list].Student_Name

            Student_resum_address = str(result[resum_list].Student_Resum_address).split('/')[3]

            Student_The_hitnum = result[resum_list].Student_The_hitnum

            if Student_The_hitnum=='':

                Student_The_hitnum='0'

                print(Student_The_hitnum)

            Student_The_hitnum = int(Student_The_hitnum)

            print(Student_The_hitnum)


            dict = str('Student_' + Student_name + '_resum_dict')

            dict = {'Student_name': Student_name, 'Student_resum_address': Student_resum_address,
                    'Student_The_hitnum':Student_The_hitnum}

            Studen_resum_list.append(dict)

    user_id = session.get('user_id')
    if len(user_id) < 10:
            return redirect(url_for('checkmyclass'))
    return render_template('others_resum.html',Studen_resum_list=Studen_resum_list,list_lenght=list_lenght,weather=weather)


@app.route('/getresum/<resum_address>',methods=['GET','POST'])
def getresum(resum_address):

        Studentname = resum_address

        print("huidiao"+Studentname)




        result = StudentResume.query.filter(StudentResume.Student_Name == Studentname).first()

        studentresum = result

        The_student_docx=buildResum.viewResum(studentresum.Student_Resum_address)

        The_student_hitnum =studentresum.Student_The_hitnum

        The_student_name = studentresum.Student_Name

        #
        The_student_discuss = studentresum.Student_discuss_address


        print(The_student_discuss)

        print(studentresum.Student_Resum_address)

        if The_student_discuss=='':

             The_student_discuss = '该简历暂无评论'
        else:
            Student_ID = str(The_student_discuss).split('评论内容')[0]

            The_student_discuss = r'static/Student_Resum/' + Student_ID + '/' + The_student_discuss

            The_student_discuss = str(The_student_discuss)

            The_student_discuss = buildResum.viewResum(The_student_discuss)


        The_student_hitnum = int(The_student_hitnum)

        The_student_resum={ 'The_student_docx':The_student_docx,
                            'The_student_hitnum':The_student_hitnum,
                            'The_student_name':The_student_name,
                            'The_student_discuss': The_student_discuss}

        #



        return render_template('View_sb_Resum.html',The_student_resum=The_student_resum,weather=weather)


@app.route('/View_mystu_resum/<resum_address>',methods=['GET','POST'])

def View_mystu_resum(resum_address):

        Studentname = resum_address

        print("huidiao"+Studentname)


        result = StudentResume.query.filter(StudentResume.Student_Name == Studentname).first()

        studentresum = result

        The_student_docx=buildResum.viewResum(studentresum.Student_Resum_address)

        The_student_hitnum =studentresum.Student_The_hitnum

        The_student_name = studentresum.Student_Name

        #
        The_student_discuss = studentresum.Student_discuss_address


        print(The_student_discuss)

        print(studentresum.Student_Resum_address)

        if The_student_discuss=='':

             The_student_discuss = '该简历暂无评论'

        else:
            Student_ID = str(The_student_discuss).split('评论内容')[0]

            The_student_discuss = r'static/Student_Resum/' + Student_ID + '/' + The_student_discuss

            The_student_discuss = str(The_student_discuss)

            The_student_discuss = buildResum.viewResum(The_student_discuss)


        The_student_hitnum = int(The_student_hitnum)

        The_student_resum={ 'The_student_docx':The_student_docx,
                            'The_student_hitnum':The_student_hitnum,
                            'The_student_name':The_student_name,
                            'The_student_discuss': The_student_discuss}

        #



        return render_template('View_mystu_resum.html',The_student_resum=The_student_resum,weather=weather)


@app.route('/add_discuss/<mubiao>',methods=['POST'])
def add_discuss(mubiao):

    if request.method=='POST':

        Student_ID = session.get('user_id')

        add_discuss = request.form.get('base_massage')

        padd_discuss = str(add_discuss).replace(' ','')

        if padd_discuss !='':

            print('品论内容：'+add_discuss)

            print("接收到的评论者ID："+Student_ID)

            print("被评论者ID："+mubiao)

            result = StudentInfomation.query.filter(StudentInfomation.Student_Name == mubiao).first()

            studentinformation = result

            discusser = StudentInfomation.query.filter(StudentInfomation.Student_ID==Student_ID).first()
            if discusser:

                discussers = discusser

            else:

                discusser = TeacherInformation.query.filter(TeacherInformation.Teacher_ID==Student_ID).first()

                discussers = discusser

            if studentinformation:

                if len(Student_ID)<10:

                    Studentdiscuss = '\n' + discussers.Teacher_Name + Student_ID + ':    ' + add_discuss + '\n'
                else:
                    Studentdiscuss = '\n' + discussers.Student_Name + Student_ID + ':    ' + add_discuss + '\n'

                Studentdiscuss = str(Studentdiscuss)

                path = 'static/Student_Resum/' + studentinformation.Student_ID

                path = path.strip()

                path = path.rstrip("\\")

                isExists = os.path.exists(path)

                user_resum_name = path + '/' + studentinformation.Student_ID+'评论内容'+ '.docx'

                user_resumExists = os.path.exists(user_resum_name)

                mubiaodocx = studentinformation.Student_ID+'\\'+studentinformation.Student_ID+'评论内容'+ '.docx'

                mubiaodocx =str(mubiaodocx)
                if not isExists:

                    os.makedirs(path)

                    print(path + ' 创建成功')
                else:
                    print(path + ' 目录已存在')

                    print(user_resumExists)


                if user_resumExists == False:

                    user_resum = open(user_resum_name, 'wb')

                    user_resum.close()

                    user_resum = buildResum.setnull(user_resum_name)

                    print(' 创建成功')
                else:
                    print(user_resum_name + '已存在')



                discuss = buildResum.makeDiscuss(user_resum_name,Studentdiscuss)


                studentresum = StudentResume.query.filter(StudentResume.Student_Name == mubiao).first()

                print('成功查询')

                studentresum.Student_discuss_address=discuss

                print('成功修改',studentresum.Student_discuss_address)

                db.session.commit()


        else:
                pass

        # discuss_massage =buildResum.viewResum(discuss)

    return redirect(url_for('getresum',resum_address=mubiao))


@app.route('/hit/',methods=['GET','POST'])
def hit():
    if request.method=='GET':

        hitnum = request.args.get('hitnum')

        hitnum = str(hitnum)

        studentName =request.args.get('StudentName')

        print(hitnum)

        # Student_ID = str(Student_ID).split('.')[0]
        print(2)

        studentresums = StudentResume.query.filter(StudentResume.Student_Name ==studentName).all()

        if studentresums:

            studentresums = studentresums[0]

            if studentresums.Student_The_hitnum == '':

                studentresums.Student_The_hitnum = '0'

            studentresums.Student_The_hitnum = hitnum

            db.session.commit()
        else:
            return '用户数据异常'
    else:
        print('false')
    return 'yes'


@app.route('/dowlod/<docxname>', methods=['GET','POST'])
def dowlod(docxname):

    filename = docxname

    filenames = str(filename).split('.')[0]

    directory = 'C:/Users/Administrator/PycharmProjects/Student_plan_System/static/Student_Resum/'+filenames

    response = make_response(send_from_directory(directory, filename, as_attachment=True))

    print(response)

    return response


@app.route('/checkmyclass/',methods=['GET','POST'])
def checkmyclass():

    tecaherid = session.get('user_id')

    print(tecaherid)

    Student_resum_list=[]

    teachermassage = TeacherInformation.query.filter(TeacherInformation.Teacher_ID==tecaherid).first()

    Teacher={'Teacher_ID':teachermassage.Teacher_ID,
             'Teacher_Name':teachermassage.Teacher_Name}
    theclass = TeacherInformation.Teacher_class

    result = StudentInfomation.query.filter(StudentInfomation.Student_class==theclass).all()

    for i in range(len(result)):

        Student_name = result[i].Student_Name

        print(Student_name)


        resum = StudentResume.query.filter(StudentResume.Student_Name==Student_name).first()

        if resum:

            Student_resum_address = str(resum.Student_Resum_address).split('/')[3]

            Student_The_hitnum = resum.Student_The_hitnum

            if Student_The_hitnum == '':

                Student_The_hitnum = '0'

                print(Student_The_hitnum)

            Student_The_hitnum = int(Student_The_hitnum)

            dict = {'Student_name': Student_name, 'Student_resum_address': Student_resum_address,
                    'Student_The_hitnum': Student_The_hitnum}

            Student_resum_list.append(dict)
        else:
            continue

    result_lenght = len(Student_resum_list)

    print('aaa')

    print(result)

    return render_template('View_my_class.html',Studen_resum_list=Student_resum_list,result_lenght=result_lenght,Teacher=Teacher,weather=weather)


@app.route('/seachsudent/',methods=['POST'])
def seachsudent():

    print("aaaaaaaaaaaaa")

    dict = {}

    if request.method=='POST':

        print('进入了后台方法')

        studentname = request.form.get('studentname')

        print(studentname)

        student = StudentResume.query.filter(StudentResume.Student_Name==studentname).first()

        # Student_resum=[]
        if student:

            if student.Student_Resum_address:

                Student_resum_address = str(student.Student_Resum_address).split('/')[3]

                Student_The_hitnum = student.Student_The_hitnum

                if Student_The_hitnum == '':

                    Student_The_hitnum = '0'

                    print(Student_The_hitnum)

                Student_The_hitnum = int(Student_The_hitnum)

                dict = {'Student_name': studentname, 'Student_resum_address': Student_resum_address,
                        'Student_The_hitnum': Student_The_hitnum}
                # Student_resum.append(dict)

            else:
                dict = {'Student_name': student.Student_Name, 'Student_resum_address': '无简历信息',
                        'Student_The_hitnum': '无'}
                # Student_resum.append(dict)
        else:
            dict = {'Student_name': '查无此人', 'Student_resum_address': '无',
                    'Student_The_hitnum': '无'}
            # Student_resum.append(dict)

    return render_template('View_the_student.html',dict=dict,weather=weather)


@app.context_processor
def my_context_processor():

    print('进入钩子函数')

    user_id = session.get('user_id')

    print('成功取得sessionid：',user_id)

    # get_others_resum()
#str(type(user_id)))
    if user_id:

        user = TeacherInformation.query.filter(TeacherInformation.Teacher_ID==user_id).first()

        if user:

            return {'teacher':user}

        else:
            user = StudentInfomation.query.filter(StudentInfomation.Student_ID==user_id).first()

            return {'student':user}


    return {}


if __name__ == '__main__':

    app.run()



