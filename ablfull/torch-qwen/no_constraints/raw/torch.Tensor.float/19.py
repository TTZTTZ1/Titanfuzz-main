import torch

# Generate input data
input_data = torch.tensor([1, 2, 3], dtype=torch.int32)

# Call the API
output_tensor = input_data.float()

print(output_tensor)