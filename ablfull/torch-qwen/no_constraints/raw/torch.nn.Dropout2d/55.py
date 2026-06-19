import torch

# Prepare input data
input_data = torch.randn(1, 3, 4, 4)

# Call the API
dropout_layer = torch.nn.Dropout2d(p=0.2)
output_data = dropout_layer(input_data)