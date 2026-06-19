import torch
input_tensor = torch.tensor([(- 1.5), (- 0.3), 0.7, 1.2])
result = torch.fix(input_tensor)
print(result)