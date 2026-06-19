import torch

# Task 2: Generate input data
input_data = torch.tensor([[4., 0.], [0., 3.]], dtype=torch.float32)

# Task 3: Call the API torch.slogdet
result = torch.slogdet(input_data)
print(result)