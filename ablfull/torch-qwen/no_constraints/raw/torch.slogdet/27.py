import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[4.0, 7.0], [2.0, 6.0]], dtype=torch.float32)

# Task 3: Call the API
result = torch.slogdet(input_tensor)
print(result)