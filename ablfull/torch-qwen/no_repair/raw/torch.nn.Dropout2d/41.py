import torch

# Generate input data
input_tensor = torch.randn(1, 3, 4, 4)

# Call the API
dropout_layer = torch.nn.Dropout2d(p=0.3)
output_tensor = dropout_layer(input_tensor)