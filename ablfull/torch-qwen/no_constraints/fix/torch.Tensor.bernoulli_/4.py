import torch
input_tensor = torch.tensor([0.5, 0.7, 0.3])
result = input_tensor.bernoulli_()
print(result)