from flask import Flask,render_template,request, redirect,url_for
app = Flask(__name__)
from pytube import YouTube



@app.route('/',methods=['POST', 'GET'])
def home():
    url1=""
    if request.method == 'POST':
        url=request.form.get('url')
        yt=YouTube(url)
        res=request.form.get('resolution')
        stream=yt.streams.get_by_resolution(res)
        path=request.form.get('path')
        if(stream.download(path)):
            url1="Successful"
        else:
            url1="unsuccessful"
    return render_template('index.html',url1=url1)   

if __name__=="__main__":
    app.run()
