import torch

# Task 2: Generate input data - create a tensor of random integers
input_data = torch.randint(0, 10, (3, 3)).float()

# Task 3: Call the API torch.Tensor.double
output_data = input_data.double()