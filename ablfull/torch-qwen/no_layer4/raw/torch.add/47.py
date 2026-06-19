import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
other_tensor = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

# Task 3: Call the API torch.add
result = torch.add(input_tensor, other_tensor)

print(result)