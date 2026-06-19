
import torch
input_tensor = torch.tensor([(- 1.0), 0.5, 1.0])
output_tensor = torch.nn.functional.hardsigmoid(input_tensor)
