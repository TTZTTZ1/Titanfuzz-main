import torch
wrap_storage = None
args = (5,)
result = torch.QInt32Storage(*args, wrap_storage=wrap_storage)