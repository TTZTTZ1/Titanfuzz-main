import torch

# Generate valid input data
input_data = torch.tensor([0.0, 0.5, 1.0])

# Call the API
result = torch.sin(input_data)
print(result)