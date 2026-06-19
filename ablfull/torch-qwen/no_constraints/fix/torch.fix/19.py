import torch
input_tensor = torch.tensor([(- 1.5), (- 0.7), 0.2, 1.8])
result = torch.fix(input_tensor)
print(result)