<script setup>
import { onMounted, ref, shallowRef } from 'vue'
import axios from 'axios'

const incidents = ref([])

let selected_incident = {
  id: '',
  name: '',
  date: '',
  location: '',
  complaints: '',
  advice: '',
  classification: '',
  description: '',
  processed: '',
}

async function getIncidents() {
  try {
    const response = await axios.get('https://poc-postgresql-server-route-bram-terlouw-dev.apps.sandbox-m2.ll9k.p1.openshiftapps.com/api/incidents');
    const data = response.data;

    data.forEach((item) => {
      const incident = {
        id: item.id,
        description: item.description,
        color: 'blue',
        icon: 'mdi-information-outline',
        title: 'Incident_' + item.id
      };
      incidents.value.push(incident);
    })

  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

onMounted(() => {
  getIncidents()
})

function set_selected_incident(incident) {
  selected_incident = incident
  processed_dialog.value = true
}

const processed_dialog = shallowRef(false)
</script>

<template>
  <v-card class="mx-auto rounded-0 border-0">
    <v-toolbar class="bg-dark">
      <v-toolbar-title>Incident overview</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>

    <v-list lines="two">
      <v-list-subheader inset>Incidents</v-list-subheader>

      <v-list-item v-for="(file, index) in incidents" :key="file.title" :title="file.title">
        <template v-slot:prepend>
          <v-avatar :color="file.color">
            <v-icon color="white">{{ file.icon }}</v-icon>
          </v-avatar>
        </template>

        <template v-slot:append>
          <v-btn @click="set_selected_incident(incidents[index])" color="blue" icon="mdi-arrow-right-bold-circle-outline"
                 variant="text"></v-btn>
        </template>
      </v-list-item>
    </v-list>
  </v-card>

  <v-dialog v-model="processed_dialog" transition="dialog-bottom-transition" fullscreen>
    <v-card>
      <v-toolbar class="bg-dark">
        <v-btn icon="mdi-close" @click="processed_dialog = false"></v-btn>

        <v-toolbar-title>Incident Details</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-toolbar-items>
          <v-btn text="Save" variant="text" @click="processed_dialog = false"></v-btn>
        </v-toolbar-items>
      </v-toolbar>

      <v-list lines="two" subheader>
        <v-list-subheader>Incident information</v-list-subheader>
        <v-card>
          <v-card-text class="d-flex flex-row ga-3 set-height">
                <div class="textarea-wrapper">
                  <v-textarea
                    class="test"
                    clearable
                    no-resize
                    hide-details
                    :model-value="selected_incident.description"
                    variant="solo-filled"
                  ></v-textarea>
                </div>
                <div class="image-wrapper">
                  <img class="image-placeholder" src="./icons/images/incident_0001.jpg">
                </div>
          </v-card-text>

          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn text="Close" variant="plain" @click="processed_dialog = false"></v-btn>

            <v-btn
              color="primary"
              text="Save"
              variant="tonal"
              @click="processed_dialog = false"
            ></v-btn>
          </v-card-actions>
        </v-card>

        <v-divider></v-divider>
      </v-list>
    </v-card>
  </v-dialog>
</template>

<style scoped>
.bg-dark {
  background-color: #212427;
  color: white;
}

.set-height {
  height: 300px;
}

.image-placeholder {
  height: 100%;
  background-color: grey;
}

.textarea-wrapper {
  flex-basis: 75%;
  height: 100%;
}

.image-wrapper {
  height: 78%;
}

.test {
  height: 100%;
}
</style>
