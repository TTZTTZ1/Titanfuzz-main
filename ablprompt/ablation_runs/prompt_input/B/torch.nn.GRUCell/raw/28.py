import torch

# Define the input size, hidden size, and number of layers
input_size = 10
hidden_size = 20
num_layers = 3

# Create a random input sequence and initial hidden state
batch_size = 5
seq_len = 4
input_seq = torch.randn(seq_len, batch_size, input_size)
h0 = torch.randn(num_layers, batch_size, hidden_size)

# Initialize the GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Forward pass through the GRUCell
for t in range(seq_len):
    h_t = gru_cell(input_seq[t], h0)
    print(f"Hidden state at time {t}: {h_t}")

# Print final hidden state
print(f"Final hidden state: {h_t}")