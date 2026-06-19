import torch

input_data = [0, 1, 2]
storage = torch.Storage(input_data)
qint8_storage = torch.QUInt8Storage(wrap_storage=storage)