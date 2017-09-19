from flask_admin import BaseView, expose


class SampleView(BaseView):
    @expose('/')
    def index(self):
        return self.render('sample_index.html')
