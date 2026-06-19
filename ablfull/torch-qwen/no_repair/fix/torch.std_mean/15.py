
import torch
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
result = torch.std_mean(input_tensor, dim=0, correction=1, keepdim=True)
