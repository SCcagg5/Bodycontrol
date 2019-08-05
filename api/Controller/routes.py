from .routesfunc import *

def setuproute(app, call):
    @app.route('/test/',            ['OPTIONS', 'POST', 'GET'], lambda x = None: call([])                                 )
    @app.route('/login/',    	    ['OPTIONS', 'POST'],        lambda x = None: call([getauth])                          )
    @app.route('/infos/',    	    ['OPTIONS', 'POST'],        lambda x = None: call([auth, exist,  infos])              )
    @app.route('/create/',    	    ['OPTIONS', 'POST'],        lambda x = None: call([auth, create, exist,  infos])      )
    @app.route('/changepower/',     ['OPTIONS', 'POST'],        lambda x = None: call([auth, exist,  changepow, infos])   )
    @app.route('/changedata/',      ['OPTIONS', 'POST'],        lambda x = None: call([auth, exist,  changedata, infos])  )
    @app.route('/admin/infos/',     ['OPTIONS', 'POST'],        lambda x = None: call([auth, allinfos])                   )
    def base():
        return
