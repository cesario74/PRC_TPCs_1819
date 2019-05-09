<template>
  <v-container>
      <Ator :idAtor="$route.params.id"/>
      <v-layout>
          <v-btn color="info" @click="$router.go(-1)">
              Voltar à página anterior
          </v-btn>
      </v-layout>
  </v-container>
</template>

<script>
import Ator from '@/components/Ator'

export default {
  components: {
    Ator
  }
}
</script>
