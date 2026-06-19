import torch

# Prepare input data
input_data = torch.randn(1, 3, 224, 224)

# Call the API
dropout_layer = torch.nn.Dropout2d(p=0.5, inplace=False)
output = dropout_layer(input_data)