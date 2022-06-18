from flask import Flask # importamos la libreria flask
from flask import render_template, request, url_for #importamos render_templetam, request, url _for
from fun import fun
app = Flask(__name__)
PORT = 8000
DEBUG = True
@app.errorhandler(404)
def not_found(error):
    return "Not Found"

@app.route('/',methods=['GET'])
def index():
    #texto="""<h1></h1>"""
    #return texto
    #return render_template('index2.html')
    fun.conbd()
    return render_template('index3.html')

@app.route('/home',methods=['POST'])
def Home():
    ema=request.form['ema']
    contr=request.form['contr']
    if(fun.selectuser(ema,contr)):
        return render_template('home.html')
    else:
        return render_template('index3.html')


@app.route('/reg',methods=['GET'])
def reg():    
    return render_template('registro.html')

@app.route('/val',methods=['POST'])
def val():    
    name=request.form['name']
    ap=request.form['ap']
    tel=request.form['tel']
    ema=request.form['ema']
    contr=request.form['contr']
    fun.insertuser(name,ap,tel,ema,contr)
    return render_template('regisexi.html',name=name,ap=ap,tel=tel,ema=ema,contr=contr)

if __name__== '__main__':
    app.run(port=PORT,debug=DEBUG)