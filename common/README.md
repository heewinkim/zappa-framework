## common pakage  

### Note
    본 프로젝트는 zappa lambda 구현시 필요한 최소한의 기본 공통프레임워크입니다. 
---

### common.core
- error : Error 에러클래스 제공, ERROR_TYPES의 에러 타입 제공
- logger : Logger 클래스 제공, 로그관련 처리 기능 제공
- output : Output 클래스 제공, output 관련기능, 에러에 대한 로그처리 기능 제공

### common.framwork  

- flask : Flask로 구현된 웹 API 클래스인 Flask 를 제공합니다.  


    >>> EXMAPLE
    
    # -*- coding: utf-8 -*-
    """
    본 코드는 API 작성에 대한 예시 입니다.
    예시 API로는 본 코드에 작성된
    ExampleApi 클래스를 사용합니다.
    실제 API 사용시에는 API 클래스를 import 하여 사용합니다.
    """
    
    
    class ExampleApi(object):
    
        def run(self):
            result = {'arg1':100,'arg2':200}
            return result
    
    
    from framework.snaps_flask import SnapsFlask
    
    example_api = ExampleApi()
    application = SnapsFlask('ex')
    
    
    @application.route('/snaps/v1/example',methods=['POST','GET'])
    def request_api():
    
        application.output.set_default(['arg1','arg2'],-1)
        result = example_api.run()
        return application.output.return_output(result)
    
    if __name__ == '__main__':
        application.run('0.0.0.0',port=5000)    
    
