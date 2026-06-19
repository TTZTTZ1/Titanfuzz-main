import torch

# Prepare valid input data
input_data = torch.randn(3, 4, 5)

# Call the API
output_data = input_data.float(memory_format="preserve_format")

print(output_data)