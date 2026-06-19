import torch

# Define the LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size=10, hidden_size=20)

# Initialize input and hidden/cell states
input_tensor = torch.randn(5, 10)  # Batch size of 5, input size of 10
hidden_state = torch.zeros(5, 20)   # Batch size of 5, hidden size of 20
cell_state = torch.zeros(5, 20)     # Batch size of 5, hidden size of 20

# Process the input through the LSTMCell
for i in range(input_tensor.size(0)):
    hidden_state, cell_state = lstm_cell(input_tensor[i], (hidden_state, cell_state))

print("Final Hidden State:", hidden_state)
print("Final Cell State:", cell_state)