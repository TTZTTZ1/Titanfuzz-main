import torch

# Generate input data
input_data = torch.randint(0, 100, (5,))

# Call the API
result = input_data.float()

print(result)