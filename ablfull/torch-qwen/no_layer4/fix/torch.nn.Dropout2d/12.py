import torch
input_data = torch.randn(1, 3, 224, 224)
dropout_layer = torch.nn.Dropout2d(p=0.7)
output_data = dropout_layer(input_data)