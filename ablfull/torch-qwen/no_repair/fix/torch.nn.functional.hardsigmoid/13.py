
import torch
input_tensor = torch.tensor([(- 1.0), 0.0, 1.0], dtype=torch.float)
result = torch.nn.functional.hardsigmoid(input_tensor, inplace=False)
print(result)
