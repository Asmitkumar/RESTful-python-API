import json
import os
#from bottle import route, run
from bottle import route, run, static_file, request

# file path set in json
config_file = open( 'config.json' )
config_data = json.load( config_file )
pth_xml     = config_data["paths"]["xml"]

@route('/recipes/')
def recipes_list():
    paths = []
    ls = os.listdir( pth_xml )
    for entry in ls:
        if ".xml" == os.path.splitext( entry )[1]:
            paths.append( entry )
    return { "success" : True, "paths" : paths }

@route('/recipes/<name>', method='GET')
def recipe_show( name="" ):
    if "" != name:
        return static_file( name, pth_xml  )
    else:
        return { "success" : False, "error" : "show called without a filename" }

@route('/recipes/<name>', method='PUT')
def recipe_save( name="" ):
    xml = request.forms.get( "xml" )
    if "" != name and "" != xml:
        with open( os.path.join( pth_xml, name + ".xml" ), "w" ) as f:
            f.write( xml )
        return { "success" : True, "path" : name }
    else:
        return { "success" : False, "error" : "save called without a filename or content" }

@route('/recipes/<name>', method='DELETE' )
def recipe_delete( name="" ):
    if "" != name:
        try:
            os.remove( os.path.join( pth_xml, name + ".xml" ) )
            return { "success" : True  }
        except:
            return { "success" : False  }

run(host='localhost', port=8080, debug=True)
