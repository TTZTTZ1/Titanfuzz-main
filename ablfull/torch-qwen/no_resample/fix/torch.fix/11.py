import torch
input_tensor = torch.tensor([(- 1.5), 0.2, 3.8])
result = torch.fix(input_tensor)
print(result)