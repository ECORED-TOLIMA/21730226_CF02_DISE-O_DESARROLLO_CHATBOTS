<template lang="pug">
.curso-main-container.pb-3.tema5
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span 5
      h1 Concepto y características del informe técnico

    .bloque-texto-g.bloque-texto-g--inverso.color-primario.p-3.p-sm-4.p-md-5.mb-4
      .bloque-texto-g__img(:style="{'background-image': `url(${require_src('@/assets/curso/temas/t5/img1.png')})`}")
      .bloque-texto-g__texto.p-4
        p.mb-0 El informe técnico del <em>chatbot</em> es el documento que registra de manera ordenada el proceso de configuración, construcción, verificación y ajuste del sistema conversacional. Su propósito es presentar las actividades realizadas, los resultados obtenidos, los hallazgos identificados, las correcciones aplicadas y las evidencias que permiten verificar el trabajo desarrollado.

    p.mb-4 Las características principales de un buen informe técnico son la claridad, la objetividad, la concisión, la precisión y la trazabilidad. Estas permiten presentar la información de manera comprensible, verificable, directa, exacta y respaldada por evidencias. La siguiente tabla sintetiza estas características y muestra su aplicación en la elaboración del informe:
    .titulo-sexto.color-acento-contenido.mb-3.mt-4
      h5 Tabla 7.
      span Características de un buen informe técnico
    .tabla-a.color-acento-contenido.mb-4
      table
        thead
          tr
            th(scope="col") <strong>Característica</strong>
            th(scope="col") <strong>Descripción</strong>
            th(scope="col") <strong>Ejemplo de aplicación</strong>
        tbody
          tr
            td Claridad.
            td Permite que cualquier lector con la formación adecuada comprenda el contenido sin esfuerzo excesivo, mediante lenguaje sencillo, estructura lógica y vocabulario adecuado al público.
            td Definir términos técnicos al introducirlos por primera vez.
          tr
            td Objetividad.
            td Exige respaldar las afirmaciones con datos verificables y evitar opiniones subjetivas, de manera que la información presentada pueda ser comprobada.
            td Reportar la tasa de comprensión con cifras exactas y la fuente de los datos.
          tr
            td Concisión.
            td Consiste en presentar la información necesaria de forma directa, evitando redundancias o repeticiones que dificulten la lectura.
            td Evitar repetir el mismo argumento en distintas secciones del informe.
          tr
            td Precisión.
            td Requiere que los datos numéricos, fechas, nombres y conceptos sean exactos y correspondan con la información disponible.
            td Verificar que las cifras coincidan con los reportes de la plataforma.
          tr
            td Trazabilidad.
            td Garantiza que las afirmaciones y resultados puedan rastrearse hasta las fuentes o evidencias que los respaldan.
            td Citar la bitácora de pruebas como soporte de los hallazgos reportados.

    p.mb-4 Además de estas características, el informe debe presentar la información de manera completa y organizada. La estructura visual, la ortografía, la selección de gráficos y la presentación general contribuyen a facilitar la lectura y respaldar la credibilidad del documento.
    p.mb-4 En cuanto al estilo de redacción, el informe técnico se redacta en tercera persona, con un tono neutro y profesional. Se evita el uso de la primera persona tanto del singular como del plural porque desplaza el foco del trabajo al autor. Por ejemplo:
    .row.justify-content-center.mb-4
      .col-md-6.col-lg-4.mb-4.mb-md-0
        .tarjeta-avatar
          img(src="@/assets/curso/temas/t5/img3.svg" alt="")
          .tarjeta.bg02.w-100
            .p-4.text-center
              p.mb-0 Se prefiere «se implementó el <em>chatbot</em>».
      .col-md-6.col-lg-4.mb-4.mb-md-0
        .tarjeta-avatar
          img(src="@/assets/curso/temas/t5/img2.svg" alt="")
          .tarjeta.bg02.w-100
            .p-4.text-center
              p.mb-0 En lugar de escribir «implementamos el <em>chatbot</em>».

    .row.justify-content-center.align-items-center.mb-4
      .col-auto.mb-4.mb-md-0
        img.tema5-icono.mx-auto(src="@/assets/curso/temas/t5/img4.svg" alt="")
      .col-md-9
        .bg04.p-4
          p.mb-0 Esta convención no es absoluta y algunas organizaciones permiten variaciones, pero la tercera persona impersonal es la opción más segura para informes técnicos formales en el contexto profesional colombiano.

    p.mb-4 Las normas técnicas y los estilos de citación proporcionan orientaciones para presentar documentos profesionales de manera organizada. Según el contexto del proyecto, pueden considerarse referentes como las normas técnicas colombianas y las normas APA para la presentación y citación de fuentes.
    .row.align-items-center.mb-4
      .col-lg-5.mb-4.mb-lg-0
        img(src="@/assets/curso/temas/t5/img5.png" alt="")
      .col-lg-7
        p.mb-4 Otro aspecto fundamental del informe técnico es la sección de evidencias y soportes. Esta sección, ubicada generalmente al final del documento, incluye todos los materiales que respaldan las afirmaciones realizadas a lo largo del informe. Entre estos materiales se encuentran capturas de pantalla del <em>chatbot</em> funcionando en distintos canales, diagramas del flujo conversacional construido, fragmentos de código de configuración, registros de las pruebas ejecutadas con sus resultados, gráficos con la evolución de los indicadores de desempeño y, cuando aplique, citas de retroalimentación recibida de usuarios reales.
        .bg01.p-4
          p.mb-0 La presentación de las evidencias debe ser cuidadosa. Cada elemento incluido debe estar correctamente referenciado desde el cuerpo del informe para que el lector pueda consultarlo en el momento adecuado. Las capturas de pantalla deben ser legibles y enfocadas en lo que se quiere mostrar, evitando incluir información irrelevante o sensible. Los gráficos deben tener leyendas claras y unidades de medida explícitas. Los fragmentos de código deben presentarse con tipografía monoespaciada y, cuando sea extenso, con resaltado de sintaxis para facilitar la lectura.

    p.mb-4 Cuando el informe técnico se entrega a una audiencia diversa, por ejemplo, una combinación de directivos, personal técnico y usuarios finales, conviene adaptar la información a las necesidades de cada grupo. Para ello, pueden elaborarse versiones diferenciadas:
    .row.align-items-center.mb-4
      .col-lg-8.mb-4.mb-lg-0
        AcordionA(tipo="b" clase-tarjeta="tarjeta tarjeta--azul")
          div(titulo="Versión ejecutiva")
            p.mb-0 Presenta de manera breve los principales resultados del proyecto, los indicadores de desempeño, los beneficios obtenidos y las decisiones que requieren atención. Está dirigida a directivos y responsables de la toma de decisiones que necesitan una visión general sin profundizar en los detalles técnicos.
          div(titulo="Versión técnica")
            p.mb-0 Desarrolla con mayor profundidad los aspectos relacionados con la configuración, construcción, verificación y ajuste del <em>chatbot</em>. Incluye detalles de implementación, pruebas realizadas, hallazgos, correcciones, integraciones y demás información necesaria para que el equipo técnico pueda mantener o continuar el proyecto.
          div(titulo="Versión orientada al usuario")
            p.mb-0 Utiliza un lenguaje más accesible y reduce el uso de términos especializados. Se enfoca en explicar los cambios incorporados, las funcionalidades disponibles, las mejoras realizadas y las indicaciones necesarias para comprender o utilizar adecuadamente el <em>chatbot</em>.
      .col-lg-4
        img(src="@/assets/curso/temas/t5/img6.png" alt="")

    p.mb-4 Estas versiones pueden complementarse con otras modalidades de presentación cuando las características del proyecto lo requieran. La siguiente tabla relaciona las principales audiencias con la versión recomendada y el énfasis de la información que debe presentarse en cada caso:
    .titulo-sexto.color-acento-contenido.mb-3.mt-4
      h5 Tabla 8.
      span Versiones diferenciadas del informe técnico según la audiencia
    .tabla-a.color-acento-contenido.mb-4
      table
        thead
          tr
            th(scope="col") <strong>Audiencia</strong>
            th(scope="col") <strong>Versión recomendada</strong>
            th(scope="col") <strong>Énfasis principal</strong>
        tbody
          tr
            td Directivos.
            td Versión ejecutiva (5-10 páginas).
            td Resultados de negocio, indicadores clave, retorno de inversión.
          tr
            td Equipo técnico.
            td Versión completa (30+ páginas).
            td Detalles de configuración, código, pruebas, hallazgos y ajustes.
          tr
            td Usuarios finales.
            td Versión orientada al usuario (1-3 páginas).
            td Cambios visibles, mejoras incorporadas, instrucciones de uso.
          tr
            td Auditoría.
            td Versión completa con anexos extendidos.
            td Cumplimiento normativo, trazabilidad, evidencias documentales.

    p.mb-4 La elaboración de versiones diferenciadas no implica redactar 3 documentos completamente distintos. En la práctica, se mantiene un documento maestro completo del que se derivan las distintas versiones, según las necesidades de cada audiencia. Esta aproximación garantiza la consistencia de la información y facilita el mantenimiento del documento a lo largo del proyecto.
    .row.justify-content-center.align-items-center.mb-0
      .col-auto.mb-4.mb-md-0
        img.tema5-icono.mx-auto(src="@/assets/curso/temas/t5/img7.svg" alt="")
      .col-md-9
        .bg04.p-4
          p.mb-0 Los apoyos visuales, como tablas, gráficos, capturas de pantalla y diagramas, deben incorporarse cuando aporten información relevante. Cada elemento debe estar correctamente numerado, titulado y relacionado con una explicación que oriente al lector sobre su propósito.

    Separador
    #t_5_1.titulo-segundo.color-acento-contenido(data-aos="fade-left")
      h2 5.1 Estructura y contenido del informe del #[em chatbot]

    p.mb-4 La estructura de un informe técnico de <em>chatbot</em> se adapta a las necesidades del proyecto, pero suele incluir las siguientes 9 secciones estándar que aseguran cubrir los aspectos esenciales. Esta estructura es ampliamente aceptada en la industria y facilita que distintos lectores encuentren rápidamente la información que necesitan:
    .BGF01.px-5.p-4.mb-4
      .row.align-items-center
        .col-lg-4.mb-4.mb-lg-0
          img.tema5-personaje.mx-auto(src="@/assets/curso/temas/t5/img8.png" alt="")
        .col-lg-8
          SlyderF(columnas="col-12 col-md-6 col-xl-4")
            .tarjeta.bgwhite.p-4.h-100.text-center
              img.tema5-icono.mx-auto.mb-4(src="@/assets/curso/temas/t5/img9.svg" alt="")
              h5.mb-4 1. Portada
              p.mb-0 Título, autor, organización, fecha y versión.
            .tarjeta.bgwhite.p-4.h-100.text-center
              img.tema5-icono.mx-auto.mb-4(src="@/assets/curso/temas/t5/img10.svg" alt="")
              h5.mb-4 2. Resumen Ejecutivo
              p.mb-0 Síntesis del proyecto, hallazgos clave y conclusiones.
            .tarjeta.bgwhite.p-4.h-100.text-center
              img.tema5-icono.mx-auto.mb-4(src="@/assets/curso/temas/t5/img11.svg" alt="")
              h5.mb-4 3. Introducción
              p.mb-0 Contexto del proyecto, problema abordado, objetivos y alcance.
            .tarjeta.bgwhite.p-4.h-100.text-center
              img.tema5-icono.mx-auto.mb-4(src="@/assets/curso/temas/t5/img12.svg" alt="")
              h5.mb-4 4. Metodología
              p.mb-0 Plataforma utilizada, intenciones definidas, casos de prueba aplicados.
            .tarjeta.bgwhite.p-4.h-100.text-center
              img.tema5-icono.mx-auto.mb-4(src="@/assets/curso/temas/t5/img13.svg" alt="")
              h5.mb-4 5. Desarrollo
              p.mb-0 Descripción detallada de la configuración, creación del flujo y verificación.
            .tarjeta.bgwhite.p-4.h-100.text-center
              img.tema5-icono.mx-auto.mb-4(src="@/assets/curso/temas/t5/img14.svg" alt="")
              h5.mb-4 6. Resultados
              p.mb-0 Datos cuantitativos: indicadores, tasas, casos exitosos y fallidos.
            .tarjeta.bgwhite.p-4.h-100.text-center
              img.tema5-icono.mx-auto.mb-4(src="@/assets/curso/temas/t5/img15.svg" alt="")
              h5.mb-4 7. Hallazgos y ajustes
              p.mb-0 Lista de hallazgos clasificados, ajustes aplicados y validación.
            .tarjeta.bgwhite.p-4.h-100.text-center
              img.tema5-icono.mx-auto.mb-4(src="@/assets/curso/temas/t5/img16.svg" alt="")
              h5.mb-4 8. Conclusiones y recomendaciones
              p.mb-0 Aprendizajes principales y propuestas de evolución del #[em chatbot].
            .tarjeta.bgwhite.p-4.h-100.text-center
              img.tema5-icono.mx-auto.mb-4(src="@/assets/curso/temas/t5/img17.svg" alt="")
              h5.mb-4 9. Anexos
              p.mb-0 Capturas de pantalla, bitácora de pruebas, código de configuración y referencias.

    p.mb-4 Cada sección cumple un propósito específico. La portada y el resumen ejecutivo permiten al lector identificar rápidamente el documento y comprender sus puntos clave en pocos minutos. La introducción contextualiza el proyecto y aclara qué problema se abordó. La metodología y el desarrollo explican cómo se construyó la solución, permitiendo a otros equipos replicar el trabajo o continuarlo. Los resultados presentan datos objetivos sobre el desempeño del <em>chatbot</em>. Los hallazgos y ajustes documentan las correcciones aplicadas. Las conclusiones y recomendaciones cierran el documento con aprendizajes útiles para el futuro. Los anexos proporcionan evidencia adicional para quienes desean profundizar.
    .row.justify-content-center.align-items-center.mb-4
      .col-auto.mb-4.mb-md-0
        img.tema5-icono.mx-auto(src="@/assets/curso/temas/t5/img18.svg" alt="")
      .col-md-9
        .bg04.p-4
          p.mb-0 El informe debe presentar los resultados de los indicadores definidos para evaluar el desempeño del <em>chatbot</em>, acompañados de datos que permitan interpretar objetivamente su desempeño.

    p.mb-4 Las recomendaciones para versiones posteriores deben derivarse de los resultados y hallazgos identificados durante la verificación. Estas pueden orientarse a corregir problemas pendientes, ampliar funcionalidades, mejorar el flujo conversacional o incorporar ajustes que contribuyan al funcionamiento del <em>chatbot</em>. Recomendaciones típicas incluyen ampliar las intenciones del <em>chatbot</em>, integrar nuevas plataformas, mejorar la voz y el tono según retroalimentación recibida o automatizar procesos adicionales que actualmente requieren intervención humana.
    .row.align-items-center.mb-4
      .col-lg-8.mb-4.mb-lg-0
        p.mb-4 Una buena práctica al elaborar el informe técnico es someterlo a revisión por pares antes de su entrega final. Otro miembro del equipo, ajeno a la redacción del documento, puede identificar errores de claridad, lagunas en la información o aspectos que no se explican adecuadamente. Esta revisión, aunque parece añadir trabajo, ahorra tiempo posterior al evitar que el lector final encuentre problemas que pudieron haberse corregido antes.
        .cajon.color-primario.p-4.mb-4
          p.mb-0 Adicionalmente, el informe técnico debe incluir una sección de control de versiones que registre las modificaciones realizadas a lo largo del tiempo. Cada versión debe identificar el autor del cambio, la fecha de modificación y un resumen de las modificaciones aplicadas. Este control de versiones es especialmente importante cuando el informe se actualiza periódicamente o cuando varias personas contribuyen a su elaboración.
        p.mb-0 En proyectos dirigidos al sector público pueden requerirse apartados adicionales relacionados con el cumplimiento normativo, especialmente cuando se gestionan datos personales o información de carácter institucional.
      .col-lg-4
        img(src="@/assets/curso/temas/t5/img19.png" alt="")

    p.mb-4 En síntesis, el campo de los <em>chatbots</em> y la inteligencia artificial conversacional se encuentra en plena expansión. Las tendencias descritas anticipan un futuro donde la conversación máquina-humano será aún más fluida, multimodal y personalizada de lo que ya es hoy.
    .cajon.color-secundario.p-4.mb-4
      p.mb-0 Adicionalmente, conviene reconocer que cada organización tiene su propio contexto, su cultura y sus restricciones específicas. Las recomendaciones generales presentadas deben adaptarse al contexto particular de cada proyecto. Lo que funciona en una gran empresa bancaria puede no aplicar a una pequeña empresa familiar; lo que es viable en una empresa de tecnología puede no serlo en una entidad pública con procesos rígidos. La capacidad para adaptar las prácticas a cada contexto es uno de los rasgos que distinguen a los profesionales experimentados de quienes están comenzando.

    p.mb-4 Los saberes técnicos sobre configuración, creación, verificación, ajuste y documentación de <em>chatbots</em> tienen aplicación inmediata en distintos contextos productivos:
    .row.align-items-center.mb-4
      .col-lg-4.mb-4.mb-lg-0
        img(src="@/assets/curso/temas/t5/img20.png" alt="")
      .col-lg-8
        AcordionA(tipo="b" clase-tarjeta="tarjeta tarjeta--azul")
          div(titulo="Atención al cliente")
            p.mb-0 Estas competencias permiten construir y mantener asistentes virtuales para responder preguntas frecuentes, atender consultas habituales y derivar casos complejos a un agente humano. Para ello, se requieren conocimientos de diseño conversacional, redacción clara y comprensión del negocio.
          div(titulo="Comercio electrónico")
            p.mb-0 Los <em>chatbots</em> pueden apoyar procesos de venta y postventa mediante recomendaciones de productos, seguimiento de pedidos y gestión de devoluciones. Su implementación requiere conocimientos de integración con sistemas de comercio, análisis del proceso de compra y <em>marketing</em> conversacional.
          div(titulo="Salud")
            p.mb-0 Los saberes adquiridos pueden aplicarse en soluciones para agendamiento de citas, recordatorios e información médica básica. En este contexto, es necesario considerar los protocolos correspondientes, el manejo de datos sensibles y la validación de los contenidos con personal especializado.
          div(titulo="Sector educativo")
            p.mb-0 Los <em>chatbots</em> pueden apoyar procesos académicos y administrativos, resolver dudas frecuentes y facilitar el acceso a información para los estudiantes. Su desarrollo requiere conocimientos de diseño pedagógico, redacción didáctica y manejo de plataformas de aprendizaje.
          div(titulo="Gobierno digital")
            p.mb-0 Contribuyen a acercar el Estado a la ciudadanía mediante soluciones para trámites, consultas y orientación sobre servicios. En este ámbito, son necesarias competencias relacionadas con el cumplimiento normativo, la accesibilidad y el uso de lenguaje claro.
          div(titulo="Emprendimiento propio")
            p.mb-0 Los conocimientos adquiridos también pueden aplicarse en servicios de consultoría e implementación de <em>chatbots</em> para pequeñas empresas y emprendimientos. Esta alternativa requiere combinar comunicación con clientes, gestión de proyectos y autonomía técnica para adaptar las soluciones a diferentes necesidades.

    p.mb-4 La aplicación de estos saberes no se limita a las grandes organizaciones. Las pequeñas y medianas empresas, así como los emprendimientos personales, pueden aprovechar los <em>chatbots</em> para diferenciarse de su competencia, profesionalizar su atención y operar con mayor eficiencia. Una pequeña tienda en línea, una clínica veterinaria, una academia de idiomas o una fundación social pueden implementar soluciones conversacionales con plataformas accesibles y obtener beneficios concretos en pocas semanas. Esta democratización de la tecnología abre oportunidades laborales y de emprendimiento para quienes dominen las competencias presentadas.
    .row.justify-content-center.mb-4
      .col-lg-10
        .tarjeta-avatar-b
          .tarjeta-avatar-b__img
            img(src="@/assets/curso/temas/t5/img21.svg" alt="")
          .tarjeta.bg02
            .p-4
              p.mb-0 El informe técnico reúne y organiza las decisiones, resultados, hallazgos, ajustes y evidencias generados durante el desarrollo del chatbot. Su elaboración facilita la comprensión de la solución, la transferencia de conocimiento, el mantenimiento del sistema y la toma de decisiones para futuras versiones.

    p.mb-4 De acuerdo con lo presentado sobre el informe técnico de <em>chatbots</em>, se relaciona una imagen que sintetiza sus principales características, estructura, tipos de presentación y evidencias de soporte:
    .titulo-sexto.color-acento-contenido.mb-3.mt-4
      h5 Figura 6.
      span Representación informe técnico #[em chatbots]
    .row.justify-content-center.mb-4
      .col-12.d-none.d-lg-block
        figure
          img(src="@/assets/curso/temas/t5/img22.svg" alt="Figura 6 que representa de manera general los principales elementos que conforman un informe técnico de chatbots, desde sus características y estructura hasta las evidencias que respaldan la documentación del proyecto")
      .col-12.d-block.d-lg-none
        figure
          img(src="@/assets/curso/temas/t5/img22_1.svg" alt="Figura 6 que representa de manera general los principales elementos que conforman un informe técnico de chatbots, desde sus características y estructura hasta las evidencias que respaldan la documentación del proyecto")
    p.mb-0 Para finalizar, se presenta un pódcast en el que se aborda la elaboración de un informe técnico de un <em>chatbot</em>. A través de una situación práctica, se revisan aspectos relacionados con su estructura, documentación de resultados, evidencias y recomendaciones, destacando la importancia de organizar y comunicar de manera clara el trabajo realizado:
    //- Pendiente de incorporar el pódcast oficial 21730226_CF02_Guion_Podcast_01.
</template>

<script>
export default {
  name: 'Tema5',
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
