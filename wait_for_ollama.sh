# Start Ollama in the background.
ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "🔴 Retrieving models..."
ollama pull phi4:14b-q8_0
ollama pull llama3.1:8b-instruct-q8_0
echo "🟢 Done!"

# Wait for Ollama process to finish.
wait $pid