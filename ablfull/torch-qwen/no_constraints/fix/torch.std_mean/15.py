import torch
input_tensor = torch.randn(10)
result = torch.std_mean(input_tensor, unbiased=False)
print(result)