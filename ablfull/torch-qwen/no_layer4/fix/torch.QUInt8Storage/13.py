import torch
data = [0, 1, 2, 3, 4, 5]
result = torch.QUInt8Storage(data)
print(result)