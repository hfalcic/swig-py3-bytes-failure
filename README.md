Introduction
============

This example code exposes a failure in SWIG's default behavior in Python 3.
The default mapping from byte strings (`char *` or `std::string`) to Python
objects attempts to decode those bytes as UTF-8, and when this decoding fails
there is no way to obtain the original byte string if the user wants to use a
different codec or treat the data as a raw sequence of bytes. This behavior can
be overridden in each project, but SWIG's default behavior may as well be as
helpful as possible.

This example code is related to
[SWIG issue #165](https://github.com/swig/swig/pull/165), which changes the
default decoding to use the `surrogateescape` error handler by default.

Usage
=====

Compilation
-----------

Run `make`.

Testing
-------

Enter the appropriate `build` directory, run `python3`, import the SWIG module
and call its test method. With Python 3.4:


    $ cd build/lib.linux-x86_64-3.4/
    $ python3
    Python 3.4.0 (default, Apr 11 2014, 13:05:11) 
    [GCC 4.8.2] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import unicodetest
    >>> unicodetest.test()


Without the patch for SWIG issue 165, this produces the following output:

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 1: invalid continuation byte

With that patch, this produces:

    'h\udce9llo'

<!-- vim: set tw=79: -->
