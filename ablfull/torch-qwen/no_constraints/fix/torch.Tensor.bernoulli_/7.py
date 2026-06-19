import torch
input_data = torch.tensor([0.5, 0.7, 0.3], dtype=torch.float32)
result = input_data.bernoulli_()
print(result)