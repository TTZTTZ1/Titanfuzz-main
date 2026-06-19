import torch

class SimpleFunction(torch.nn.Module):

    def __init__(self):
        super(SimpleFunction, self).__init__()
        self.linear = torch.nn.Linear(5, 5)

    def forward(self, x):
        return self.linear(x)
functions = [SimpleFunction(), SimpleFunction()]
input_data = torch.randn(1, 5)
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments=1, input=input_data)