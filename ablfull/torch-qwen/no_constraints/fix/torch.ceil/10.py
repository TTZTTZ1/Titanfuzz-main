import torch
input_data = torch.tensor([(- 1.7), (- 1.5), (- 0.2), 0.0, 0.2, 1.5, 1.7], dtype=torch.float32)
result = torch.ceil(input_data)
print(result)