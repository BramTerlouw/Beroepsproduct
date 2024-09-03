<script setup>
import router from '@/router'

const items = [
  { text: 'Home', icon: 'mdi-home', link: '/' },
  { text: 'Incidents (Old)', icon: 'mdi-format-list-bulleted-square', link: '/incidents-old' },
  { text: 'Incidents (New)', icon: 'mdi-format-list-bulleted-square', link: '/incidents-new' },
]

function navigateTo(route) {
  router.push(route)
}

</script>

<template>
  <v-card
    class="mx-auto rounded-0 border-0"
    width="256"
  >
    <v-layout>
      <v-navigation-drawer permanent absolute class="side-nav rounded-0">
        <v-list class="d-flex flex-column">
          <div class="d-flex justify-space-between">
            <v-list-item
              title="Bram Terlouw"
              subtitle="bram@hospital.com"
              height="48"
            >
            </v-list-item>
          </div>
        </v-list>
        <v-divider></v-divider>

        <v-list
          :lines="false"
          density="default"
          nav
        >
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            :value="item"
            @click="navigateTo(item.link)"
            class="test"
          >
            {{ item.text }}
            <template v-slot:prepend>
              <v-icon :icon="item.icon"></v-icon>
            </template>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-main style="height: 100vh;"></v-main>
    </v-layout>
  </v-card>
</template>

<style scoped>
.side-nav {
  background-color: #212427;
  color: white;
}

</style>