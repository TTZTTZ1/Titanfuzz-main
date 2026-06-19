import torch

# Prepare valid input data
input_data = torch.randn(10, 5, 8)
mat2_data = torch.randn(10, 8, 3)

# Call the target API
result = torch.bmm(input_data, mat2_data)
print(result.shape)  # Output should be torch.Size([10, 5, 3])