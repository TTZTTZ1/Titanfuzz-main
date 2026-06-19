import torch

input_data = [0, 1, 2, 3, 4]
storage = torch.QuantizedStorage()
result = torch.QUInt8Storage(input_data, wrap_storage=storage)