import torch

# Create a random tensor
x = torch.randn(5, 5)

# Define indices to select
indices = torch.tensor([0, 2, 4])

# Select rows using torch.index_select
selected_rows = torch.index_select(x, 0, indices)

print("Original Tensor:")
print(x)
print("\nSelected Rows:")
print(selected_rows)