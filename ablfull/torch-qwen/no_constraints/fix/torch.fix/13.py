import torch
input_data = torch.tensor([(- 1.5), 0.2, 4.7])
result = torch.fix(input_data)
print(result)