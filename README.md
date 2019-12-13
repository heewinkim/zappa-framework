## Zappa wrapping framework

    aws lambda - zappa - flask - python 
    을 한번더 감싼 개인적인 목적의 프로젝트 입니다. 

----

- 좀더 사용하기 편한 (로그관리, 인풋아웃풋처리, 에러처리, 등) Flask 제공 (common/flask.py)


----


### common.core
- error : Error 에러클래스 제공, ERROR_TYPES의 에러 타입 제공
- logger : Logger 클래스 제공, 로그관련 처리 기능 제공
- output : Output 클래스 제공, output 관련기능, 에러에 대한 로그처리 기능 제공

### common.framwork  

- flask : Flask로 구현된 웹 API 클래스인 Flask 를 제공합니다.  

### source.main

- main : flask 를 이용하여 lambda function 를 구현하는 파일입니다.  

---

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
        application.output.set_default(dict_obj={'result':None})
        
        # files, form, json, args 파라미터는 모두 다음과같이 꺼내올 수 있음
        data = application.output.form['data']
        
        # output은 다음과같이 최종결과를 dict로 보내면 됨
        return application.output.return_output(
            {
                'result':'good {}'.format(data)
            }
        )
    
    if __name__ == '__main__':
        application.run()
        
        
