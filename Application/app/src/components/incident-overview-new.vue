<script setup>
import { onMounted, ref, shallowRef } from 'vue'
import axios from 'axios'

axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

const description = shallowRef(false)
const processed_dialog = shallowRef(false)
const start_process_dialog = shallowRef(false)

let processed = ref([])
let processing = ref([])
let unprocessed = ref([])

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
    const response = await axios.get('https://poc-postgresql-server-route-poc-thesis-bram-terlouw.apps.cluster-nvtcj.sandbox1725.opentlc.com/api/incidents');
    const data = response.data;

    const statusMapping = {
      unprocessed: { color: 'red', icon: 'mdi-alert-circle-outline' },
      in_progress: { color: 'orange', icon: 'mdi-progress-alert' },
      processed: { color: 'green', icon: 'mdi-check' }
    };

    data.forEach((item) => {
      const commonFields = {
        id: item.id,
        title: 'Incident_' + item.id,
        name: item.patient_name || 'Unknown',
        date: item.incident_date || 'Unknown',
        location: item.incident_location || 'Unknown',
        complaints: item.patient_complaints || 'Unknown',
        advice: item.advice || 'Unknown',
        classification: item.fracture_classification || 'Unknown',
        description: item.description,
        status: item.incident_status
      };

      const formattedItem = {
        ...commonFields,
        ...statusMapping[item.incident_status]
      }

      switch (formattedItem.status) {
        case 'unprocessed':
          unprocessed.value.push(formattedItem);
          break;
        case 'in_progress':
          processing.value.push(formattedItem);
          break;
        case 'processed':
          processed.value.push(formattedItem);
          break;
        default:
          console.warn(`Unknown status: ${item.status}`, item);
      }
    })

  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

onMounted(() => {
  getIncidents()
})

async function set_selected_incident(incident) {
  selected_incident = incident
  processed_dialog.value = true
}
</script>

<template>
  <v-card class="mx-auto rounded-0 border-0">
    <v-toolbar class="bg-dark">
      <v-toolbar-title>Incident overview</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>

    <v-list lines="two">
      <v-list-subheader inset>Processed Incidents</v-list-subheader>

      <v-list-item
        v-for="(file, index) in processed"
        :key="file.title"
        :subtitle="file.date"
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
            @click="set_selected_incident(processed[index])"
          ></v-btn>
        </template>
      </v-list-item>

      <v-divider inset></v-divider>

      <v-list-subheader inset>Processing Incidents</v-list-subheader>

      <v-list-item
        v-for="file in processing"
        :key="file.title"
        :subtitle="file.date"
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
            :disabled="true"
          ></v-btn>
        </template>
      </v-list-item>

      <v-divider inset></v-divider>

      <v-list-subheader inset>Unprocessed Incidents</v-list-subheader>

      <v-list-item
        v-for="(file, index) in unprocessed"
        :key="file.title"
        :subtitle="file.date"
        :title="file.title"
      >
        <template v-slot:prepend>
          <v-avatar :color="file.color">
            <v-icon color="white">{{ file.icon }}</v-icon>
          </v-avatar>
        </template>

        <template v-slot:append>
          <v-btn
            @click="start_process_dialog = true"
            color="blue"
            icon="mdi-cog-sync"
            variant="text"
            :disabled="false"
          ></v-btn>
          <v-btn
            @click="set_selected_incident(unprocessed[index])"
            color="blue"
            icon="mdi-arrow-right-bold-circle-outline"
            variant="text"
          ></v-btn>
        </template>
      </v-list-item>
    </v-list>
  </v-card>

  <div class="text-center pa-4">
    <v-dialog v-model="start_process_dialog" max-width="400" persistent>
      <v-card
        prepend-icon="mdi-cog"
        text="This action will start the processing of incident_005. Are you sure you want to continue this action?"
        title="Start processing incident_005"
      >
        <template v-slot:actions>
          <v-spacer></v-spacer>

          <v-btn @click="start_process_dialog = false"> Cancel</v-btn>

          <v-btn @click="start_process_dialog = false"> Confirm</v-btn>
        </template>
      </v-card>
    </v-dialog>
  </div>

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
          <div class="wrapper">
            <div class="container-inputs">
              <v-card-text>
                <v-row dense>
                  <v-col cols="12" md="6" sm="6">
                    <v-text-field
                      hide-details
                      label="Incident ID"
                      required
                      :model-value="selected_incident.id"
                      variant="solo-filled"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="12" md="6" sm="6">
                    <v-text-field
                      hide-details
                      label="Patient name"
                      :model-value="selected_incident.name"
                      variant="solo-filled"
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row dense>
                  <v-col cols="12" md="6" sm="6">
                    <v-text-field
                      hide-details
                      label="Date of incident"
                      :model-value="selected_incident.date"
                      variant="solo-filled"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="12" md="6" sm="6">
                    <v-text-field
                      hide-details
                      label="Location of incident"
                      :model-value="selected_incident.location"
                      variant="solo-filled"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-card-text>

              <v-card-text>
                <v-row dense>
                  <v-col cols="12" md="6" sm="6">
                    <v-divider></v-divider>
                    <v-list-subheader>Patient complaints</v-list-subheader>
                    <v-divider></v-divider>
                    <v-textarea
                      class="mt-4"
                      clearable
                      no-resize
                      hide-details
                      :model-value="selected_incident.complaints"
                      variant="solo-filled"
                    ></v-textarea>
                  </v-col>
                  <v-col cols="12" md="6" sm="6">
                    <v-divider></v-divider>
                    <v-list-subheader>Advice follow-up actions</v-list-subheader>
                    <v-divider></v-divider>
                    <v-textarea
                      class="mt-4"
                      clearable
                      no-resize
                      hide-details
                      :model-value="selected_incident.advice"
                      variant="solo-filled"
                    ></v-textarea>
                  </v-col>
                </v-row>
              </v-card-text>
            </div>

            <div class="container-image">
              <v-card-text>
                <img class="image-entity" src="./icons/images/incident_0001.jpg" />
                <v-text-field
                  label="Type of fracture"
                  hide-details
                  :model-value="selected_incident.classification"
                  variant="solo-filled"
                ></v-text-field>
              </v-card-text>
            </div>

            <v-divider></v-divider>

            <div class="mt-0 container-description">
              <v-card-text>
                <v-btn v-if="!description" @click="description = true">Show Description</v-btn>
                <v-btn class="mb-2" v-if="description" @click="description = false"
                  >Hide Description
                </v-btn>
                <v-row dense v-if="description">
                  <v-col cols="12" md="12" sm="12">
                    <v-textarea
                      clearable
                      no-resize
                      hide-details
                      :model-value="selected_incident.description"
                      variant="solo-filled"
                    ></v-textarea>
                  </v-col>
                </v-row>
              </v-card-text>
            </div>
          </div>

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

.wrapper {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.container-inputs {
  flex-basis: 70%;
}

.container-image {
  flex-basis: 30%;

  display: flex;
  flex-direction: column;
  align-items: center;
}

.container-description {
  width: 70%;
}

.image-entity {
  height: 300px;
}
</style>
