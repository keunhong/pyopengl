'''OpenGL extension EXT.texture_sRGB_decode

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_texture_sRGB_decode'
_DEPRECATED = False
GL_TEXTURE_SRGB_DECODE_EXT = constant.Constant( 'GL_TEXTURE_SRGB_DECODE_EXT', 0x8A48 )
GL_DECODE_EXT = constant.Constant( 'GL_DECODE_EXT', 0x8A49 )
GL_SKIP_DECODE_EXT = constant.Constant( 'GL_SKIP_DECODE_EXT', 0x8A4A )


def glInitTextureSrgbDecodeEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
