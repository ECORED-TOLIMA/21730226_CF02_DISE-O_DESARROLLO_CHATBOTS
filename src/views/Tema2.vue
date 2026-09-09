<template lang="pug">
.curso-main-container.pb-3.tema2
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span 2
      h1 Creación del flujo de conversación

    .bloque-texto-g.bloque-texto-g--inverso.color-primario.p-3.p-sm-4.p-md-5.mb-0
      .bloque-texto-g__img(:style="{'background-image': `url(${require_src('@/assets/curso/temas/t2/img1.png')})`}")
      .bloque-texto-g__texto.p-4
        p.mb-0 La creación del flujo de conversación constituye la etapa en la que el diseño previo se lleva a la plataforma seleccionada y se convierte en una secuencia funcional de interacciones. Para comprender este proceso, las siguientes temáticas abordan las buenas prácticas que orientan la construcción del flujo y presentan un ejemplo integrador que permite observar su aplicación en un caso del sector servicios.

    Separador
    #t_2_1.titulo-segundo.color-acento-contenido(data-aos="fade-left")
      h2 2.1 Buenas prácticas de construcción
    
    p.mb-4 Un flujo de conversación es la secuencia de mensajes y respuestas que sigue el <em>chatbot</em> durante una sesión con el usuario. Su construcción se realiza, por lo general, mediante un editor visual en el que se enlazan bloques de mensajes, preguntas, condiciones y acciones. La calidad del flujo depende tanto del diseño previo como de la rigurosidad con que se implementen sus diferentes componentes.
    .row.align-items-center.mb-4
      .col-lg-5.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t2/img2.png" alt="")
      .col-lg-7
        .bg01.p-4.mb-4
          p.mb-0 Durante la construcción del flujo se deben verificar la conexión entre los bloques, la secuencia de las interacciones, las condiciones, las acciones y las variables utilizadas. También es necesario comprobar que cada recorrido conduzca a una respuesta o acción definida y que existan alternativas para los escenarios que no siguen el recorrido esperado.
        p.mb-0 Un patrón recurrente en la construcción de <em>chatbots</em> es la creación iterativa por versiones. La primera versión, conocida como mínimo producto viable, contempla únicamente las 2 o 3 intenciones más relevantes, los flujos esenciales y los mensajes básicos. Esta versión se lanza al público con la conciencia de que es incompleta, pero suficiente para resolver las consultas más frecuentes. Las siguientes versiones incorporan más intenciones, mejores respuestas y nuevas integraciones, basándose en el aprendizaje obtenido del uso real.
    .row.justify-content-center.mb-4
      .col-lg-6
        .bg06.rounded-3.p-2
          p.mb-0.text-center Esta aproximación iterativa tiene varias ventajas:
    .tema2-ventajas.p-4.mb-4
      .tarjeta.bgwhite.shadow-sm.p-4
        ol.lista-ol--cuadro.lista-ol--cuadro--separador.lista-ol--separador.mb-0
          li.d-flex
            .lista-ol--cuadro__vineta.flex-shrink-0
              span.text-dark 1
            p.mb-0 Reduce el tiempo desde el inicio del proyecto hasta el primer impacto en el cliente.
          li.d-flex
            .lista-ol--cuadro__vineta.flex-shrink-0
              span.text-dark 2
            p.mb-0 Permite descubrir tempranamente qué funciona y qué no, antes de invertir grandes recursos en funcionalidades que pueden no ser necesarias.
          li.d-flex
            .lista-ol--cuadro__vineta.flex-shrink-0
              span.text-dark 3
            p.mb-0 Facilita la apropiación gradual de la herramienta por parte del equipo interno.
          li.d-flex.mb-0
            .lista-ol--cuadro__vineta.flex-shrink-0
              span.text-dark 4
            p.mb-0 Y, sobre todo, mantiene el <em>chatbot</em> vivo, en constante evolución, en lugar de convertirlo en un sistema estático que rápidamente queda desactualizado.
    p.mb-4 La construcción del flujo puede desarrollarse de manera progresiva, incorporando mejoras a partir de la experiencia obtenida durante su implementación. La siguiente figura resume las principales etapas de este proceso, desde el diseño previo hasta el desarrollo iterativo del <em>chatbot</em>:
    .titulo-sexto.color-acento-contenido.mb-3.mt-4
      h5 Figura 1.
      span Proceso de creación del flujo de #[em chatbot]
    .row.justify-content-center.mb-0
      .col-12.d-none.d-lg-block
        figure
          img(src="@/assets/curso/temas/t2/img3.svg" alt="Figura 1 que presenta 6 etapas del proceso de desarrollo de un flujo conversacional: diseño previo, construcción de flujo, implementación de buenas prácticas, lanzamiento del MVP, recopilación de feedback y desarrollo iterativo. Cada etapa permite analizar de manera secuencial la evolución del flujo desde su diseño inicial hasta su mejora continua.")
      .col-12.d-block.d-lg-none
        figure
          img(src="@/assets/curso/temas/t2/img3_1.svg" alt="Figura 1 que presenta 6 etapas del proceso de desarrollo de un flujo conversacional: diseño previo, construcción de flujo, implementación de buenas prácticas, lanzamiento del MVP, recopilación de feedback y desarrollo iterativo. Cada etapa permite analizar de manera secuencial la evolución del flujo desde su diseño inicial hasta su mejora continua.")

    Separador
    #t_2_2.titulo-segundo.color-acento-contenido(data-aos="fade-left")
      h2 2.2 Ejemplo integrador para la atención al cliente

    .row.align-items-center.mb-4
      .col-lg-8.mb-4.mb-lg-0
        .bg04.p-4.mb-4
          p.mb-0 Para ilustrar la integración de los conceptos abordados, se presenta un caso aplicado al sector de servicios:
        p.mb-4 Una pequeña empresa de domicilios desea construir un <em>chatbot</em> en WhatsApp que atienda 3 tipos de consultas frecuentes: horarios de atención, menú del día y estado del pedido. La empresa enfrenta un alto volumen de llamadas telefónicas que saturan a su equipo de atención al cliente y considera que un <em>chatbot</em> puede aliviar esta carga sin reducir la calidad del servicio.
        .cajon.color-secundario.p-4.mb-4
          p.mb-0 El proceso de diseño parte de entender al usuario típico: clientes habituales que conocen el producto y desean consultar información rápidamente, sin esperas. La plataforma elegida es Landbot, por su modalidad sin código y su integración con WhatsApp Business, lo que permitiría a la empresa lanzar el <em>chatbot</em> en pocos días sin contratar desarrolladores externos.
        p.mb-0 Las intenciones definidas son consultar el horario, el menú y el estado del pedido. Para atender estas consultas, el <em>chatbot</em> debe identificar y extraer las entidades necesarias, como el número de pedido, cuando se requiera para consultar su estado, y la fecha, cuando aplique. A partir de estas intenciones y entidades, se establece una comunicación cercana, breve y amable, en la que el <em>chatbot</em> se dirige al usuario por su nombre cuando este esté disponible. Esta experiencia se articula alrededor de una personalidad definida como Pipo, el asistente virtual de la pizzería, quien será el encargado de acompañar al usuario durante la interacción.
      .col-lg-4
        figure
          img(src="@/assets/curso/temas/t2/2150169863.png" alt="")
    .row.justify-content-center.mb-4
      .col-lg-6
        .bg06.rounded-3.p-2
          p.mb-0.text-center La siguiente tabla resume la configuración aplicada al caso:
    .titulo-sexto.color-acento-contenido.mb-3.mt-4
      h5 Tabla 2.
      span Configuración del caso integrador
    .tabla-a.color-acento-contenido.mb-4
      table
        thead
          tr
            th(scope="col") <strong>Elemento</strong>
            th(scope="col") <strong>Configuración del caso</strong>
        tbody
          tr
            td Propósito
            td Atender las consultas frecuentes de los clientes y descongestionar la línea telefónica.
          tr
            td Plataforma elegida
            td Landbot, por su modalidad sin código e integración nativa con WhatsApp Business.
          tr
            td Intenciones
            td Consultar horario.<br>Consultar menú.<br>Consultar estado del pedido.
          tr
            td Entidades
            td NumeroPedido (numérico), Fecha (cuando aplique).
          tr
            td Voz y tono
            td Cercano, breve, amable. El <em>chatbot</em> trata al usuario por su nombre.
          tr
            td Personalidad
            td «Soy Pipo, el asistente virtual de la pizzería».
          tr
            td Mensaje de bienvenida
            td «¡Hola! Soy Pipo. ¿En qué puedo ayudarte hoy?<br>1) Ver el menú.<br>2) Estado de mi pedido.<br>3) Horarios».
          tr
            td Mensaje de respaldo
            td «Disculpa, no entendí tu mensaje. ¿Podrías reformularlo o escribir AGENTE para hablar con una persona?».
          tr
            td Regla de escalamiento
            td Si el usuario escribe AGENTE o el <em>chatbot</em> falla dos veces seguidas, se transfiere al equipo humano.

    .row.align-items-center.mb-0
      .col-auto.mb-4.mb-md-0
        img.tema2-icono-cierre(src="@/assets/curso/temas/t2/img4.png" alt="")
      .col-md
        p.mb-0 Con la configuración definida, el equipo de la pizzería puede implementar el flujo y organizar los recorridos correspondientes a cada consulta. La primera versión contempla las funcionalidades esenciales para atender las necesidades más frecuentes y constituye un mínimo producto viable. Una vez construido, el <em>chatbot</em> deberá pasar por la fase de verificación para comprobar su funcionamiento antes de ser puesto en operación.
</template>

<script>
export default {
  name: 'Tema2',
  mounted() {
    this.$nextTick(() => this.$aosRefresh())
  },
  updated() {
    this.$aosRefresh()
  },
}
</script>
