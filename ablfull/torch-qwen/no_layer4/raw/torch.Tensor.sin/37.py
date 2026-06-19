import torch

# Task 2: Generate input data
input_data = torch.tensor([0.0, math.pi/4, math.pi/2])

# Task 3: Call the API torch.Tensor.sin
output = torch.sin(input_data)
print(output)