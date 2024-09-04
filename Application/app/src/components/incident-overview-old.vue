<script setup>
import { shallowRef } from 'vue'

const incidents = [
  {
    color: 'blue',
    icon: 'mdi-information-outline',
    title: 'Incident_001'
  },
  {
    color: 'blue',
    icon: 'mdi-information-outline',
    title: 'Incident_002'
  },
  {
    color: 'blue',
    icon: 'mdi-information-outline',
    title: 'Incident_003'
  },
  {
    color: 'blue',
    icon: 'mdi-information-outline',
    title: 'Incident_004'
  }
]

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

      <v-list-item v-for="file in incidents" :key="file.title" :title="file.title">
        <template v-slot:prepend>
          <v-avatar :color="file.color">
            <v-icon color="white">{{ file.icon }}</v-icon>
          </v-avatar>
        </template>

        <template v-slot:append>
          <v-btn @click="processed_dialog = true" color="blue" icon="mdi-arrow-right-bold-circle-outline"
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
                    model-value="Op 27 augustus 2024 omstreeks 14:30 uur heeft er een ongeval plaatsgevonden op de fietsroute langs de Schouwseweg, vlakbij het park aan de rand van het dorp. De betrokken persoon, Mark Jansen, een 35-jarige man, is gevallen terwijl hij op zijn fiets reed. Bij aankomst van de hulpdiensten klaagde Mark over ernstige pijn in zijn zij en had hij moeite met ademhalen. Er zijn geen verdere details over de aard van de verwondingen op dit moment, maar de hulpdiensten hebben hem met spoed naar het ziekenhuis vervoerd voor nader onderzoek en behandeling."
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
