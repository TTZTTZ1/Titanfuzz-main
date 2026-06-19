import torch
input_data = torch.tensor([(- 1.5), (- 0.2), 0.0, 0.7, 2.3])
result = torch.fix(input_data)
print(result)