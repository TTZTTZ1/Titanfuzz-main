import torch
input_data = torch.tensor([0.5, (- 0.3), 1.2])
result = torch.sin(input_data)
print(result)