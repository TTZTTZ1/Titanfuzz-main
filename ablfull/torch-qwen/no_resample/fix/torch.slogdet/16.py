import torch
input_tensor = ((torch.rand((3, 3)) * 2) - 1)
input_tensor = input_tensor.float()
result = torch.slogdet(input_tensor)
print(result)