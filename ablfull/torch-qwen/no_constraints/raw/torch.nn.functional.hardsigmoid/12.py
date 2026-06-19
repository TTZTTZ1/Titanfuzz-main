import torch

# Task 2: Generate input data
input_data = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float32)

# Task 3: Call the API
output = torch.nn.functional.hardsigmoid(input_data)
print(output)