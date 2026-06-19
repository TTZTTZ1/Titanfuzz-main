import torch

# Task 2: Generate input data
input_data = torch.tensor([-1.7, -0.5, 0.2, 1.8], dtype=torch.float32)

# Task 3: Call the API torch.ceil
result = torch.ceil(input_data)
print(result)