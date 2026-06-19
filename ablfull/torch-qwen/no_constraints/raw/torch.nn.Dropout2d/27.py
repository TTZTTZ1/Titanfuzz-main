import torch

# Prepare valid input data
input_data = torch.randn(1, 3, 64, 64)

# Call the API
dropout_layer = torch.nn.Dropout2d(p=0.5)
output_data = dropout_layer(input_data)