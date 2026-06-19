import torch

input_data = [100, 200, 300]
storage = torch.tensor(input_data, dtype=torch.uint8)
quint8_storage = torch.QUInt8Storage(wrap_storage=storage)