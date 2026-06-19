import torch

# Initialize the GRUCell
gru_cell = torch.nn.GRUCell(input_size=10, hidden_size=20)

# Create random input and hidden state
input_tensor = torch.randn(5, 10)  # Batch size of 5, sequence length of 5, feature dimension of 10
hidden_state = torch.randn(5, 20)  # Batch size of 5, hidden state dimension of 20

# Process the input through the GRUCell
updated_hidden_state = gru_cell(input_tensor, hidden_state)

print(updated_hidden_state)