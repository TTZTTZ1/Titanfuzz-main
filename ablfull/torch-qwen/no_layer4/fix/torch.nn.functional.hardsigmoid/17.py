import torch
input_tensor = torch.tensor([(- 1.0), 0.5, 1.5], dtype=torch.float)
output_tensor = torch.nn.functional.hardsigmoid(input_tensor)
print(output_tensor)