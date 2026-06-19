import torch

data = [100]
storage = torch.empty(0)
result = torch.QUInt8Storage(data, wrap_storage=storage)