"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from xblock.fragment import Fragment
from django.template import Context, Template
from xblock.core import XBlock
from xblock.fields import Integer, Scope, String, Boolean, Dict

class MyXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    username = String(
        default="", scope=Scope.user_state,
        help="Nombre de usuario",
    )

    lastname = String(
        default="", scope=Scope.user_state,
        help="Apellido del usuario",
    )

    email = String(
        default="", scope=Scope.user_state,
        help="Correo del usuario",
    )

    title = String(
        default="MyXBlock", scope=Scope.content,
        help="Título del XBlock"
    )

    totalAnswers = Integer(
        default=0, scope=Scope.user_state_summary,
        help="Total de respuestas"
    )

    flag = Boolean(
        default=False, scope=Scope.user_state,
        help="Bandera para saber si fue resuelto el formulario"
    )

    def load_resource(self, resource_path):
        """
        Gets the content of a resource
        """
        resource_content = pkg_resources.resource_string(__name__, resource_path)
        return resource_content.decode("utf8")

    def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        template_str = self.load_resource(template_path)
        return Template(template_str).render(Context(context))

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the MyXBlock, shown to students
        when viewing courses.
        """
        context = {
            'flag': self.flag,
            'name': self.username,
            'lastname': self.lastname,
            'email': self.email,
            'title': self.title,
            'total': self.totalAnswers,
        }
        
        html = self.render_template("static/html/myxblock.html", context)
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/myxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/myxblock.js"))
        frag.initialize_js('MyXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def get_formdata(self, data, suffix=''):
        self.username = data['name']
        self.lastname = data['lastname']
        self.email = data['email']
        self.totalAnswers += 1
        self.flag = True
        self.student_view()        

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("MyXBlock",
             """<myxblock/>
             """),
            ("Multiple MyXBlock",
             """<vertical_demo>
                <myxblock/>
                <myxblock/>
                <myxblock/>
                </vertical_demo>
             """),
        ]
