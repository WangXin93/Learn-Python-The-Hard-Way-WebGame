import web

# Whatever someone goes to / with a browser, lpthw.web will find the class
# index and load it to handle the request.
urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('templates/', base="layout")

class Index:
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet=None)
        if form.greet:
            greeting = "%s, %s" % (form.greet, form.name)
            return render.index(greeting = greeting)
        else:
            return "ERROR: greet is required."
    
if __name__ == "__main__":
    app.run()
