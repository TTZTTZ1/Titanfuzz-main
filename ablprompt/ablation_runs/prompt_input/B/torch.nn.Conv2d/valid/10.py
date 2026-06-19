import torch
import torch.nn as nn

# Define a simple model using Conv2d
class SimpleConvModel(nn.Module):
    def __init__(self):
        super(SimpleConvModel, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=8, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        return x

# Create an instance of the model and print its architecture
model = SimpleConvModel()
print(model)