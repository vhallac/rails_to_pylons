import sample_app.model as model
import formencode

class Unique(formencode.FancyValidator):
    messages = {
        'invalid': 'This value must be unique'
        }
    def validate_python(self, value, state):
        filter_kw = {str(self.filter_column): value}
        query = model.Session.query(self.orm_class)
        item = query.filter_by(**filter_kw).first()
        if item:
            raise formencode.Invalid(
                self.message('invalid', state),
                value, state)
        return value
