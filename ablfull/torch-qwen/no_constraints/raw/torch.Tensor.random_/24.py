import torch

# Task 2: Generate input data
input_data = (5,)  # Example shape for random tensor generation

# Task 3: Call the API
result = torch.Tensor().random_(*input_data)
print(result)