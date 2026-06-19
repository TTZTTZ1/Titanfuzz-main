import torch

# Generate sample input data
input_tensor = torch.tensor([[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]])
indices_tensor = torch.tensor([[[0, 1, 2], [3, 4, 5]]])

# Call the API
output_tensor = torch.nn.functional.max_unpool1d(input_tensor, indices_tensor, kernel_size=2, padding=0)

print(output_tensor)