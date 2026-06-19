import torch

# Task 2: Generate input data
input_data = torch.tensor([-0.5, 0.0, 0.5], dtype=torch.float32)

# Task 3: Call the API torch.sin
result = torch.sin(input_data)
print(result)