from .routesfunc import *

def setuproute(app, call):
    @app.route('/test/',            ['OPTIONS', 'POST', 'GET'], lambda x = None: call([])                                   )
    @app.route('/login/',    	    ['OPTIONS', 'POST'],        lambda x = None: call([getauth])                            )
    @app.route('/infos/',    	    ['OPTIONS', 'POST'],        lambda x = None: call([myauth, exist,  infos])              )
    @app.route('/create/',    	    ['OPTIONS', 'POST'],        lambda x = None: call([myauth, create, exist,  infos])      )
    @app.route('/changepower/',     ['OPTIONS', 'POST'],        lambda x = None: call([myauth, exist,  changepow, infos])   )
    @app.route('/changedata/',      ['OPTIONS', 'POST'],        lambda x = None: call([myauth, exist,  changedata, infos])  )
    @app.route('/changecharge/',    ['OPTIONS', 'POST'],        lambda x = None: call([myauth, exist,  changecharge, infos]))
    @app.route('/admin/infos/',     ['OPTIONS', 'POST'],        lambda x = None: call([myauth, allinfos])                   )
    def base():
        return
