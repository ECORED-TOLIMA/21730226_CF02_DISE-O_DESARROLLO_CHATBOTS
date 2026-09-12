<template lang="pug">
.curso-main-container.pb-3.tema3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span 3
      h1 Verificación del funcionamiento del #[em chatbot]

    .row.align-items-center.mb-0
      .col-lg-2.mb-4.mb-md-0.d-none.d-lg-block
        img(src="@/assets/curso/temas/t3/img1.svg" alt="")
      .col-md-10
        .bg04.p-4
          p.mb-0 La verificación del funcionamiento del <em>chatbot</em> es la fase en la que se valida que el sistema responda correctamente a las consultas previstas, manteniendo coherencia, precisión y empatía con el usuario. A continuación, se describen, en primer lugar, el procedimiento general de verificación; en segundo lugar, los indicadores de desempeño y los casos de prueba que permiten medir objetivamente la calidad del <em>chatbot</em> construido.

    Separador
    #t_3_1.titulo-segundo.color-acento-contenido(data-aos="fade-left")
      h2 3.1 Procedimiento de verificación

    p.mb-4 La verificación de un <em>chatbot</em> también, conocida como <em>testing</em> conversacional, consiste en someter el sistema a un conjunto de pruebas estructuradas que evalúan su comportamiento en distintos escenarios. Su objetivo es detectar errores antes de que el <em>chatbot</em> llegue a los usuarios finales y, de esta forma, evitar fallas que afecten la experiencia y dañen la reputación de la organización.
    p.mb-4 El procedimiento de verificación se compone de cuatro fases que se ejecutan de manera secuencial:
    .row.justify-content-center.mb-4
      .col-lg-10
        PasosA.color-primario(tipo="n")
          .row.align-items-center
            .col-md-9
              h5.mb-4 Planificación de la verificación
              p.mb-4 En esta fase se establecen los objetivos, el alcance y las condiciones bajo las cuales se realizará la verificación. Se determinan los escenarios que deben evaluarse, las funcionalidades que serán objeto de prueba, los criterios de aceptación y los responsables de ejecutar y documentar el proceso.
              p.mb-0 Resultado esperado: plan de pruebas documentado.
            .col-md-3.mt-4.mt-md-0
              img.tema3-icono-paso.mx-auto(src="@/assets/curso/temas/t3/img2.svg" alt="")
          .row.align-items-center.flex-md-row-reverse
            .col-md-9
              h5.mb-4 Diseño de los casos de prueba
              p.mb-4 En esta fase se construyen los casos que permitirán comprobar el comportamiento del <em>chatbot</em> en diferentes situaciones. Se redactan mensajes hipotéticos del usuario, se contemplan variaciones en las consultas y se define la respuesta o comportamiento esperado para cada escenario.
              p.mb-0 Resultado esperado: repositorio de casos de prueba.
            .col-md-3.mt-4.mt-md-0
              img.tema3-icono-paso.mx-auto(src="@/assets/curso/temas/t3/img3.svg" alt="")
          .row.align-items-center
            .col-md-9
              h5.mb-4 Ejecución de las pruebas
              p.mb-4 En esta fase se interactúa con el <em>chatbot</em> siguiendo los casos de prueba previamente definidos. Cada resultado se registra y se compara con el comportamiento esperado, identificando respuestas correctas, errores, fallas de interpretación, problemas en el flujo o situaciones que requieran revisión.
              p.mb-0 Resultado esperado: bitácora de ejecución con hallazgos.
            .col-md-3.mt-4.mt-md-0
              img.tema3-icono-paso.mx-auto(src="@/assets/curso/temas/t3/img4.svg" alt="")
          .row.align-items-center.flex-md-row-reverse
            .col-md-9
              h5.mb-4 Análisis de resultados y ajustes
              p.mb-4 En esta fase se revisan los resultados obtenidos durante las pruebas y se clasifican los hallazgos según su importancia. A partir de esta información, se priorizan las correcciones y se establecen los ajustes necesarios para mejorar el funcionamiento, la calidad de las respuestas y la experiencia del usuario.
              p.mb-0 Resultado esperado: informe de hallazgos y plan de ajustes.
            .col-md-3.mt-4.mt-md-0
              img.tema3-icono-paso.mx-auto(src="@/assets/curso/temas/t3/img5.svg" alt="")

    p.mb-4 Para sintetizar los aspectos principales de la verificación de un <em>chatbot</em>, el siguiente esquema resume el proceso de evaluación mediante las 4 fases que permiten identificar errores y establecer acciones de mejora:
    .titulo-sexto.color-acento-contenido.mb-3.mt-4
      h5 Figura 2.
      span Fases del proceso de verificación de un #[em chatbot]
    .row.justify-content-center.mb-4
      .col-12.d-none.d-lg-block
        figure
          img(src="@/assets/curso/temas/t3/img6.svg" alt="Figura 2 que presenta las 4 fases del proceso de verificación de un chatbot: planificación, diseño de los casos de prueba, ejecución de las pruebas y análisis de resultados y ajustes, organizadas de manera secuencial para evaluar y mejorar su funcionamiento.")
      .col-12.d-block.d-lg-none
        figure
          img(src="@/assets/curso/temas/t3/Group 1217074.svg" alt="Figura 2 que presenta las 4 fases del proceso de verificación de un chatbot: planificación, diseño de los casos de prueba, ejecución de las pruebas y análisis de resultados y ajustes, organizadas de manera secuencial para evaluar y mejorar su funcionamiento.")
    p.mb-4 Existen diferentes tipos de pruebas que pueden aplicarse a los <em>chatbots</em>, según el aspecto que se busca verificar. Entre las principales se encuentran las siguientes:
    AcordionA.mb-4(tipo="a" clase-tarjeta="tarjeta tarjeta--azul")
      div(titulo="Pruebas funcionales")
        .row.justify-content-center
          .col-lg-6.mb-4.mb-lg-0.order-2.order-lg-1
            p.mb-0 Validan que el <em>chatbot</em> ejecute correctamente las acciones esperadas y que cada componente del flujo responda de acuerdo con lo establecido. Permiten comprobar si el sistema comprende las intenciones del usuario, identifica y extrae las entidades necesarias, proporciona respuestas adecuadas y completa correctamente las tareas para las que fue diseñado, como agendar una cita, consultar un saldo, verificar el estado de un pedido o proporcionar información específica. También permiten detectar errores en las conexiones, condiciones, secuencias y acciones que hacen parte del flujo conversacional.
          .col-lg-6.col-10.mb-4.mb-lg-0.order-1.order-lg-2
            img(src="@/assets/curso/temas/t3/img7.png" alt="")
      div(titulo="Pruebas de experiencia de usuario")
        .row.justify-content-center
          .col-lg-6.mb-4.mb-lg-0.order-2.order-lg-1
            p.mb-4 Evalúan la calidad de la interacción desde la perspectiva de las personas que utilizan el <em>chatbot</em>. Además de verificar que la conversación funcione, permiten valorar aspectos como la naturalidad de los intercambios, el tono y la coherencia de las respuestas, la claridad de las instrucciones, la facilidad para completar una tarea y la capacidad del sistema para orientar al usuario cuando no comprende una solicitud. También consideran la percepción general del usuario, su nivel de satisfacción y posibles dificultades que puedan afectar la experiencia durante la conversación.
            p.mb-0 Una buena práctica es involucrar a usuarios reales en una fase de prueba <em>beta</em> antes del lanzamiento masivo. Estos usuarios, ajenos al equipo de desarrollo, identifican problemas que pasarían desapercibidos para quienes diseñaron el <em>chatbot</em>: malentendidos, ambigüedades, errores no contemplados y oportunidades de mejora. La prueba <em>beta</em> suele durar entre una y dos semanas, con un grupo de 10 a 20 usuarios y aporta información valiosísima sobre el comportamiento del <em>chatbot</em> en el mundo real.
          .col-lg-6.col-10.mb-4.mb-lg-0.order-1.order-lg-2
            img(src="@/assets/curso/temas/t3/img8.png" alt="")
      div(titulo="Pruebas de carga")
        .row.justify-content-center
          .col-lg-6.mb-4.mb-lg-0.order-2.order-lg-1
            p.mb-0 Se recomienda realizar pruebas de carga cuando se anticipa un alto volumen de uso. Estas pruebas simulan la interacción simultánea de numerosos usuarios para validar que el <em>chatbot</em> mantenga su desempeño bajo presión. Aunque las plataformas modernas suelen escalar automáticamente, conviene comprobar que las integraciones con sistemas externos, como bases de datos, sistemas de gestión de relaciones con clientes y plataformas de pagos, soporten la carga esperada sin degradar la experiencia.
          .col-lg-6.col-10.mb-4.mb-lg-0.order-1.order-lg-2
            img(src="@/assets/curso/temas/t3/img9.png" alt="")
      div(titulo="Pruebas exploratorias")
        .row.justify-content-center
          .col-lg-6.mb-4.mb-lg-0.order-2.order-lg-1
            p.mb-0 Las pruebas exploratorias son particularmente útiles para los <em>chatbots</em>, ya que permiten a los evaluadores interactuar libremente con el sistema sin seguir un guion predefinido. Su propósito es descubrir comportamientos inesperados o errores que podrían no haber sido contemplados en los casos de prueba estructurados. Este tipo de pruebas suele revelar problemas relacionados con el manejo del lenguaje natural, la transición entre temas y la respuesta del <em>chatbot</em> ante consultas ambiguas.
          .col-lg-6.col-10.mb-4.mb-lg-0.order-1.order-lg-2
            img(src="@/assets/curso/temas/t3/img10.png" alt="")
      div(titulo="Documentación de las pruebas")
        .row.justify-content-center
          .col-lg-6.mb-4.mb-lg-0.order-2.order-lg-1
            p.mb-0 Como parte del proceso de verificación, es importante documentar los resultados obtenidos en cada caso de prueba. Para ello, se registra si el caso fue aprobado, fallido o inconcluso y, cuando se presentan errores, se describe el comportamiento esperado, el comportamiento observado y, si es posible, la causa probable. Esta información, recopilada en una bitácora de pruebas, facilita el análisis de los hallazgos, la definición de acciones de mejora y la elaboración del informe técnico final.
          .col-lg-6.col-10.mb-4.mb-lg-0.order-1.order-lg-2
            img(src="@/assets/curso/temas/t3/img11.png" alt="")

    p.mb-4 Además del propósito de cada prueba, estas también pueden clasificarse según el momento del proyecto en que se realizan:
    .row.justify-content-center.mb-0
      .col-md-6.col-lg-4.mb-4.mb-lg-0
        .tarjeta-avatar
          img(src="@/assets/curso/temas/t3/img12.svg" alt="")
          .tarjeta.bg02.w-100
            .p-4.text-center
              h5.mb-4 Durante el desarrollo
              p.mb-0 El equipo realiza pruebas unitarias que validan cada bloque del flujo de forma aislada.
      .col-md-6.col-lg-4.mb-4.mb-lg-0
        .tarjeta-avatar
          img(src="@/assets/curso/temas/t3/img13.svg" alt="")
          .tarjeta.bg02.w-100
            .p-4.text-center
              h5.mb-4 Antes del lanzamiento
              p.mb-0 Se ejecutan pruebas de integración que validan el funcionamiento conjunto de todos los componentes.
      .col-md-6.col-lg-4
        .tarjeta-avatar
          img(src="@/assets/curso/temas/t3/img14.svg" alt="")
          .tarjeta.bg02.w-100
            .p-4.text-center
              h5.mb-4 Después del lanzamiento
              p.mb-0 Se realizan pruebas de regresión cada vez que se introduce un cambio, para garantizar que las funcionalidades previas no se hayan visto afectadas.

    Separador
    #t_3_2.titulo-segundo.color-acento-contenido(data-aos="fade-left")
      h2 3.2 Indicadores de desempeño y casos de prueba

    p.mb-4 Para medir objetivamente la calidad del <em>chatbot</em>, se utilizan indicadores clave de desempeño que cuantifican distintos aspectos de su funcionamiento. Estos indicadores deben definirse desde el inicio del proyecto, recogerse sistemáticamente durante la operación y revisarse de forma periódica para orientar las mejoras continuas. La siguiente tabla presenta algunos indicadores de referencia que pueden utilizarse para evaluar el desempeño de un <em>chatbot</em>:
    .titulo-sexto.color-acento-contenido.mb-3.mt-4
      h5 Tabla 3.
      span Indicadores clave de desempeño para #[em chatbots]
    .tabla-a.color-acento-contenido.mb-4
      table
        thead
          tr
            th(scope="col") <strong>Indicador</strong>
            th(scope="col") <strong>Definición</strong>
            th(scope="col") <strong>Referencia orientativa</strong>
        tbody
          tr
            td Tasa de comprensión.
            td Porcentaje de mensajes del usuario que el <em>chatbot</em> interpreta correctamente.
            td Idealmente superior al 80 %.
          tr
            td Tasa de finalización exitosa.
            td Porcentaje de conversaciones que terminan resolviendo la consulta.
            td Idealmente superior al 70 %.
          tr
            td Tasa de escalamiento.
            td Porcentaje de conversaciones transferidas a agentes humanos.
            td Entre 10 % y 25 % según el sector.
          tr
            td Tiempo promedio de conversación.
            td Duración media desde el saludo hasta el cierre.
            td Entre 1 y 3 minutos para <em>chatbots</em> simples.
          tr
            td Satisfacción del usuario.
            td Calificación promedio que los usuarios dan al <em>chatbot</em>.
            td Idealmente superior a 4 sobre 5.
          tr
            td Cobertura de intenciones.
            td Porcentaje de los temas relevantes que el <em>chatbot</em> atiende.
            td Crece progresivamente con cada versión.

    p.mb-4 Basado en lo anterior, la siguiente imagen presenta un panel de rendimiento de un <em>chatbot</em>, en el que se reúnen diferentes indicadores para evaluar la calidad y efectividad de las conversaciones:
    .titulo-sexto.color-acento-contenido.mb-3.mt-4
      h5 Figura 3.
      span Panel de rendimiento del #[em chatbot]
    .row.justify-content-center.mb-4
      .col-12.d-none.d-lg-block
        figure
          img(src="@/assets/curso/temas/t3/img15.png" alt="Figura 3 que presenta los principales indicadores para valorar el rendimiento de un chatbot, relacionando diferentes porcentajes y escalas de medición con aspectos como la comprensión de las solicitudes, la finalización exitosa de las conversaciones, el escalamiento, el tiempo promedio de interacción, la satisfacción del usuario y la cobertura de las intenciones.")
      .col-12.d-block.d-lg-none
        figure
          img(src="@/assets/curso/temas/t3/img15_1.png" alt="Figura 3 que presenta los principales indicadores para valorar el rendimiento de un chatbot, relacionando diferentes porcentajes y escalas de medición con aspectos como la comprensión de las solicitudes, la finalización exitosa de las conversaciones, el escalamiento, el tiempo promedio de interacción, la satisfacción del usuario y la cobertura de las intenciones.")
    h5.mt-4 <strong>Casos prueba</strong>
    p.mb-4 Los casos de prueba son el insumo principal para verificar el funcionamiento del <em>chatbot</em>. Cada caso describe un escenario concreto y la respuesta que el <em>chatbot</em> debería dar en ese escenario. La diversidad de casos es fundamental: deben incluirse no solo los flujos felices —donde todo sale bien— sino también los flujos de excepción donde el usuario se confunde, abandona, escribe con errores ortográficos o aborda temas fuera del alcance del <em>chatbot</em>.
    p.mb-4 Como ejemplos de casos de prueba para un <em>chatbot</em> se tienen los relacionados en la siguiente imagen:
    .titulo-sexto.color-acento-contenido.mb-3.mt-4
      h5 Figura 4.
      span Casos de prueba y respuesta
    .row.justify-content-center.mb-4
      .col-12.d-none.d-lg-block
        figure
          img(src="@/assets/curso/temas/t3/img16.svg" alt="Figura 4 que presenta ejemplos de mensajes de usuario y las respuestas esperadas del chatbot ante diferentes situaciones de interacción, como saludos, intenciones reconocidas, errores tipográficos, solicitudes fuera de alcance, requerimientos de atención humana, repetición de errores y despedidas.")
      .col-12.d-block.d-lg-none
        figure
          img(src="@/assets/curso/temas/t3/img16_1.svg" alt="Figura 4 que presenta ejemplos de mensajes de usuario y las respuestas esperadas del chatbot ante diferentes situaciones de interacción, como saludos, intenciones reconocidas, errores tipográficos, solicitudes fuera de alcance, requerimientos de atención humana, repetición de errores y despedidas.")
    p.mb-4 La cantidad de casos de prueba depende de la complejidad del <em>chatbot</em> y de la diversidad de escenarios que deba atender. Entre las estrategias y técnicas que pueden incorporarse para ampliar y analizar la cobertura de las pruebas se encuentran:
    .row.align-items-center.justify-content-center.mb-4
      .col-lg-8.mb-4.mb-lg-0.order-2.order-lg-1
        AcordionA(tipo="b" clase-tarjeta="tarjeta tarjeta--azul")
          div(titulo="Cobertura según la complejidad")
            p.mb-0 Para un <em>chatbot</em> simple con tres intenciones, puede establecerse un conjunto de casos que cubra las situaciones más relevantes, mientras que en soluciones más complejas será necesario ampliar progresivamente la cobertura. La cantidad y variedad de pruebas deben ajustarse a las funcionalidades, los riesgos identificados y los cambios que experimente el sistema.
          div(titulo="Matriz de confusión")
            p.mb-0 Para <em>chatbots</em> con alta variabilidad lingüística, conviene usar técnicas estadísticas como la matriz de confusión. Esta matriz cruza las intenciones detectadas por el <em>chatbot</em> con las intenciones reales de los mensajes, permitiendo identificar dónde el sistema confunde una intención con otra. Por ejemplo, si el <em>chatbot</em> frecuentemente confunde la intención «consultar saldo» con «consultar movimientos», la matriz de confusión lo evidenciará y orientará al equipo sobre dónde reforzar el entrenamiento.
          div(titulo="Pruebas A/B")
            p.mb-0 En proyectos de mayor envergadura, conviene incorporar la práctica de las pruebas A/B. Esta técnica consiste en lanzar dos versiones distintas del <em>chatbot</em> a diferentes grupos de usuarios y comparar los resultados obtenidos por cada una. Las pruebas A/B son particularmente útiles para validar decisiones de diseño cuando el equipo no está seguro sobre cuál opción funcionará mejor. Por ejemplo, si conviene usar un mensaje de bienvenida con 3 opciones o con 5, o si conviene saludar al usuario por su nombre o de manera genérica.
      .col-lg-4.col-8.mb-4.mb-lg-0.order-1.order-lg-2
        img(src="@/assets/curso/temas/t3/img17.png" alt="")

    p.mb-4 Vale la pena destacar que la verificación de un <em>chatbot</em> no es responsabilidad exclusiva del equipo técnico. Los expertos del negocio, quienes conocen a fondo los productos, los servicios y los clientes, deben participar activamente en la definición de los casos de prueba y en la evaluación de los resultados. Su perspectiva complementa la mirada técnica y ayuda a detectar errores que solo se evidencian desde el conocimiento profundo del dominio. Esta colaboración interdisciplinaria es uno de los factores más críticos para el éxito de cualquier proyecto de inteligencia artificial conversacional.
    p.mb-4 La siguiente tabla sintetiza los principales tipos de pruebas aplicables a los <em>chatbots</em>, considerando su propósito y el momento del ciclo de vida en que resultan más pertinentes:
    .titulo-sexto.color-acento-contenido.mb-3.mt-4
      h5 Tabla 4.
      span Tipos de pruebas aplicables a #[em chatbots]
    .tabla-a.color-acento-contenido.mb-4
      table
        thead
          tr
            th(scope="col") <strong>Tipo de prueba</strong>
            th(scope="col") <strong>Objetivo</strong>
            th(scope="col") <strong>Momento de aplicación</strong>
        tbody
          tr
            td Pruebas unitarias.
            td Validar el funcionamiento de cada bloque del flujo de forma aislada.
            td Durante el desarrollo, después de implementar cada bloque.
          tr
            td Pruebas de integración.
            td Validar el funcionamiento conjunto de todos los componentes y las integraciones externas.
            td Antes del lanzamiento, después de completar la implementación.
          tr
            td Pruebas funcionales.
            td Verificar que el <em>chatbot</em> ejecute correctamente las acciones esperadas.
            td Antes del lanzamiento y después de cada cambio significativo.
          tr
            td Pruebas de experiencia.
            td Evaluar aspectos cualitativos como naturalidad, tono y satisfacción.
            td Durante la fase beta y de manera periódica en producción.
          tr
            td Pruebas de carga.
            td Validar el desempeño bajo alto volumen de usuarios simultáneos.
            td Antes del lanzamiento masivo y antes de eventos de alto tráfico.
          tr
            td Pruebas exploratorias.
            td Descubrir comportamientos inesperados o errores no anticipados.
            td Durante todo el ciclo, complementando las pruebas estructuradas.
          tr
            td Pruebas de regresión.
            td Garantizar que cambios nuevos no rompan funcionalidades previas.
            td Después de cada modificación al <em>chatbot</em> ya en producción.
          tr
            td Pruebas A/B.
            td Comparar dos versiones distintas para identificar la mejor.
            td Cuando hay incertidumbre sobre cuál opción de diseño funciona mejor.

    p.mb-4 No todos los tipos de pruebas se aplican en todos los proyectos. Para <em>chatbots</em> simples, las pruebas funcionales, de experiencia y exploratorias suelen ser las más relevantes; mientras que las pruebas de carga y A/B son típicamente reservadas para <em>chatbots</em> de mayor envergadura o de uso masivo.
    .row.align-items-center.justify-content-center.mb-4
      .col-lg-4.col-8.mb-4.mb-lg-0
        img(src="@/assets/curso/temas/t3/img18.png" alt="")
      .col-lg-8
        .cajon.color-secundario.p-4.mb-4
          p.mb-0 La automatización de pruebas cobra relevancia conforme aumenta la complejidad del <em>chatbot</em> y la frecuencia de los cambios. Las plataformas modernas permiten ejecutar conjuntos de casos de prueba de manera programada y generar reportes sobre los resultados, lo que facilita detectar rápidamente errores en funcionalidades previamente validadas. La elección entre pruebas manuales y automatizadas depende del volumen de pruebas, los recursos disponibles y la frecuencia de actualización del <em>chatbot</em>; mientras que las pruebas manuales pueden ser suficientes en proyectos pequeños, la automatización resulta especialmente útil en soluciones de mayor complejidad o con cambios constantes.
        p.mb-0 Otro aspecto a considerar durante la verificación es el manejo de los datos de prueba. Idealmente, las pruebas se ejecutan en un entorno separado del de producción, con datos ficticios que simulen las condiciones reales sin afectar a usuarios o sistemas en operación. Las plataformas profesionales suelen ofrecer entornos diferenciados de desarrollo, prueba y producción, con mecanismos para mover el <em>chatbot</em> entre ellos siguiendo flujos de aprobación. Esta separación protege a los usuarios reales de los errores que puedan aparecer durante las pruebas.

    .row.align-items-center.justify-content-center.bg01.mb-4
      .col-lg-7.p-4.order-2.order-lg-1
        p.mb-0 Cuando varias personas trabajan en paralelo en el <em>chatbot</em>, también es necesario prever el manejo de los entornos y los cambios. Las plataformas profesionales suelen ofrecer mecanismos de control de cambios que permiten a varios desarrolladores realizar modificaciones sin interferir entre sí. Estos mecanismos incluyen el bloqueo temporal de elementos durante su edición, la fusión automática de cambios cuando son compatibles y el manejo manual de conflictos cuando dos personas modifican el mismo elemento simultáneamente. Una buena gestión de estos mecanismos evita la pérdida de trabajo y mantiene la coherencia de la solución.
      .col-lg-5.col-8.p-0.mb-4.mb-lg-0.order-1.order-lg-2
        img(src="@/assets/curso/temas/t3/img19.png" alt="")

    p.mb-4 Adicionalmente, los entornos de prueba deben mantenerse sincronizados con el de producción en cuanto a su configuración técnica. Cualquier diferencia entre los entornos puede generar comportamientos distintos que dificultan la verificación. Por ejemplo, si el entorno de prueba apunta a una base de datos vacía mientras que el de producción tiene millones de registros, los tiempos de respuesta serán distintos y los problemas de rendimiento solo aparecerán en producción. La sincronización adecuada de entornos requiere disciplina técnica, pero ahorra muchos dolores de cabeza posteriores.
    .row.justify-content-center.mb-0
      .col-lg-10
        .tarjeta-avatar-b
          .tarjeta-avatar-b__img
            img(src="@/assets/curso/temas/t3/img20.svg" alt="")
          .tarjeta.bg02
            .p-4
              p.mb-0 En cuanto a la duración de las pruebas, no existe una regla universal. Para <em>chatbots</em> simples, el período de pruebas puede ser más corto, mientras que para soluciones más complejas puede extenderse durante varias semanas o incluso meses. La presión por lanzar rápidamente debe equilibrarse con la necesidad de garantizar la calidad: lanzar un <em>chatbot</em> con problemas graves puede causar mayores pérdidas que retrasar el lanzamiento para corregirlos. La decisión final debe tomarse considerando el contexto específico de cada proyecto.
</template>

<script>
export default {
  name: 'Tema3',
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
