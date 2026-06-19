import torch

# Task 2: Generate input data
input_data = torch.tensor([1.0, 2.0, 3.0, 4.0], dtype=torch.float32)

# Task 3: Call the API
result = torch.std_mean(input_data)

print(result)