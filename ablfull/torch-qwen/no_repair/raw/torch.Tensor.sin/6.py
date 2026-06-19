import torch

# Task 2: Generate input data
input_data = torch.tensor([0.0, 1.5708, 3.1416], dtype=torch.float32)

# Task 3: Call the API
result = torch.sin(input_data)