import torch
input_tensor = torch.tensor([0.5, 0.7, 0.3], dtype=torch.float)
result_tensor = input_tensor.bernoulli_()
print(result_tensor)