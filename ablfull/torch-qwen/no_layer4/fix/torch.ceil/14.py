import torch
input_tensor = torch.tensor([(- 1.7), (- 1.5), (- 0.2), 0.0, 0.2, 1.5, 1.7], dtype=torch.float)
result = torch.ceil(input_tensor)
print(result)