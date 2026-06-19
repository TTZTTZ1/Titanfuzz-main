import torch

# Task 2: Generate input data
def simple_function(x):
    return x * x

functions = [simple_function]
segments = 1
input_data = torch.tensor([1.0, 2.0, 3.0])

# Task 3: Call the API
result = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_data)
print(result)