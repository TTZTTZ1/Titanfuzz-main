import torch

def test_torch_nn_fold():
    # Define input tensor and parameters for Fold operation
    input_tensor = torch.randn(1, 32, 8, 8)
    output_size = (4, 4)
    kernel_size = (2, 2)
    stride = (2, 2)
    
    # Create a Fold layer
    fold_layer = torch.nn.Fold(output_size=output_size, kernel_size=kernel_size, stride=stride)
    
    # Apply the Fold layer to the input tensor
    folded_output = fold_layer(input_tensor)
    
    # Print the shape of the output tensor to verify correctness
    print(f"Input tensor shape: {input_tensor.shape}")
    print(f"Folded output tensor shape: {folded_output.shape}")

# Call the function to test the Fold layer
test_torch_nn_fold()