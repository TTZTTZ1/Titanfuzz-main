import torch

# Task 2: Generate input data
data = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])

# Task 3: Call the API
result = torch.std_mean(data)

print(result)