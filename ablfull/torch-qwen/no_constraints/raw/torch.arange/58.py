import torch

# Generate input data: start=0, end=5 (exclusive), step=1
input_data = torch.arange(0, 5, 1)

# Call the API
result = torch.arange(input_data)
print(result)