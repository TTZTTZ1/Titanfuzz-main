import torch

input_data = [1, 2, 3]
storage = torch.tensor(input_data, dtype=torch.uint8)
result = torch.QUInt8Storage(wrap_storage=storage, dtype=torch.uint8)