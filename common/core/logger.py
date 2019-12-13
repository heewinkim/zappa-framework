# -*- coding: utf-8 -*-
"""
===============================================
logger module
===============================================

========== ====================================
========== ====================================
 Module     logger module
 Date       2019-03-26
 Author     hian
 Comment    `관련문서링크 <>`_
========== ====================================

*Abstract*
    * 설정값을 로드하여 제공하는 모듈입니다.
    * 외부에서 사용시 인스턴스화 된 logger 를 import 하여 사용합니다.
    * set_input2log 를 통해 요청마다 클라이언트 정보를 입력해주어야 합니다.

    >>> EXAMPLE
    import traceback

    logger = Logger()


    def do_something():
        raise ValueError

    try:
        do_something()

    except Exception as e:
        logger.logger.error(traceback.format_exc())

    * TODO info 로그에 error로그가 포함되는 문제 개선필요


===============================================
"""
import time
import logging
from .singleton import Singleton
monthes = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
           'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
           'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12',
           }


class Logger(logging.Filter,metaclass=Singleton):

    def __init__(self, log_name):

        """
        init function

        :param log_name: log 파일에 접미사로 붙을 이름
        """

        # 로그 저장 경로
        self.log_name = log_name
        self.logs_type = ["info", "error"]
        self.logs_info = {"format":".log"}

        self.__logger = logging.getLogger(self.log_name)
        self.__logger.setLevel(logging.INFO)

        # 포매터를 만든다
        self.formatter = logging.Formatter(
            '%(levelname)s\t%(process)d\t%(asctime)s\t%(user_ip)s\t%(user_agent)s\t%(svr_protocol)s\t%(req_method)s\t%(full_path)s\t%(message)s',
            datefmt='%y-%m-%d %H:%M:%S')

        # input image path 설정
        super().__init__()
        self.__logger.addFilter(self)
        self.set_request_info()

    def info(self,message,**kwargs):
        """
        info log를 남깁니다.
        Logger 초기화시 td_log 가 True이면
        kwargs를 추가하여 td-log를 전송합니다.

        :param message: 메세지
        :param kwargs: td log에 추가할 키워드 파라미터
        :return:
        """

        for k,v in kwargs.items():
            self.__logger.info('{}\t{}'.format(k,v))
        self.__logger.info(message)

    def warning(self,message):
        self.__logger.warning(message)

    def error(self,message):
        self.__logger.error(message)

    def set_request_info(self,
                         userIp=None,
                         user_agent=None,
                         svr_protocol=None,
                         req_method=None,
                         path=None,
                         full_path=None,
                         host=None,
                         language=None,
                         deviceId=None,
                         appType=None,
                         userNo=None
                         ):
        """
        input으로 들어온 데이터를 로그에 기록합니다.

        :param user_ip: user ip
        :param user_agent: user agent
        :param svr_protocol:  server protocol
        :param req_method: GET or POST
        :param full_path: url full_path
        :return:
        """

        self.userIp = userIp
        self.user_agent = user_agent
        self.svr_protocol=svr_protocol
        self.req_method=req_method
        self.path=path
        self.full_path=full_path
        self.host=host
        self.accept_language=language
        self.deviceId=deviceId
        self.appType=appType
        self.userNo=userNo

    def filter(self, record):
        """
        오버로딩 메소드
        로그에 input 이미지 경로를 나타내는 필터

        Autor : hian

        :param record: input data
        :return:

        """

        record.user_ip = self.userIp
        record.user_agent = self.user_agent
        record.svr_protocol = self.svr_protocol
        record.req_method = self.req_method
        record.full_path = self.full_path
        return True

    @staticmethod
    def _get_today():
        """
        YY-MM-DD 형식의 오늘날짜를 str으로 반환(eg. '18-07-08')
        :return: str, 오늘날짜
        """

        ctime_list = time.ctime().split(' ')
        today = ctime_list[-1][2:]+'-'+monthes[ctime_list[1]]+'-'+'%02d' % int(ctime_list[-3])

        return today