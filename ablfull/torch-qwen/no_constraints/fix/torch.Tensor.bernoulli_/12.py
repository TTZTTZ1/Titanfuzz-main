import torch
input_tensor = torch.tensor([0.5, 0.7, 0.3])
output_tensor = input_tensor.bernoulli_()
print(output_tensor)