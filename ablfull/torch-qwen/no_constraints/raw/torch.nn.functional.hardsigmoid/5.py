import torch

input_data = torch.tensor([-1.0, 0.0, 1.0])
output = torch.nn.functional.hardsigmoid(input_data)