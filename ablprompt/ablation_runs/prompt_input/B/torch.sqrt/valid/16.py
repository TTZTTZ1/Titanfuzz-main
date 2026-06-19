import torch

# Create a random tensor with negative values to demonstrate handling of nan
input_tensor = torch.tensor([-1.0, 4.0, 9.0], dtype=torch.float32)
result = torch.sqrt(input_tensor)
print(result)  # Output will include nan for -1.0