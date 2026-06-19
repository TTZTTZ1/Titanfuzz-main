
import torch
input_tensor = torch.tensor([(- 0.5), 0.0, 0.5], dtype=torch.float)
output_tensor = torch.nn.functional.hardsigmoid(input_tensor)
print(output_tensor)
