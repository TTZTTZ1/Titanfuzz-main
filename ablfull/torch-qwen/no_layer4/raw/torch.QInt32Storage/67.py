import torch

storage = torch.tensor([1, 2, 3], dtype=torch.qint32)
result = torch.QInt32Storage(wrap_storage=storage)