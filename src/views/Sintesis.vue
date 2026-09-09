<template lang="pug">
.curso-main-container.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span
          i.fas.fa-sitemap
      h1 Síntesis

    p.mb-4 El desarrollo del <em>chatbot</em> simple comprende un proceso articulado que inicia con la configuración de sus parámetros y la creación del flujo conversacional, continúa con la verificación de su funcionamiento mediante casos de prueba e indicadores de desempeño, y avanza hacia el ajuste de los flujos a partir de los hallazgos identificados. Este proceso permite evaluar el comportamiento del sistema, priorizar correcciones y aplicar acciones de mejora continua para mantener una experiencia conversacional coherente y funcional.
    p.mb-4 Finalmente, la elaboración del informe técnico permite documentar de manera ordenada los resultados, hallazgos, ajustes y evidencias del proyecto, considerando criterios de claridad, objetividad, concisión, precisión y trazabilidad. En conjunto, estos saberes proporcionan al aprendiz una visión integral del ciclo de desarrollo de un <em>chatbot</em> simple y fortalecen sus capacidades para configurar, construir, verificar, ajustar y documentar soluciones de inteligencia artificial conversacional.
    .row.justify-content-center.mb-4
      .col-12
        figure
          img(src="@/assets/curso/sintesis.svg" alt="En la síntesis se presenta un mapa conceptual que organiza los principales temas relacionados con el desarrollo de un chatbot. Inicia con la configuración de los parámetros de la conversación, considerando aspectos generales y específicos, mensajes, variables, canales, horarios y seguridad; continúa con la creación del flujo de conversación, relacionada con la secuencia, las intenciones, las respuestas, las condiciones y el manejo de errores. Posteriormente, aborda la verificación del funcionamiento mediante la planificación, los casos de prueba, la ejecución y el análisis. Luego, presenta el ajuste de los flujos a partir de los hallazgos, su priorización y las correcciones. Finalmente, integra la elaboración del informe técnico, considerando sus características, estructura, evidencias, versiones según la audiencia y control de versiones.")
    .row.justify-content-center
      .col-auto
        a.anexo.mb-0(:href="obtenerLink('/downloads/Sintesis.pdf')" target="_blank" rel="noopener")
          .anexo__icono
            img(src="@/assets/bullets/icono-pdf.svg" alt="")
          .anexo__texto
            p Anexo. Síntesis
</template>

<script>
export default {
  name: 'Sintesis',
}
</script>
