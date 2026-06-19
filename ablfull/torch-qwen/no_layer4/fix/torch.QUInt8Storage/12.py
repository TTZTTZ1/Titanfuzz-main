import torch
data = torch.tensor([1, 2, 3], dtype=torch.uint8)
storage = torch.QUInt8Storage(data.tolist())