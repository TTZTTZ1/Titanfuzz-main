import torch
import torch.nn as nn

# Define a simple model using Conv2d
class SimpleConvModel(nn.Module):
    def __init__(self):
        super(SimpleConvModel, self).__init__()
        self.conv_layer = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1), bias=True)

    def forward(self, x):
        return self.conv_layer(x)

# Create an instance of the model and print its architecture
model = SimpleConvModel()
print(model)