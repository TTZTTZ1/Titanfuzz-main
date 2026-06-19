import torch
input_tensor = torch.tensor([4.0])
divisor = torch.tensor([2.0])
result = torch.divide(input_tensor, divisor)
print(result)