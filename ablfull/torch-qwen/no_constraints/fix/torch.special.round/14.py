import torch
input_data = torch.tensor([1.5, (- 2.3), 4.8, (- 0.7)])
result = torch.special.round(input_data)
print(result)