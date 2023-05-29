import { ChatWidget } from '@rasahq/rasa-chat';

export  default function MyApp() {
    return (
        <ChatWidget websocketUrl="https://your-rasa-url-here/" />
    );
}