unicodetest: unicodetest_wrap.c
	python setup.py build

unicodetest_wrap.c: unicodetest.i
	swig -python -py3 unicodetest.i
