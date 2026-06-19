import torch
input_tensor = torch.ones(3)
result = input_tensor.bernoulli_()
print(result)