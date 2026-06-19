import torch
input_tensor = torch.randn(1, 3, 224, 224)
dropout_layer = torch.nn.Dropout2d(p=0.3)
output_tensor = dropout_layer(input_tensor)