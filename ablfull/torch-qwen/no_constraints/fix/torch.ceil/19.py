import torch
input_data = torch.tensor([(- 1.5), (- 0.2), 0.0, 0.7, 1.3], dtype=torch.float32)
result = torch.ceil(input_data)
print(result)