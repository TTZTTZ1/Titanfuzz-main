import torch
input_tensor = torch.tensor([1.5, (- 0.4), 2.7, (- 3.2)])
result = torch.special.round(input_tensor)
print(result)