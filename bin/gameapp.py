import web
from gothonweb import map

urls = (
    '/game', 'GameEngine',
    '/', 'Index',
)

app = web.application(urls, globals())

# Use session can remember current room
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,
            initializer={'room': None, 'heroname': None})
    web.config._session = session
else:
    session = web.config._session

render = web.template.render('templates', base='layout')

class Index(object):
    def GET(self):
        # this is used to "setup" the session with starting values
        session.room = map.START
        return render.hero_register()

    def POST(self):
        form = web.input(heroname=None)
        if form.heroname:
            session.heroname = form.heroname
        else:
            session.heroname = 'Anonym'
        web.seeother("/game")

class GameEngine(object):
    def GET(self):
        if session.room:
            return render.show_room(room=session.room, heroname=session.heroname)
        # If directly use /game URL
        else:
            session.room = map.START
            return render.show_room(room=session.room, heroname=session.heroname)

    def POST(self):
        form = web.input(action=None)
        if session.room and form.action:
            session.room = session.room.go(form.action)
        if session.room is None:
            session.room = map.generic_death

        web.seeother("/game")

if __name__ == "__main__":
    app.run()

