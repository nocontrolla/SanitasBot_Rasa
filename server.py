
from sanic import Sanic, response
from rasa.core.agent import Agent
from rasa.core.channels.socketio import SocketIOInput

app = Sanic(__name__)

# Load your trained Rasa model
model_path = "/home/iamequanimity/development/SanitasBot_Rasa/models/20230515-102214-animato-seller.tar.gz"
agent = Agent.load(model_path)

# Create a SocketIO input channel
input_channel = SocketIOInput(
    user_message_evt='user_uttered',
    bot_message_evt='bot_uttered',
    namespace='/chat'
)

@app.route("/")
async def hello(request):
    return response.text("Hello, Rasa server is running!")

# Define a request handler for incoming user messages
@app.post("/webhooks/socketio/webhook")
async def handle_message(request):
    response = await input_channel.handle_message(request.json, agent.handle_message)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
