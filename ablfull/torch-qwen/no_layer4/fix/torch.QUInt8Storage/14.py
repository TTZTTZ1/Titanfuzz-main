import torch
data = [42, 0, 255]
storage = torch.QUInt8Storage(data)
print(storage)