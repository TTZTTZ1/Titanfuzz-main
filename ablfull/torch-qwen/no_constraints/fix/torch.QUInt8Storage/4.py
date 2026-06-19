import torch
data = torch.randint(0, 256, (10,), dtype=torch.uint8)
storage = torch.QUInt8Storage(data.tolist())