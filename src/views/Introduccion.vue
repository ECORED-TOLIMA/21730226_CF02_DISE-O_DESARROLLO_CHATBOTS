<template lang="pug">
.curso-main-container.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span
          i.fas.fa-info
      h1 Introducción

    p.mb-4 Los <em>chatbots</em> requieren una configuración adecuada para responder de acuerdo con los objetivos definidos y ofrecer una interacción coherente con los usuarios. Su desarrollo comprende diferentes etapas que permiten:
    .row.justify-content-center.align-items-center.mb-4
      .col-lg-2.col-10
        .bg07
          p.mb-0.text-center.text-bold Pasar de la configuración inicial a:
      .col-12.col-lg-auto.d-flex.justify-content-center.px-0.py-2.py-lg-0
        img.intro-flecha-etapas(src="@/assets/curso/temas/intro/img2.svg" alt="")
      .col-lg-2.col-10
        .bg08
          p.mb-0.text-center.text-bold La construcción del flujo
      .col-12.col-lg-auto.d-flex.justify-content-center.px-0.py-2.py-lg-0
        img.intro-flecha-etapas(src="@/assets/curso/temas/intro/img2.svg" alt="")
      .col-lg-2.col-10
        .bg08
          p.mb-0.text-center.text-bold La verificación de su funcionamiento
      .col-12.col-lg-auto.d-flex.justify-content-center.px-0.py-2.py-lg-0
        img.intro-flecha-etapas(src="@/assets/curso/temas/intro/img2.svg" alt="")
      .col-lg-2.col-10
        .bg08
          p.mb-0.text-center.text-bold El ajuste de los hallazgos
      .col-12.col-lg-auto.d-flex.justify-content-center.px-0.py-2.py-lg-0
        img.intro-flecha-etapas(src="@/assets/curso/temas/intro/img2.svg" alt="")
      .col-lg-2.col-10
        .bg08
          p.mb-0.text-center.text-bold La documentación de los resultados
    p.mb-4 Sin embargo, construir un <em>chatbot</em> que realmente aporte valor exige mucho más que una idea inicial o una plataforma tecnológica. Detrás de cada conversación automatizada existen decisiones técnicas y procedimentales que determinan la calidad del producto final:
    .BGF00.p-4.mb-4
      .row.justify-content-center.align-items-center
        .col-lg-7.mb-4.mb-lg-0.order-2.order-lg-1
          .tarjeta.bg-white.shadow-sm.p-4
            ul.lista-ul.mb-0
              li.mb-2
                i.fas.fa-comment
                span Configuración de los parámetros del sistema.
              li.mb-2
                i.fas.fa-comment
                span Construcción del flujo conversacional.
              li.mb-2
                i.fas.fa-comment
                span Verificación del funcionamiento.
              li.mb-2
                i.fas.fa-comment
                span Ajuste a partir de los hallazgos identificados.
              li.mb-2
                i.fas.fa-comment
                span Documentación del proceso para facilitar su comprensión, mantenimiento y evolución.
        .col-lg-3.col-8.mb-4.mb-lg-0.order-1.order-lg-2
          figure
            img(src="@/assets/curso/temas/intro/img1.svg" alt="")
    p.mb-4 La verificación del funcionamiento del <em>chatbot</em>, también conocida como <em>testing</em> conversacional, es una disciplina que combina prácticas de la ingeniería de <em>software</em> con metodologías propias del diseño de experiencia de usuario. Implica diseñar casos de prueba, ejecutarlos sistemáticamente, registrar los hallazgos y aplicar correcciones de forma iterativa. Este proceso no termina con el lanzamiento del <em>chatbot</em> al público: continúa a lo largo de toda su vida útil, garantizando que la solución se mantenga relevante, precisa y útil para los usuarios.
    .row.justify-content-center.mb-4
      .col-lg-10
        .cajon.color-primario.p-4
          p.mb-0 El presente componente desarrolla, de manera progresiva y articulada, los saberes necesarios para llevar un <em>chatbot</em> desde la configuración inicial hasta la entrega final con su respectivo informe técnico. El contenido se organiza en temáticas que cubren, en orden lógico, las etapas operativas del ciclo de vida de un <em>chatbot</em> simple: configuración de parámetros, creación del flujo conversacional, verificación del funcionamiento, ajuste de los flujos a partir de hallazgos y elaboración del informe técnico.
    p.mb-4 Al finalizar la revisión de los contenidos, el aprendiz contará con las herramientas para verificar y ajustar flujos conversacionales simples, evaluar el desempeño de un <em>chatbot</em> mediante indicadores objetivos y elaborar informes técnicos que comuniquen con claridad los resultados del proyecto. Estas competencias resultan especialmente valiosas en un mercado laboral colombiano que demanda cada vez más perfiles capaces de diseñar, construir, verificar y documentar soluciones de inteligencia artificial conversacional para empresas establecidas o para emprendimientos propios.
    p.mb-4 Por lo anterior, para comprender la importancia del contenido y los temas abordados, se recomienda acceder al siguiente video:
    //- Video de muestra conservado por indicación del usuario; pendiente reemplazo por el oficial.
    .video
      iframe(width="560" height="315" src="https://www.youtube.com/embed/vdPrCjWJSHo?si=X4NxENRo3LLXAua_" title="Video de introducción" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen)
</template>

<script>
export default {
  name: 'Introduccion',
}
</script>
