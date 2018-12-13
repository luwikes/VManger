from . import db


class Project(db.Model):
    __tablename__ = 'project'  ##注意这句，网上有些实例上并没有
    ##必须设置主键
    id = db.Column(db.Integer, primary_key=True)
    projectName = db.Column(db.String(200))
    implementer = db.Column(db.String(100))
    customer = db.Column(db.String(100))
    implementerPerson = db.Column(db.String(50))
    itemNumber = db.Column(db.String(50))
    startTime = db.Column(db.DateTime)

    def __init__(self, projectName, implementer,
                 customer, implementerPerson,itemNumber,
                 startTime,
                 ):

        self.id = id
        self.projectName = projectName
        self.implementer = implementer
        self.customer = customer
        self.implementerPerson = implementerPerson
        self.itemNumber = itemNumber
        self.startTime = startTime

    def __repr__(self):
        return '<User %r>' % self.year

    def save(self):
        db.session.add(self)
        db.session.commit()


