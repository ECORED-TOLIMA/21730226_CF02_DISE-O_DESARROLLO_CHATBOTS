<template lang="pug">
.curso-main-container.pb-3.tema4
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span 4
      h1 Ajuste de los flujos de conversación

    figure.mb-4
      img(src="@/assets/curso/temas/t4/img1.png" alt="")

    p.mb-0 Una vez completada la fase de verificación, los hallazgos identificados deben traducirse en ajustes concretos al flujo conversacional. Para ello, las siguientes temáticas abordan el análisis de los hallazgos de las pruebas y la priorización de las correcciones, junto con la mejora continua como estrategia para mantener el <em>chatbot</em> relevante y útil a lo largo del tiempo.

    Separador
    #t_4_1.titulo-segundo.color-acento-contenido(data-aos="fade-left")
      h2 4.1 Análisis de hallazgos y priorización

    p.mb-4 Los hallazgos obtenidos durante la verificación son de naturaleza diversa:
    .BGF01.px-5.p-4.mb-4
      .row.align-items-center
        .col-lg-4.mb-4.mb-lg-0
          img.tema4-personaje.mx-auto(src="@/assets/curso/temas/t4/img2.png" alt="")
        .col-lg-8
          SlyderF(columnas="col-12 col-md-6 col-xl-4")
            .tarjeta.bgwhite.p-4.h-100.text-center
              img.tema4-icono.mx-auto.mb-4(src="@/assets/curso/temas/t4/img3.svg" alt="")
              p.mb-0 Errores de comprensión.
            .tarjeta.bgwhite.p-4.h-100.text-center
              img.tema4-icono.mx-auto.mb-4(src="@/assets/curso/temas/t4/img4.svg" alt="")
              p.mb-0 Respuestas incorrectas.
            .tarjeta.bgwhite.p-4.h-100.text-center
              img.tema4-icono.mx-auto.mb-4(src="@/assets/curso/temas/t4/img5.svg" alt="")
              p.mb-0 Mensajes confusos.
            .tarjeta.bgwhite.p-4.h-100.text-center
              img.tema4-icono.mx-auto.mb-4(src="@/assets/curso/temas/t4/img6.svg" alt="")
              p.mb-0 Flujos rotos.
            .tarjeta.bgwhite.p-4.h-100.text-center
              img.tema4-icono.mx-auto.mb-4(src="@/assets/curso/temas/t4/img7.svg" alt="")
              p.mb-0 Integraciones que fallan.
            .tarjeta.bgwhite.p-4.h-100.text-center
              img.tema4-icono.mx-auto.mb-4(src="@/assets/curso/temas/t4/img8.svg" alt="")
              p.mb-0 Oportunidades de mejora en la experiencia del usuario.

    .row.justify-content-center.align-items-center.mb-4
      .col-auto.mb-4.mb-md-0
        img.tema4-icono.mx-auto(src="@/assets/curso/temas/t4/img25.svg" alt="")
      .col-md-9
        .bg04.p-4
          p.mb-0 No todos los hallazgos tienen la misma importancia ni el mismo impacto, por lo que es necesario clasificarlos y priorizarlos para orientar el trabajo del equipo.

    .row.justify-content-center.mb-4
      .col-lg-4
        .bg06.rounded-3.p-2
          p.mb-0.text-center Una clasificación útil distingue entre:

    .row.justify-content-center.mb-4
      .col-lg-4.mb-4.mb-lg-0
        .tarjeta.tarjeta--boton.bg03.p-4.h-100.text-center
          .tema4-icono-hallazgo.mx-auto.mb-4
            img(src="@/assets/curso/temas/t4/img9.svg" alt="")
          h5.mb-4 Hallazgos críticos
          p.mb-4 Impiden que el <em>chatbot</em> cumpla su propósito principal o ponen en riesgo a los usuarios; deben corregirse antes del lanzamiento.
          p.mb-0 Acción recomendada: corregir antes del lanzamiento; bloquea la salida a producción.
      .col-lg-4.mb-4.mb-lg-0
        .tarjeta.tarjeta--boton.bg03.p-4.h-100.text-center
          .tema4-icono-hallazgo.mx-auto.mb-4
            img(src="@/assets/curso/temas/t4/img10.svg" alt="")
          h5.mb-4 Hallazgos mayores
          p.mb-4 Afectan significativamente la experiencia o la precisión, pero no impiden el funcionamiento básico; deben corregirse en la versión inicial siempre que el cronograma lo permita.
          p.mb-0 Acción recomendada: corregir en la versión inicial si el cronograma lo permite.
      .col-lg-4.mb-4.mb-lg-0
        .tarjeta.tarjeta--boton.bg03.p-4.h-100.text-center
          .tema4-icono-hallazgo.mx-auto.mb-4
            img(src="@/assets/curso/temas/t4/img12.svg" alt="")
          h5.mb-4 Hallazgos menores
          p.mb-4 Son mejoras estéticas o ajustes finos que no afectan la funcionalidad esencial, pero pueden mejorar la experiencia del usuario. Pueden incorporarse en versiones posteriores.
          p.mb-0 Acción recomendada: programar en versiones posteriores como mejora continua.

    p.mb-4 La siguiente imagen representa de manera jerárquica estos hallazgos:
    .titulo-sexto.color-acento-contenido.mb-3.mt-4
      h5 Figura 5.
      span Jerarquía de prioridad de hallazgos o errores
    .row.justify-content-center.mb-4
      .col-12.d-none.d-lg-block
        figure
          img(src="@/assets/curso/temas/t4/img13.svg" alt="Figura 5 que relaciona una pirámide de jerarquía de prioridad de hallazgos o errores en un chatbot, organizada en tres niveles: crítico, de atención inmediata; mayor, que requiere corrección prioritaria; y menor, que puede atenderse posteriormente.")
      .col-12.d-block.d-lg-none
        figure
          img(src="@/assets/curso/temas/t4/img13_1.svg" alt="Figura 5 que relaciona una pirámide de jerarquía de prioridad de hallazgos o errores en un chatbot, organizada en tres niveles: crítico, de atención inmediata; mayor, que requiere corrección prioritaria; y menor, que puede atenderse posteriormente.")
    p.mb-4 La priorización también puede apoyarse en otros criterios: la frecuencia con que ocurre el problema, el número de usuarios afectados, el impacto en los indicadores de negocio y el costo de la corrección. Una matriz que combine impacto y esfuerzo ayuda al equipo a tomar decisiones informadas: las correcciones de alto impacto y bajo esfuerzo se ejecutan primero; las de alto impacto y alto esfuerzo se planifican cuidadosamente; las de bajo impacto y alto esfuerzo se posponen.
    .row.justify-content-center.mb-4
      .col-lg-10
        .cajon.color-primario.p-4
          p.mb-0 Cada ajuste aplicado al <em>chatbot</em> debe documentarse adecuadamente. La documentación incluye la descripción del problema original, la causa identificada, la solución implementada y la prueba que valida la corrección. Esta documentación, además de servir como bitácora del proyecto, facilita el aprendizaje del equipo y reduce la probabilidad de que el mismo error vuelva a ocurrir en el futuro.

    p.mb-4 Existen tipos específicos de ajustes que se aplican con frecuencia en proyectos de <em>chatbot</em>. La siguiente tabla explica un poco cada uno y los ejemplifica para mayor entendimiento:
    .titulo-sexto.color-acento-contenido.mb-3.mt-4
      h5 Tabla 5.
      span Tipos de ajustes frecuentes en #[em chatbots] y ejemplos de aplicación
    .tabla-a.color-acento-contenido.mb-0
      table
        thead
          tr
            th(scope="col") <strong>Tipo de ajuste</strong>
            th(scope="col") <strong>Descripción</strong>
            th(scope="col") <strong>Ejemplo</strong>
        tbody
          tr
            td Ajuste de comprensión.
            td Modifica frases de entrenamiento o palabras clave para mejorar el reconocimiento.
            td Agregar variaciones como «cuánto debo» a la intención de consulta de saldo.
          tr
            td Ajuste de respuesta.
            td Corrige el contenido o el tono de los mensajes del <em>chatbot</em>.
            td Hacer más empática la respuesta cuando el usuario reporta un problema.
          tr
            td Ajuste de flujo.
            td Modifica la secuencia de pasos en una conversación.
            td Mover la confirmación del pedido antes de tomar el método de pago.
          tr
            td Ajuste de configuración.
            td Cambia parámetros generales como tiempos de espera.
            td Aumentar el tiempo de espera de 5 a 10 minutos.
          tr
            td Ajuste de integración.
            td Corrige problemas en la conexión con sistemas externos.
            td Manejar el caso en que la base de datos no responde dentro del tiempo esperado.


    Separador
    #t_4_2.titulo-segundo.color-acento-contenido(data-aos="fade-left")
      h2 4.2 Iteración y mejora continua del #[em chatbot]

    p.mb-4 El ajuste no termina con el lanzamiento del <em>chatbot</em>. La mejora continua es una práctica que se mantiene durante toda la vida útil del sistema, garantizando que se adapte a las necesidades cambiantes de los usuarios y del negocio. Esta práctica se basa en ciclos cortos de medición, análisis y ajuste, conocidos en la industria como ciclos de iteración.
    p.mb-4 Un enfoque popular para la mejora continua es el ciclo <em>plan-do-</em><em>check</em><em>-</em><em>act</em>, adaptado al contexto de los <em>chatbots</em>. Cada fase representa lo siguiente:
    .row.justify-content-center.mb-4.tema4-ciclo
      .col-lg-10
        ImagenInfografica.color-acento-botones.d-none.d-lg-block
          template(v-slot:imagen)
            figure
              img(src="@/assets/curso/temas/t4/img14.svg" alt="")
          .tarjeta.bgwhite.p-4(x="81%" y="22%" numero="+")
            h5.mb-4 Plan
            p.mb-0 En la fase de planificación, el equipo identifica oportunidades de mejora a partir de los datos disponibles.
          .tarjeta.bgwhite.p-4(x="81%" y="78%" numero="+")
            h5.mb-4 Do
            p.mb-0 En la fase de ejecución, aplica los cambios seleccionados en un entorno de pruebas.
          .tarjeta.bgwhite.p-4(x="57%" y="78%" numero="+")
            h5.mb-4 Check
            p.mb-0 En la fase de verificación, mide el impacto de los cambios en los indicadores de desempeño.
          .tarjeta.bgwhite.p-4(x="57%" y="22%" numero="+")
            h5.mb-4 Act
            p.mb-0 En la fase de actuación, decide si los cambios se promueven al entorno de producción o si requieren ajustes adicionales.
        AcordionA.d-lg-none(tipo="a" clase-tarjeta="tarjeta tarjeta--azul")
          div(titulo="Plan")
            p.mb-0 En la fase de planificación, el equipo identifica oportunidades de mejora a partir de los datos disponibles.
          div(titulo="Do")
            p.mb-0 En la fase de ejecución, aplica los cambios seleccionados en un entorno de pruebas.
          div(titulo="Check")
            p.mb-0 En la fase de verificación, mide el impacto de los cambios en los indicadores de desempeño.
          div(titulo="Act")
            p.mb-0 En la fase de actuación, decide si los cambios se promueven al entorno de producción o si requieren ajustes adicionales.

    p.mb-4 La mejora continua se alimenta de diversas fuentes de información que permiten identificar patrones, detectar oportunidades de optimización y orientar los ajustes del <em>chatbot</em>. El análisis conjunto de estos datos facilita una visión más completa de su funcionamiento y de las necesidades de los usuarios.
    p.mb-4 La siguiente tabla sintetiza las principales fuentes de información para la mejora continua del <em>chatbot</em> y su utilidad en la identificación de oportunidades de ajuste:
    .titulo-sexto.color-acento-contenido.mb-3.mt-4
      h5 Tabla 6.
      span Fuentes de información para la mejora continua del #[em chatbot]
    .tabla-a.color-acento-contenido.mb-4
      table
        thead
          tr
            th(scope="col") <strong>Fuente</strong>
            th(scope="col") <strong>Descripción</strong>
            th(scope="col") <strong>Uso recomendado</strong>
        tbody
          tr
            td Registros de conversación.
            td Histórico de mensajes intercambiados entre usuarios y <em>chatbot</em>.
            td Identificar consultas no atendidas y patrones de uso.
          tr
            td Indicadores de desempeño.
            td Métricas cuantitativas como tasa de comprensión y satisfacción.
            td Detectar deterioros tempranos y orientar prioridades.
          tr
            td Retroalimentación del usuario.
            td Encuestas breves al cierre de la conversación.
            td Capturar la percepción cualitativa del usuario.
          tr
            td Reportes de agentes humanos.
            td Observaciones del equipo que recibe los escalamientos.
            td Identificar temas que el <em>chatbot</em> no resuelve adecuadamente.
          tr
            td Análisis de temas emergentes.
            td Detección de nuevas consultas que aparecen con frecuencia.
            td Incorporar nuevas intenciones a la versión siguiente.

    p.mb-4 La mejora continua requiere acciones sistemáticas que permitan revisar el funcionamiento del chatbot, responder a los cambios, conservar los aprendizajes y fortalecer las capacidades del equipo. Estos aspectos se desarrollan a continuación:
    .BGF02.px-5.p-5.mb-4
      LineaTiempoC.color-acento-botones
        .row.align-items-center(titulo="a.")
          .col-lg-6.mb-4.mb-lg-0
            img(src="@/assets/curso/temas/t4/img15.png" alt="")
          .col-lg-6
            h5.mb-4 Revisión periódica
            p.mb-0 Conviene establecer una cadencia regular para revisar el <em>chatbot</em>. La frecuencia de estas revisiones debe ajustarse al volumen de uso, la frecuencia de los cambios en el negocio y los resultados obtenidos. Cada revisión genera un conjunto de ajustes que se priorizan, ejecutan y verifican antes de promoverlos al entorno productivo. Esta disciplina garantiza que el <em>chatbot</em> mantenga su utilidad y siga aportando valor a la organización a lo largo del tiempo.
        .row.align-items-center(titulo="b.")
          .col-lg-6.mb-4.mb-lg-0
            img(src="@/assets/curso/temas/t4/img16.png" alt="")
          .col-lg-6
            h5.mb-4 Revisión por eventos
            p.mb-0 La revisión periódica del <em>chatbot</em> debe complementarse con la revisión por eventos. Cuando ocurren cambios significativos en el negocio, como el lanzamiento de un nuevo producto, la modificación de procesos, cambios regulatorios o reestructuraciones internas, el <em>chatbot</em> debe ajustarse de inmediato para reflejar estos cambios. La falta de actualización oportuna puede llevar al <em>chatbot</em> a entregar información desactualizada o incorrecta, dañando la credibilidad de la organización ante sus usuarios.
        .row.align-items-center(titulo="c.")
          .col-lg-6.mb-4.mb-lg-0
            img(src="@/assets/curso/temas/t4/img17.png" alt="")
          .col-lg-6
            h5.mb-4 Gestión del conocimiento
            p.mb-0 Las lecciones aprendidas durante el proceso de ajuste deben capturarse en una base de conocimiento que pueda consultarse en proyectos futuros. Esta base de conocimiento incluye los problemas más frecuentes encontrados, las soluciones aplicadas, las técnicas que funcionaron y las que no, y las decisiones de diseño que se demostraron acertadas. Su existencia acelera significativamente el desarrollo de <em>chatbots</em> posteriores y reduce la probabilidad de repetir errores ya cometidos.
        .row.align-items-center(titulo="d.")
          .col-lg-6.mb-4.mb-lg-0
            img(src="@/assets/curso/temas/t4/img18.png" alt="")
          .col-lg-6
            h5.mb-4 Indicadores de mejora
            p.mb-0 Más allá de los indicadores de desempeño del <em>chatbot</em>, conviene monitorear indicadores propios del proceso de mejora: número de ajustes implementados por mes, tiempo promedio entre la detección de un hallazgo y su corrección, porcentaje de hallazgos resueltos en cada ciclo e impacto medible de cada ajuste en los indicadores principales. Estos metaindicadores permiten optimizar el proceso de mejora en sí mismo.
        .row.align-items-center(titulo="e.")
          .col-lg-6.mb-4.mb-lg-0
            img(src="@/assets/curso/temas/t4/img19.png" alt="")
          .col-lg-6
            h5.mb-4 Formación del equipo
            p.mb-0 A medida que el <em>chatbot</em> evoluciona, el equipo debe mantener actualizadas sus competencias técnicas y procedimentales. Esto puede lograrse mediante capacitaciones periódicas, certificaciones en las plataformas utilizadas, asistencia a eventos del sector y participación en comunidades de práctica. Un equipo bien formado aplica las mejores prácticas de la industria y produce <em>chatbots</em> de mayor calidad.

    p.mb-4 En proyectos exitosos de <em>chatbots</em>, se observan algunos patrones recurrentes que pueden orientar a los aprendices:
    .row.align-items-center.mb-4
      .col-lg-8.mb-4.mb-lg-0
        TabsA.color-acento-botones
          .tarjeta.bg05.p-4(titulo="Primero")
            p.mb-0 <strong>Primero</strong>, el compromiso de la alta dirección con el proyecto: cuando los líderes de la organización valoran y respaldan la iniciativa, los recursos fluyen y los obstáculos se superan más fácilmente.
          .tarjeta.bg05.p-4(titulo="Segundo")
            p.mb-0 <strong>Segundo</strong>, la formación de equipos interdisciplinarios que incluyen representantes del área técnica, del negocio, de servicio al cliente y de mercadeo.
          .tarjeta.bg05.p-4(titulo="Tercero")
            p.mb-0 <strong>Tercero</strong>, el enfoque iterativo, comenzando con un alcance reducido y expandiéndolo progresivamente con base en los aprendizajes.
          .tarjeta.bg05.p-4(titulo="Cuarto")
            p.mb-0 <strong>Cuarto</strong>, la cultura de medición, donde las decisiones se toman a partir de datos objetivos y no de intuiciones.
      .col-lg-4
        img(src="@/assets/curso/temas/t4/img20.svg" alt="")

    p.mb-4 La incorporación de <em>chatbots</em> puede generar beneficios como la reducción de consultas repetitivas, una atención más disponible, el aumento de la capacidad del equipo para atender casos complejos y una mejor recopilación de información sobre las necesidades de los usuarios. Estos resultados dependen de factores como el diseño de la solución, el volumen de uso, la calidad de las integraciones y el seguimiento posterior al lanzamiento.
    .row.align-items-center.mb-4
      .col-lg-4.mb-4.mb-lg-0
        img(src="@/assets/curso/temas/t4/img21.svg" alt="")
      .col-lg-8
        .cajon.color-primario.p-4.mb-4
          p.mb-0 Sin embargo, los proyectos de <em>chatbot</em> pueden enfrentar dificultades cuando no existe claridad sobre el problema que se busca resolver, las expectativas de los equipos están desalineadas, el alcance inicial es demasiado amplio, los datos de entrenamiento son insuficientes o no se realizan pruebas y seguimiento adecuados. Reconocer estas situaciones permite anticiparlas y establecer acciones preventivas durante el desarrollo y la evolución del <em>chatbot</em>.
        p.mb-4 Los <em>chatbots</em> tienen aplicaciones en diversos sectores, entre ellos la banca, las telecomunicaciones, el comercio electrónico, la salud, la educación, el gobierno digital, el turismo y la manufactura. Sus usos pueden abarcar la atención de consultas, el soporte, el seguimiento de solicitudes, la orientación de usuarios y la gestión de procesos, de acuerdo con las necesidades y características de cada sector.
        p.mb-0 A continuación, se ejemplifica un poco este proceso:

    .row.justify-content-center.mb-4.tema4-sectores
      .col-lg-10
        ImagenInfografica.color-acento-botones.d-none.d-lg-block
          template(v-slot:imagen)
            figure
              img(src="@/assets/curso/temas/t4/img22.svg" alt="")
          .tarjeta.bgwhite.p-4(x="65%" y="25%" numero="+")
            h5.mb-4 Banca y finanzas Alto
            p.mb-0 Consulta de saldo, transferencias, bloqueo de tarjetas.
          .tarjeta.bgwhite.p-4(x="70%" y="33%" numero="+")
            h5.mb-4 Telecomunicaciones Alto
            p.mb-0 Soporte técnico, consulta de planes, recargas.
          .tarjeta.bgwhite.p-4(x="74%" y="42%" numero="+")
            h5.mb-4 Comercio electrónico Medio-alto
            p.mb-0 Recomendación de productos, seguimiento de pedidos.
          .tarjeta.bgwhite.p-4(x="79%" y="50%" numero="+")
            h5.mb-4 Salud Medio
            p.mb-0 Agendamiento de citas, recordatorios, primer <em>triaje</em>.
          .tarjeta.bgwhite.p-4(x="79%" y="58%" numero="+")
            h5.mb-4 Educación Medio
            p.mb-0 Resolución de dudas, soporte a estudiantes.
          .tarjeta.bgwhite.p-4(x="74%" y="66%" numero="+")
            h5.mb-4 Gobierno digital Medio-bajo
            p.mb-0 Información ciudadana, orientación de trámites.
          .tarjeta.bgwhite.p-4(x="70%" y="74%" numero="+")
            h5.mb-4 Turismo y hospitalidad Medio-bajo
            p.mb-0 Reservas, recomendaciones, atención multilingüe.
          .tarjeta.bgwhite.p-4(x="65%" y="83%" numero="+")
            h5.mb-4 Manufactura y agro Bajo
            p.mb-0 Soporte interno, atención a distribuidores.
        AcordionA.d-lg-none(tipo="a" clase-tarjeta="tarjeta tarjeta--azul")
          div(titulo="Banca y finanzas Alto")
            p.mb-0 Consulta de saldo, transferencias, bloqueo de tarjetas.
          div(titulo="Telecomunicaciones Alto")
            p.mb-0 Soporte técnico, consulta de planes, recargas.
          div(titulo="Comercio electrónico Medio-alto")
            p.mb-0 Recomendación de productos, seguimiento de pedidos.
          div(titulo="Salud Medio")
            p.mb-0 Agendamiento de citas, recordatorios, primer <em>triaje</em>.
          div(titulo="Educación Medio")
            p.mb-0 Resolución de dudas, soporte a estudiantes.
          div(titulo="Gobierno digital Medio-bajo")
            p.mb-0 Información ciudadana, orientación de trámites.
          div(titulo="Turismo y hospitalidad Medio-bajo")
            p.mb-0 Reservas, recomendaciones, atención multilingüe.
          div(titulo="Manufactura y agro Bajo")
            p.mb-0 Soporte interno, atención a distribuidores.

    p.mb-4 Hay que aclarar que no todos los proyectos de <em>chatbot</em> terminan exitosamente. Los casos de fracaso suelen tener causas comunes:
    .tema4-fondo-cierre.p-4.mb-4
      .row.justify-content-center.align-items-center
        .col-lg-7.mb-4.mb-lg-0
          .tarjeta.bgwhite.shadow-sm.p-4
            ul.lista-ul.mb-0
              li.d-flex
                i.fas.fa-comment
                span Falta de claridad sobre el problema a resolver.
              li.d-flex
                i.fas.fa-comment
                span Expectativas desalineadas entre los equipos.
              li.d-flex
                i.fas.fa-comment
                span Alcance excesivo en la primera versión.
              li.d-flex
                i.fas.fa-comment
                span Datos de entrenamiento insuficientes.
              li.d-flex.mb-0
                i.fas.fa-comment
                span Falta de pruebas adecuadas o ausencia de seguimiento posterior al lanzamiento.
        .col-lg-3
          img(src="@/assets/curso/temas/t4/img23.svg" alt="")

    .row.justify-content-center.align-items-center.mb-0
      .col-auto.mb-4.mb-md-0
        img.tema4-icono.mx-auto(src="@/assets/curso/temas/t4/img24.svg" alt="")
      .col-md-9
        .bg04.p-4
          p.mb-0 Comprender estas causas ayuda a los aprendices a anticiparlas y prevenirlas en sus propios proyectos. La experiencia muestra que los proyectos de <em>chatbot</em> que aplican rigurosamente las prácticas aquí presentadas tienen significativamente más probabilidades de éxito que aquellos que las descuidan.
</template>

<script>
export default {
  name: 'Tema4',
  mounted() {
    this.$nextTick(() => {
      this.$aosRefresh()
    })
  },
  updated() {
    this.$aosRefresh()
  },
}
</script>
