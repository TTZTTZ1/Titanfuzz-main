import torch
input_tensor = torch.tensor([(- 1.5), (- 0.4), 0.0, 0.6, 1.9], dtype=torch.float)
result = torch.ceil(input_tensor)
print(result)