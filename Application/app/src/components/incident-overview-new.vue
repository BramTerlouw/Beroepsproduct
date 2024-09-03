<script setup>
import { shallowRef } from 'vue'

const processed = [
  {
    color: 'green',
    icon: 'mdi-check',
    subtitle: 'Jan 20, 2014',
    title: 'Incident Bram Terlouw'
  },
  {
    color: 'green',
    icon: 'mdi-check',
    subtitle: 'Jan 10, 2014',
    title: 'Incident Frank Dersjant'
  }
]

const processing = [
  {
    color: 'orange',
    icon: 'mdi-progress-alert',
    subtitle: 'Unkown',
    title: 'Incident_003'
  }
]

const unprocessed = [
  {
    color: 'red',
    icon: 'mdi-alert-circle-outline',
    subtitle: 'Unknown',
    title: 'Incident_004'
  },
  {
    color: 'red',
    icon: 'mdi-alert-circle-outline',
    subtitle: 'Unknown',
    title: 'Incident_005'
  }
]

const description = shallowRef(false)
const dialog = shallowRef(false)
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
        v-for="file in processed"
        :key="file.title"
        :subtitle="file.subtitle"
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
            @click="dialog = true"
          ></v-btn>
        </template>
      </v-list-item>

      <v-divider inset></v-divider>

      <v-list-subheader inset>Processing Incidents</v-list-subheader>

      <v-list-item
        v-for="file in processing"
        :key="file.title"
        :subtitle="file.subtitle"
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
        v-for="file in unprocessed"
        :key="file.title"
        :subtitle="file.subtitle"
        :title="file.title"
      >
        <template v-slot:prepend>
          <v-avatar :color="file.color">
            <v-icon color="white">{{ file.icon }}</v-icon>
          </v-avatar>
        </template>

        <template v-slot:append>
          <v-btn color="blue" icon="mdi-cog-sync" variant="text" :disabled="false"></v-btn>
          <v-btn
            color="blue"
            icon="mdi-arrow-right-bold-circle-outline"
            variant="text"
            :disabled="true"
          ></v-btn>
        </template>
      </v-list-item>
    </v-list>
  </v-card>

  <v-dialog v-model="dialog" transition="dialog-bottom-transition" fullscreen>
    <v-card>
      <v-toolbar class="bg-dark">
        <v-btn icon="mdi-close" @click="dialog = false"></v-btn>

        <v-toolbar-title>Incident Details</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-toolbar-items>
          <v-btn text="Save" variant="text" @click="dialog = false"></v-btn>
        </v-toolbar-items>
      </v-toolbar>

      <v-list lines="two" subheader>
        <v-list-subheader>Incident information</v-list-subheader>
        <v-card>
          <div class="wrapper">
            <div class="card-inputs">
              <v-card-text>
                <v-row dense>
                  <v-col cols="12" md="6" sm="6">
                    <v-text-field label="Incident ID" required model-value="001"></v-text-field>
                  </v-col>

                  <v-col cols="12" md="6" sm="6">
                    <v-text-field label="Patient name" model-value="Mark Jansen"></v-text-field>
                  </v-col>
                </v-row>
                <v-row dense>
                  <v-col cols="12" md="6" sm="6">
                    <v-text-field
                      label="Date of incident"
                      model-value="27 augustus 2024, 14:30"
                    ></v-text-field>
                  </v-col>

                  <v-col cols="12" md="6" sm="6">
                    <v-text-field
                      label="Location of incident"
                      model-value="Schouwseweg, vlakbij het park aan de rand van het dorp."
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
                      model-value="De patient ervaart ernstige pijn in zijn zij en heeft moeite met ademhalen."
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
                      model-value="De patiënt moet met spoed gecheckt worden op long trauma en daarna naar de gips arts."
                    ></v-textarea>
                  </v-col>
                </v-row>
              </v-card-text>
            </div>

            <v-card-text>
              <div class="card-image">
                <div class="image-placeholder mb-4"></div>
                <div class="image-wrapper">
                  <v-text-field
                    class="image-classifier"
                    label="Type of fracture"
                    model-value="Avulsion fracture"
                  ></v-text-field>
                </div>
              </div>
            </v-card-text>
          </div>

          <v-divider></v-divider>

          <v-card-text class="mt-0 card-description">
            <v-btn v-if="!description" @click="description = true">Show Description</v-btn>
            <v-btn class="mb-2" v-if="description" @click="description = false"
              >Hide Description
            </v-btn>
            <v-row dense v-if="description">
              <v-col cols="12" md="12" sm="12">
                <v-textarea
                  clearable
                  no-resize
                  model-value="Op 27 augustus 2024 omstreeks 14:30 uur heeft er een ongeval plaatsgevonden op de fietsroute langs de Schouwseweg, vlakbij het park aan de rand van het dorp. De betrokken persoon, Mark Jansen, een 35-jarige man, is gevallen terwijl hij op zijn fiets reed. Bij aankomst van de hulpdiensten klaagde Mark over ernstige pijn in zijn zij en had hij moeite met ademhalen. Er zijn geen verdere details over de aard van de verwondingen op dit moment, maar de hulpdiensten hebben hem met spoed naar het ziekenhuis vervoerd voor nader onderzoek en behandeling."
                ></v-textarea>
              </v-col>
            </v-row>
          </v-card-text>

          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn text="Close" variant="plain" @click="dialog = false"></v-btn>

            <v-btn color="primary" text="Save" variant="tonal" @click="dialog = false"></v-btn>
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
}

.card-inputs {
  flex-basis: 70%;
}

.card-image {
  flex-basis: 30%;

  display: flex;
  flex-direction: column;
  align-items: center;
}

.image-placeholder {
  width: 80%;
  height: 250px;
  background-color: grey;
}

.image-classifier {
  width: 100%;
}

.image-wrapper {
  width: 80%;
}

.card-description {
  width: 70%;
}
</style>
