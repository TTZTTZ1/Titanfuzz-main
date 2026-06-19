import torch

# Create an instance of SiLU (Sigmoid Linear Unit)
silu = torch.nn.SiLU()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply SiLU to the input tensor
output_tensor = silu(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after applying SiLU:", output_tensor)