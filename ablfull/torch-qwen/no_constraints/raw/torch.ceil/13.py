import torch

# Task 2: Generate input data
input_data = torch.tensor([-1.7, -1.5, -0.2, 0.0, 0.2, 1.5, 1.7], dtype=torch.float32)

# Task 3: Call the API torch.ceil
result = torch.ceil(input_data)
print(result)