import numpy as np
import torch

def is_numpy(data):
    # check if data is a numpy array
    return isinstance(data, np.ndarray)

def is_tensor(data):
    # check if data is a torch tensor
    return torch.is_tensor(data)
    # this function is simply doing isinstance(obj, Tensor)

def is_tuple(data):
    return isinstance(data, tuple)


def is_tuple(data):
    """Checks if data is a tuple."""
    return isinstance(data, tuple)

def is_list(data):
    """Checks if data is a list."""
    return isinstance(data, list)

def is_dict(data):
    """Checks if data is a dictionary."""
    return isinstance(data, dict)

def is_str(data):
    """Checks if data is a string."""
    return isinstance(data, str)

def is_int(data):
    """Checks if data is an integer."""
    return isinstance(data, int)

def is_seq(data):
    '''
    checks if data is a list or tuple
    '''
    return is_tuple(data) or is_list(data)




