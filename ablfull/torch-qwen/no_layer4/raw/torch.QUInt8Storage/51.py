import torch

data = [1, 2, 3, 4]
storage = torch.tensor(data, dtype=torch.uint8)
quint8_storage = torch.QUInt8Storage(wrap_storage=storage)