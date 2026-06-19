import torch

# Create an instance of Softplus
softplus = torch.nn.Softplus()

# Define some input data
input_data = torch.tensor([-1.0, 0.0, 1.0])

# Apply Softplus to the input data
output_data = softplus(input_data)

print("Input Data:", input_data)
print("Output Data:", output_data)