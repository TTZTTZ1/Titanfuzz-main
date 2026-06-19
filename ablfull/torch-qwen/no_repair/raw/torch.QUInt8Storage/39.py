import torch

input_data = torch.tensor([0, 1, 2], dtype=torch.uint8)
storage = torch.QUInt8Storage(input_data)