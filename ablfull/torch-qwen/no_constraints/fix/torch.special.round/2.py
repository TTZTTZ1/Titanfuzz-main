import torch
input_data = torch.tensor([(- 1.5), (- 0.3), 0.7, 1.4])
result = torch.special.round(input_data)
print(result)