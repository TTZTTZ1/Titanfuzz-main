import torch

# Define the model parameters
input_size = 10
hidden_size = 20

# Create an instance of LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Initialize input and hidden state
input_data = torch.randn(5, input_size)  # Sequence length of 5
hx = torch.zeros(5, hidden_size)        # Hidden state
cx = torch.zeros(5, hidden_size)        # Cell state

# Process each time step
for i in range(input_data.size(0)):
    hx, cx = lstm_cell(input_data[i], (hx, cx))

# Output the final hidden state
print(hx)