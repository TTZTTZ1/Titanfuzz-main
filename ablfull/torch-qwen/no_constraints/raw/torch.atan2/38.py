import torch

# Task 2: Generate input data
input_data = torch.tensor([0.5, -0.5], dtype=torch.float32)

# Task 3: Call the API torch.atan2
result = torch.atan2(input_data[0], input_data[1])