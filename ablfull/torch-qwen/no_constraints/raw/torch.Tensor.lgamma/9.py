import torch

# Task 2: Generate input data
input_data = torch.tensor([1.0, 2.5, 4.0])

# Task 3: Call the API
result = input_data.lgamma()

print(result)