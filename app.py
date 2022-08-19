# Previous imports remain...
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from flask import request
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

Base = declarative_base()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1122@localhost/cars_api"
db = SQLAlchemy(app)
migrate = Migrate(app, db)



# Образовательная программа
class EducationalPrograms(db.Model):
    __tablename__ = 'educationalPrograms'

    external_id = Column(String, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    direction = Column(String, nullable=False)
    code_direction = Column(String)
    start_year = Column(Integer, nullable=False)
    end_year = Column(Integer, nullable=False)

# Учебный план
class StudyPlan(db.Model):
    __tablename__ = 'studyPlan'

    external_id = Column(String, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    direction = Column(String, nullable=False)
    code_direction = Column(String)
    start_year = Column(Integer, nullable=False)
    end_year = Column(Integer, nullable=False)
    education_form = Column(String, nullable=False)
    educational_program = Column(String, nullable=False)
"""
# Дисциплина
class Discipline(Base):
    __tablename__ = 'discipline'

    external_id = Column(String, nullable=False)
    title = Column(String, nullable=False)

# Связь учебного плана и дисциплины
class StudyPlanDiscipline(Base):
    __tablename__ = 'studyPlanDiscipline'

    study_plan = Column(String, nullable=False)
    discipline = Column(String, nullable=False)
    semester = Column(Integer, nullable=False)
"""
# Студент
class Student(Base):
    __tablename__ = 'students'

    external_id = db.Column(db.String, primary_key=True)
    surname = db.Column(db.String)
    name = db.Column(db.String)
    middle_name = db.Column(db.String)
    snils = db.Column(db.String)
    inn = db.Column(db.String)
    email = db.Column(db.String)
    gisscos_id = db.Column(db.String)
    status = db.Column(db.String)


    def __init__(self, id, human_id):
        self.id = id
        self.human_id = human_id

    def __repr__(self):
        return f""
"""   
# Связь студент и учебный план
class StudyPlanStudent(Base):
    __tablename__ = 'studyPlanStudent'

    study_plan = Column(String, nullable=False)
    student = Column(String, nullable=False)

# Движение контенгента
class ContingentFlow(Base):
    __tablename__ = 'contingentFlow'

    student = db.relationship("Student")
    contingent_flow = Column(String, nullable=False, comment='Событие')
"""
"""
# Оценка
class Marks(Base):
#
# Дополнительные таблицы
class Human(db.Model):
    __tablename__ = 'human'

    id = db.Column(db.Integer, primary_key=True)
    lastName = db.Column(db.String)
    firstName = db.Column(db.String)
    middleName = db.Column(db.String)
    snils = db.Column(db.String)
    inn = db.Column(db.String)
    basicEmail = db.Column(db.String)

    def __init__(self, id, lastName, firstName, middleName, snils, inn, basicEmail):
        self.id = id
        self.lastName = lastName
        self.basicEmail = basicEmail
        self.middleName = middleName
        self.inn = inn
        self.firstName = firstName
        self.snils = snils

    def __repr__(self):
        return f""
#
class Student_status(db.Model):
    __tablename__ = 'studentStatus'

    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String, unique=True)
    gisscos_id = db.Column(db.String, unique=True)
    status = db.Column(db.String)

    def __init__(self, id, external_id, gisscos_id, status):
        self.id = id
        self.external_id = external_id
        self.gisscos_id = gisscos_id
        self.status = status
"""
@app.route('/student', methods = ['POST', 'GET'])
def handle_student():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_student = Student(id=data['id'], human_id=data['human_id'])
            db.session.add(new_student)
            db.session.commit()
            return {"message": f"student {new_student.id}  has been created duccessfully."}
        else:
            return {"error": "The request payload is not in JSON format"}
    elif request.method == 'GET':
        students = Student.query.all()
        results = [
            {
                "id": student.id,
                "human_id": student.human_id
            } for student in students]
        return {"count": len(results), "students": results}

