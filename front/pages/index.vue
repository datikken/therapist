<template>
  <div class="index-page">
    <client-only>
      <Chat />
    </client-only>

    <Counter />
  </div>
</template>

<script>
import { provide } from 'vue';
import store from '../store/index';

export default {
  setup() {
    provide('store', store);
  }
}
</script>