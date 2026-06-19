import torch

class DummyModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 5)

    def forward(self, x):
        return self.linear(x)

def dummy_function(x):
    return DummyModule()(x)

functions = [dummy_function] * 4
segments = 2
input_data = torch.randn(1, 5)

result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_data, use_reentrant=True)