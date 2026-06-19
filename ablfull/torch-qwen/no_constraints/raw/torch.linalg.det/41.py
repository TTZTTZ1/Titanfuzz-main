import torch

# Task 2: Generate input data
input_data = torch.tensor([[4, 7], [2, 6]], dtype=torch.float32)

# Task 3: Call the API torch.linalg.det
result = torch.linalg.det(input_data)
print(result)