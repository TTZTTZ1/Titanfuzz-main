
import torch
input_tensor = torch.tensor([float('-inf'), (- 2.0), 0.0, 2.0])
result = torch.isneginf(input_tensor)
print(result)
