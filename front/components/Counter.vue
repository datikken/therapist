<template>
  <span class="p-2 bg-gradient-to-r from-cyan-500 to-blue-500 text-gray-900" @click="store.methods.decrement">-</span>
   {{ store.state.counter }}
  <span class="p-2 bg-gradient-to-r from-cyan-500 to-blue-500 text-gray-900" @click="store.methods.increment">+</span>
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