class Cursor(object):
    def __init__(self, connecter):
        self.main_cursor = connecter.db.cursor()