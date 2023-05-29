import { ChatWidget } from '@rasahq/rasa-chat';

export  default function MyApp() {
    return (
        <ChatWidget websocketUrl="http://localhost:5005/" />
    );
}