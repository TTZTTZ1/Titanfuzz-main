import torch
input_tensor = torch.tensor((- float('inf')))
result = torch.isneginf(input_tensor)
print(result)