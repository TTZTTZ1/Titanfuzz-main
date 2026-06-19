
import torch
input_data = torch.randn(1, 3, 28, 28)
dropout_layer = torch.nn.Dropout2d(p=0.5)
output_data = dropout_layer(input_data)
