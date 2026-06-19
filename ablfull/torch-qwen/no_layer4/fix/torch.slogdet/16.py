import torch
input_tensor = torch.randn(2, 2)
while (torch.det(input_tensor).item() == 0):
    input_tensor = torch.randn(2, 2)
result = torch.slogdet(input_tensor)
print(result)