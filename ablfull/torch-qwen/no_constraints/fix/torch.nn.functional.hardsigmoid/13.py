import torch
input_data = torch.tensor([(- 2.0), (- 1.5), 0.0, 1.5, 2.0])
result = torch.nn.functional.hardsigmoid(input_data)
print(result)