<template>
  <div class="chat max-w-lg max-h-120 border border-gray-300 m-6">

    <div class="w-full">
      
      <ChatHeader />

      <div class="relative w-full p-6 overflow-y-auto">

        <ul class="chat_messages space-y-2">

          <ChatMessage message="Hi" :income=true />

          <ChatMessage message="Hiiii" />

          <ChatMessage message="how are you?" />

          <ChatMessage message="Lorem ipsum dolor sit, amet consectetur adipisicing elit." :income=true />
         
        </ul>

      </div>

      <ChatFooter />
    </div>
  </div>
</template>

<script>
import { useWebSocket } from '@vueuse/core'
import { v4 as uuidv4 } from 'uuid';
import { inject } from 'vue';

export default {
  setup() {
    const store = inject('store');

    return {
      store
    }
    // const { send } = useWebSocket(`ws://localhost:8765`, {
    //   onMessage(ws, event) {
    //       console.log('data', event);
    //   },
    //   autoReconnect: {
    //     retries: 3,
    //     delay: 1000,
    //     onFailed() {
    //       alert('Failed to connect WebSocket after 3 retries')
    //     }
    //   },
    // })

    // send('yopt');
  }
}
</script>