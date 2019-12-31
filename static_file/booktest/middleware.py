#
# from django.utils.deprecation import MiddlewareMixin
# from django.shortcuts import HttpResponse
#
#
# # __init__:服务器响应第一个请求的时候调用。
# # process_request:是在产生request对象，进行url匹配之前调用。
# # process_view：是url匹配之后，调用视图函数之前。
# # process_response：视图函数调用之后，内容返回给浏览器之前。
# # process_exception:视图函数出现异常，会调用这个函数。
#
# # 类名可以自定义，其中的函数名为固定的
# class BlockedIPSMiddleware(MiddlewareMixin):
#     """中间件类"""
#     EXCLUDE_IP = ['127.0.0.6']
#
#     def process_view(self, request, view_func, *view_args, **view_kwargs):
#         """视图函数调用之前会调用"""
#         user_ip = request.META.get('REMOTE_ADDR')
#         print(user_ip)
#         if user_ip in BlockedIPSMiddleware.EXCLUDE_IP:
#             return HttpResponse('<h1>Forbidden</h1>')
#
#
# class Row1(MiddlewareMixin):
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.
#
#     def process_request(self, request):
#         print('中间件1的请求')
#
#     def process_response(self, request, response):
#         print('中间件1的返回')
#         return response
#
#     def __call__(self, request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#
#         print('中间件1的 view前调用')
#         response = self.get_response(request)
#
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#
#         print('中间件1的 view之后调用')
#
#         return response
#
#
# class Row2(MiddlewareMixin):
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.
#
#     def process_request(self, request):
#         print('中间件2的请求')
#         # return HttpResponse('前端显示：中间件：M2.process_request')
#
#     def process_response(self, request, response):
#         print('中间件2的返回')
#         return response
#
#     def __call__(self, request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#
#         print('中间件2的 view前调用')
#         response = self.get_response(request)
#
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#
#         print('中间件2的 view之后调用')
#
#         return response
#
#
# class Row3(MiddlewareMixin):
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.
#
#     def process_request(self, request):
#         print('中间件3的请求')
#
#     def process_response(self, request, response):
#         print('中间件3的返回')
#         return response
#
#     def process_view(self, request, callback, callback_args, callback_kwargs):
#         print('中间件3的 view')