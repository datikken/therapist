<template>
  <div class="p-4 counter">
    <input class="border m-4 p-2" type="text" v-model="colorCode" />
    <br/>

    <button class="p-2 bg-gradient-to-r from-cyan-500 to-blue-500 text-white" @click="store.methods.decrement">-</button>
    <span
      :style="{ color: store.state.colorCode }"
      class="value p-4">{{ store.state.counter }}</span>
    <button class="p-2 bg-gradient-to-r from-cyan-500 to-blue-500 text-white" @click="store.methods.increment">+</button>
  </div>
</template>

<script>
import { inject, computed } from 'vue';

export default {
  setup() {
    const store = inject('store');
    
    const colorCode = computed({
      get() {
        return store.state.colorCode
      },
      set(val) {
        return store.methods.setColorCode(val)
      }
    })

    return {
      store,
      colorCode
    }
  }
}
</script>