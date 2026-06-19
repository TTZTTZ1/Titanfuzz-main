
import torch
data = [0, 127]
result = torch.QUInt8Storage(data)
print(result)
