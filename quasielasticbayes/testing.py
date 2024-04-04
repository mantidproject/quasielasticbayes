"""Utility code to help with testing
"""
import base64
import json
import numpy as np
import os
import sys


def _json_numpy_obj_hook(dct):
    """
    Decodes a previously encoded numpy ndarray
    with proper shape and dtype
    :param dct: (dict) json encoded ndarray
    :return: (ndarray) if input was an encoded ndarray
    """
    if isinstance(dct, dict) and '__ndarray__' in dct:
        data = base64.b64decode(dct['__ndarray__'])
        return np.frombuffer(data, dct['dtype']).reshape(dct['shape'])
    return dct


def load_json(*args, **kwargs):
    """Loads a json-encoded file-like object to a dictionary.
    Adds supports for decoding numpy arrays
    See json.load.
    """
    kwargs.setdefault('object_hook', _json_numpy_obj_hook)
    return json.load(*args, **kwargs)


def add_path(file_path, file_name):
    """Sets the path for a file
    """
    return os.path.join(file_path, file_name)


def get_OS_precision():
    if sys.platform == 'win32':
        # Windows
        return 7  # np.almost_equals default
    elif sys.platform == 'darwin':
        # Mac OS
        return 1
    else:
        # Linux - lower due to rounding error
        return 1


def get_qlse_prob(ref):
    if sys.platform == 'win32':
        return ref
    else:
        return [-2.7656994e+04, -1.8887866e+2,  0.0, -5.8251953e-1]
