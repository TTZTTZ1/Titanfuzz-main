
import torch
p = 0.7
input_tensor = torch.zeros(3, 4)
result = input_tensor.bernoulli_(p)
