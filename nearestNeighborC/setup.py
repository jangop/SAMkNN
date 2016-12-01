 
from distutils.core import setup, Extension

module1 = Extension('libNNPythonIntf',
                    include_dirs = ['/usr/include/python2.7', '/usr/include/python2.7/numpy'],
                    libraries = [],
                    library_dirs = [],
		    extra_compile_args = ['-O3'],
                    sources = ['nearestNeighbor.cpp'])

setup (name = 'PackageName',
       version = '1.0',
       description = 'This is a demo package',
       author = 'Viktor Losing',
       author_email = 'vlosing@techfak.uni-bielefeld.de',
       ext_modules = [module1])
