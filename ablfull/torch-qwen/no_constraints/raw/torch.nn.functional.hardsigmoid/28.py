import torch

input_tensor = torch.tensor([-1.0, 0.0, 1.0])
output_tensor = torch.nn.functional.hardsigmoid(input_tensor)