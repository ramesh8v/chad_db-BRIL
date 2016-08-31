
class Buildings(db.Model):
    __table__ = db.Model.metadata.tables['few']

    def __repr__(self):
        return self.DISTRICT