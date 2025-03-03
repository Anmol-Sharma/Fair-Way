echo "🚀 Starting Ollama service..."
# Start Ollama in the background.
ollama serve &
# Record Process ID.
pid=$!

# Give more time for Ollama to start properly
echo "⏳ Waiting for Ollama to initialize..."
sleep 10

echo "📋 Current Model List:"
ollama list || echo "❌ Failed to list models"

echo "🔴 Retrieving models..."
for model in "phi4:14b-q8_0" "llama3.1:8b-instruct-q8_0" "mistral-small:24b-instruct-2501-q8_0"; do
  echo "📥 Pulling model: $model"
  ollama pull $model || echo "❌ Failed to pull model: $model"
  echo "✅ Finished pulling: $model"
done

echo "🟢 Done! All models processed"

# Wait for Ollama process to finish.
wait $pid