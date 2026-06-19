import torch
data = torch.randint(0, 256, (10,), dtype=torch.uint8)
storage = torch.QInt32Storage(wrap_storage=data.untyped_storage())