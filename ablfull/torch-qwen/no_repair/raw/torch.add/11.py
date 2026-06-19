import torch

# Prepare input data
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float)
other_tensor = torch.tensor([[5.0, 6.0], [7.0, 8.0]], dtype=torch.float)

# Call the API
result = torch.add(input_tensor, other_tensor)