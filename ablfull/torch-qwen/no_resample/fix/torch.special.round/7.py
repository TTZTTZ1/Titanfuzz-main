import torch
input_tensor = torch.tensor([0.5, (- 0.5), 1.2, (- 1.7)])
result = torch.special.round(input_tensor)
print(result)