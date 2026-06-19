
import torch
input_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0], dtype=torch.float32)
(std, mean) = torch.std_mean(input_tensor, dim=0, correction=1, keepdim=False)
print(std, mean)
