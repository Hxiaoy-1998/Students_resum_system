from sqlalchemy import ForeignKey

from exts import db

class StudentInfomation(db.Model):
    __tablename__ ='studentInfomation'

    Student_ID = db.Column(db.String(20),primary_key=True)

    Student_Name = db.Column(db.String(20),nullable=False)

    Student_Ph_Num = db.Column(db.String(20), nullable=False)

    Student_email = db.Column(db.String(20), nullable=False)

    Student_class = db.Column(db.String(20), ForeignKey("studentTerm.class_Name"),nullable=False)

    Student_password = db.Column(db.String(20), nullable=False)


class StudentResume(db.Model):

    __tablename__ ='studentResume'

    Student_Name = db.Column(db.String(20),primary_key=True)

    Student_Ph_Num = db.Column(db.String(20), nullable=False)

    Student_email = db.Column(db.String(20), nullable=False)

    Student_Resum_address = db.Column(db.String(50), nullable=False)

    Student_The_hitnum = db.Column(db.String(10), nullable=False)

    Student_discuss_address =db.Column(db.String(49),nullable=False)

    #The_discussnum = db.Column(db.Integer(20),nullable=True)





class StudentTerm(db.Model):

    __tablename__='studentTerm'

    class_ID = db.Column(db.String(20), primary_key=True)

    class_Name = db.Column(db.String(20),nullable=False)



# class TermNum(db.Model):
#     __tablename__='termNum'
#     Student_Term_01 = db.Column(db.String(20),primary_key=True, nullable=False)
#     Student_Term_02 = db.Column(db.String(20), nullable=False)
#     Student_Term_03 = db.Column(db.String(20), nullable=False)
#     Student_Term_04 = db.Column(db.String(20), nullable=False)
#     Student_Term_05 = db.Column(db.String(20), nullable=False)
#     Student_Term_06 = db.Column(db.String(20), nullable=False)
#     Student_Term_07 = db.Column(db.String(20), nullable=False)


# class Student_Learn_Plan(db.Model):
#     __tablename__='student_Learn_Plan'
#     Student_Learn_Plan01_address = db.Column(db.String(50),primary_key=True)
#     Student_Opinion01_address = db.Column(db.String(50))
#     Student_Learn_Plan02_address = db.Column(db.String(50))
#     Student_Opinion02_address = db.Column(db.String(50))
#     Student_Learn_Plan03_address = db.Column(db.String(50))
#     Student_Opinion03_address = db.Column(db.String(50))
#     Student_Learn_Plan04_address = db.Column(db.String(50))
#     Student_Opinion04_address = db.Column(db.String(50))
#     Student_Learn_Plan05_address = db.Column(db.String(50))
#     Student_Opinion05_address = db.Column(db.String(50))
#     Student_Learn_Plan06_address = db.Column(db.String(50))
#     Student_Opinion06_address = db.Column(db.String(50))
#     Student_Learn_Plan07_address = db.Column(db.String(50))
#     Student_Opinion07_address = db.Column(db.String(50))

class TeacherInformation(db.Model):

    __tablename__ = 'teacherInfomation'

    Teacher_ID = db.Column(db.String(20), primary_key=True)

    Teacher_Name = db.Column(db.String(20), nullable=False)

    Teacher_Ph_Num = db.Column(db.String(20), nullable=False)

    Teacher_email = db.Column(db.String(20), nullable=False)

    Teacher_class = db.Column(db.String(20), nullable=False)

    Teacher_password = db.Column(db.String(20), nullable=False)

