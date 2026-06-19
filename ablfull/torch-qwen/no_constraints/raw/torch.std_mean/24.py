import torch

# Task 2: Generate input data
input_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# Task 3: Call the API torch.std_mean
result = torch.std_mean(input_tensor)

print(result)