import torch

# Task 2: Generate input data
input_data = torch.randint(0, 100, (5,))

# Task 3: Call the API
result = input_data.float()
print(result)