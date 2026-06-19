
import torch
input_data = torch.tensor([(- 1.5), (- 0.2), 0.7, 2.3], dtype=torch.float)
result = torch.ceil(input_data)
print(result)
