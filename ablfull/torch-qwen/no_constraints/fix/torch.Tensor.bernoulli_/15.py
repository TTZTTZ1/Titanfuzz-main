import torch
tensor = torch.rand(4)
result = tensor.bernoulli_()
print(result)