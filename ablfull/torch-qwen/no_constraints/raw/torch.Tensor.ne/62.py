import torch

# Generate input data
input_data = torch.tensor([1.0, 2.0, 3.0])

# Call the API
result = input_data.ne(2.0)

print(result)