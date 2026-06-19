import torch

# Create a tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float32)

# Call the tan function
output_tensor = torch.tan(input_tensor)

print(output_tensor)