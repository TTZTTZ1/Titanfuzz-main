import torch
input_data = torch.tensor([1.5, (- 2.3), 0.7, (- 0.9)])
result = torch.special.round(input_data)
print(result)