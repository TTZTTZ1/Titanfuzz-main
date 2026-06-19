import torch

input_data = torch.tensor([-2.0, 0.0, 2.0], dtype=torch.float)
result = torch.nn.functional.hardsigmoid(input_data)