from src.app import db

class BaseModel(db.Model):
    __abstract__ = True
    def save(self):
        if self not in db.session:
            db.session.add(self)
        db.session.commit()

    def update(self, data: dict):
        for field, value in data.items():
            setattr(self, field, value)
        self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()