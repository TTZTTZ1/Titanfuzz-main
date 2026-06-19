import torch
p = 0.7
input_tensor = torch.tensor([0.3, 0.8, 0.4])
result = input_tensor.bernoulli_(p)
print(result)