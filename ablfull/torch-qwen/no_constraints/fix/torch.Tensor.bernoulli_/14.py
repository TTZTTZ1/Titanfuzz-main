import torch
input_data = torch.tensor([0.5, 0.7, 0.8])
result = input_data.bernoulli_()
print(result)