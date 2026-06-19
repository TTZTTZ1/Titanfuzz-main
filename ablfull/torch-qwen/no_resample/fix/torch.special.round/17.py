import torch
input_tensor = torch.tensor([1.5, (- 0.4), 3.7])
result = torch.special.round(input_tensor)
print(result)