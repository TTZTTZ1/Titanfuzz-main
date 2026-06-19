import torch
input_data = torch.randn(1, 3, 4, 4)
dropout_layer = torch.nn.Dropout2d(p=0.2)
output_data = dropout_layer(input_data)