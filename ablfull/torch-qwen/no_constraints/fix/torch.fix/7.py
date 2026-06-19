import torch
input_data = torch.tensor([(- 1.5), (- 0.3), 0.7, 1.9])
result = torch.fix(input_data)
print(result)