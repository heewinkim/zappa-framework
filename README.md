## Zappa wrapping framework

    aws lambda - zappa - flask - python 
    을 한번더 감싼 개인적인 목적의 프로젝트 입니다. 

----

- 좀더 사용하기 편한 (로그관리, 인풋아웃풋처리, 에러처리, 등) Flask 제공 (common/flask.py)


----

### USEAGE

source/main.py 에 API 작성.

    from common.framework.flask import Flask
    
    # route('/{api_name}'),('/') 자동으로 할당됨 
    api_name='api'
    
    # zappa  app_function(wsgi)을 source.main.application으로 전해주면 됨.
    application = Flask(api_name)
    
    @application.route('/function',methods=['POST','GET'])
    def request_fd():
    
        # default output key value 설정
        application.output.set_default(dict_obj={'appType': '','transId': ')})
        
        # output은 다음과같이 최종결과를 dict로 보내면 됨
        return application.output.return_output({'result':'good'})
    
    if __name__ == '__main__':
        application.run()
        
        
