import { reactive, readonly } from 'vue';

const state = reactive({
  counter: 0,
  colorCode: 'red'
});

const methods = {
  decrement() {
    state.counter--
  },
  increment() {
    state.counter++
  },
  setColorCode(val) {
    state.colorCode = val;
  }
};

const getters = {
  counterSquared() {
    return state.counter * state.counter
  }
};

export default {
  state: readonly(state),
  methods,
  getters
}