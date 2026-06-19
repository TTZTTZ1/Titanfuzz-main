import torch
input_data = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0], dtype=torch.float32)
result = torch.special.logit(input_data)
print(result)