import torch

# Prepare input data
input_data = torch.tensor([1.0, 2.0, 3.0, 4.0], dtype=torch.float32)

# Call the API
result = torch.std_mean(input_data, dim=0)
print(result)