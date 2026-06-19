import torch

# Task 2: Generate input data
input_tensor = torch.randint(0, 256, (4, 3, 224, 224), dtype=torch.uint8)
scale_tensor = torch.tensor([0.5, 1.0, 2.0], dtype=torch.float32)

# Task 3: Call the API
result = torch.quantization.observer.calculate_qparams(input_tensor, scale_tensor, axis=0)
print(result)