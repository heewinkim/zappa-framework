import urllib.request
from PIL import Image
from io import BytesIO
from common.framework.flask import Flask

api_name='zp'
application = Flask(api_name)


@application.route('/test',methods=['POST','GET'])
def request_fd():

    #application.output.set_default()
    return application.output.return_output({})


@application.route('/checkimg',methods=['POST','GET'])
def home():

    # application.output.set_default()
    url = application.form['url']
    response = urllib.request.urlopen(url)
    bytes_data = response.read()
    img = Image.open(BytesIO(bytes_data))
    result={'width':img.width,'height':img.height}

    return application.output.return_output(result)


if __name__ == '__main__':

    application.run()