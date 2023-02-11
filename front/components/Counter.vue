<template>
  <div class="p-4 counter">
    <button class="p-2 bg-gradient-to-r from-cyan-500 to-blue-500 text-white" @click="store.methods.decrement">-</button>
    <span class="value p-4">{{ store.state.counter }}</span>
    <button class="p-2 bg-gradient-to-r from-cyan-500 to-blue-500 text-white" @click="store.methods.increment">+</button>
  </div>
</template>

<script>
import { inject } from 'vue';

export default {
  setup() {
    const store = inject('store');

    return {
      store
    }
  }
}
</script>