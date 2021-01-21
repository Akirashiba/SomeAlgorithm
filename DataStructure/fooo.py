填空
1. output [0]
2. output [1, 1]
3. output [2]

4. output 1, 1, 1
5. output 1, 2, 1
6. output 3, 1, 1

7. output [0, 2, 4, 6]

简答
1、API接口实现跨域
2、404 资源没找到
   403 
   302 
   304 
   500 服务器错误
   200 正常返回
3、__new__ 是初始化类
   __init__ 是初始化实例
4、cpython 自带的全局变量锁
5、引用计数 标记清除(解决自己引用自己) 分代回收

编程
import time
from collections import defaultdict
def cache(sec):
	_cache = defaultdict(dict)
	def wrapper(func):
		def inner_wrapper(kw):
			if kw not in _cache:
				_cache[kw]['last'] = int(time.time())
				_cache[kw]['result'] = func(kw) 
				return _cache[kw]['result']
			else:
				if int(time.time()) - _cache[kw]['last'] >= sec:
					_cache[kw]['last'] = int(time.time())
					_cache[kw]['result'] = func(kw) 
				return _cache[kw]['result']
		return inner_wrapper
	return wrapper

def foo(start, end):
	return range(start, end)


def step(n):
	if n <= 0:
		return 0
	if n == 1:
		return 1
	if n == 2:
		return 2
	return step(n-1) + step(n-2)


def foo2(L):
	result = []
	for index, i in enumerate(L):
		if not index:
			result.append(i)
		else:
			if i > L[:index] and i < L[index+1:]:
				result.append(i)
	return result

