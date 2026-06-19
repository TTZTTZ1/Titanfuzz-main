import torch
from torch.nn import Sequential, Linear

# Define some random functions
class RandomFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input):
        ctx.save_for_backward(input)
        return input + 1

    @staticmethod
    def backward(ctx, grad_output):
        input, = ctx.saved_tensors
        return grad_output

random_function1 = lambda x: RandomFunction.apply(x)
random_function2 = lambda x: RandomFunction.apply(x)

functions = [random_function1, random_function2]
segments = 2
input_tensor = torch.randn(3)

result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor)
print(result)