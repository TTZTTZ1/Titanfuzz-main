import torch

# Prepare input data
input_tensor = torch.randn(1, 3, 32, 32)

# Call the API
dropout_layer = torch.nn.Dropout2d(p=0.2, inplace=False)
output_tensor = dropout_layer(input_tensor)