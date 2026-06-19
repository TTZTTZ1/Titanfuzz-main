import torch

# Create a sample input tensor
input_tensor = torch.randn(5, 3)

# Define the indices to select
indices = torch.tensor([0, 2])

# Use torch.index_select to select rows 0 and 2 from the input tensor
selected_tensor = torch.index_select(input_tensor, 0, indices)

print("Original Tensor:")
print(input_tensor)
print("\nSelected Tensor:")
print(selected_tensor)