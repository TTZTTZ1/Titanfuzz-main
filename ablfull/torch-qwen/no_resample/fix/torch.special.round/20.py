import torch
input_tensor = torch.tensor([1.5, (- 0.7), 3.2, (- 4.8)])
result = torch.special.round(input_tensor)
print(result)