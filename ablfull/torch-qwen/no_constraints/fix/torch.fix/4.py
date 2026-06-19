import torch
input_data = torch.tensor([(- 1.5), (- 0.2), 0.7, 1.8])
result = torch.fix(input_data)
print(result)