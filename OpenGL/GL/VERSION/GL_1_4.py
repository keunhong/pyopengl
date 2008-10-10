'''OpenGL extension VERSION.GL_1_4

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_1_4 to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.VERSION.GL_1_4 import *
### END AUTOGENERATED SECTION
glMultiDrawElements = wrapper.wrapper( glMultiDrawElements ).setPyConverter(
	'indices', arrays.AsArrayOfType( 'indices', 'type' ),
).setCResolver( 
	'indices', arrays.ArrayDatatype.voidDataPointer ,
).setPyConverter(
	'count', arrays.AsArrayTyped( 'count', arrays.GLsizeiArray ),
).setCResolver(
	'count', arrays.ArrayDatatype.voidDataPointer ,
)
