import torch

# Prepare valid input data
input_tensor = torch.randn(4, 4)

# Call the API
output_tensor = input_tensor.float(memory_format="contiguous_format")

print(output_tensor)