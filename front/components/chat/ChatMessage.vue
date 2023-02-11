<template>
  <li 
    :class="[income == true ? 'justify-start' : 'justify-end']"
    class="flex">
    <div class="relative max-w-xl px-4 py-2 text-gray-700 rounded shadow">
      <span class="block">{{ message }}</span>
    </div>
  </li>
</template>

<script>
export default {
  props: {
    message: String,
    income: Boolean
  }
}
</script>