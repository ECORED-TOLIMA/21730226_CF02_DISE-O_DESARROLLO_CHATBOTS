<template lang="pug">
.curso-main-container.pb-3
  BannerInterno(icono="far fa-question-circle" titulo="Actividad didáctica")
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5
    ActividadController(:cuestionario="cuestionario")
</template>

<script>
import ActividadController from '@ecored-sena/boulder-kit/plugin/components/actividad/ActividadController.vue'
import cuestionario from '@/config/actividad.json'

export default {
  name: 'ActividadDidactica',
  components: { ActividadController },
  data: () => ({ cuestionario }),
}
</script>
