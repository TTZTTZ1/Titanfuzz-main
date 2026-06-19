import torch

# Task 2: Generate input data
input_data = torch.randint(0, 10, (3, 4), dtype=torch.int)

# Task 3: Call the API torch.Tensor.float
output_data = input_data.float()