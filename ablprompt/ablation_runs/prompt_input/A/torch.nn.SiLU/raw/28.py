import torch

# Create an instance of SiLU (Sigmoid Linear Unit)
silu = torch.nn.SiLU()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply the SiLU function to the input tensor
output_tensor = silu(input_tensor)

print(output_tensor)