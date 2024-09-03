<script setup>
const incidents = [
  {
    color: 'blue',
    icon: 'mdi-information-outline',
    title: 'Incident_001',
  },
  {
    color: 'blue',
    icon: 'mdi-information-outline',
    title: 'Incident_002',
  },
  {
    color: 'blue',
    icon: 'mdi-information-outline',
    title: 'Incident_003',
  },
  {
    color: 'blue',
    icon: 'mdi-information-outline',
    title: 'Incident_004',
  },
]

</script>

<template>
  <v-card
    class="mx-auto rounded-0 border-0"
  >
    <v-toolbar class="bg-dark" >
      <v-toolbar-title>Incident overview</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>

    <v-list lines="two">
      <v-list-subheader inset>Processed Incidents</v-list-subheader>

      <v-list-item
        v-for="file in incidents"
        :key="file.title"
        :title="file.title"
      >
        <template v-slot:prepend>
          <v-avatar :color="file.color">
            <v-icon color="white">{{ file.icon }}</v-icon>
          </v-avatar>
        </template>

        <template v-slot:append>
          <v-btn
            color="blue"
            icon="mdi-arrow-right-bold-circle-outline"
            variant="text"
          ></v-btn>
        </template>
      </v-list-item>

    </v-list>
  </v-card>
</template>

<style scoped>

.bg-dark {
  background-color: #212427;
  color: white;
}
</style>