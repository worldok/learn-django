import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeItMiddleware(MiddlewareMixin):
    # 执行的第一个方法
    def process_request(self, request):
        self.start_time = time.time()
        return

    # 执行中的第二个方法 处理需要统计的时间
    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse('index'):
            return  None

        start = time.time()
        response = func(request)
        costed = time.time() - start
        print('process view: {:.2f}s'.format(costed))
        return response

    # 异常处理
    def process_exception(self, request, exception):
        pass

    # 跟response方法一样 多了有template处理方式
    def process_template_response(self, request, response):
        return response

    # 所有流程处理完毕后来到这里
    def process_response(self, request, response):
        costed = time.time() - self.start_time
        print('request to response cose: {:.2f}s'.format(costed))
        return response

class MiddlewareMixi(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response