import torch

# Generate input data
input_data = torch.tensor([1.0, -float('inf'), float('nan'), 2.5])

# Call the API
result = torch.isfinite(input_data)

print(result)