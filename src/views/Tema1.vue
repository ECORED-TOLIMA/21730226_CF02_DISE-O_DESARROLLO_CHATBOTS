<template lang="pug">
.curso-main-container.pb-3.tema1
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span 1
      h1 Configuración de los parámetros de la conversación

    figure.mb-4
      img(src="@/assets/curso/temas/t1/img1.png" alt="")

    p.mb-0 La configuración de los parámetros del <em>chatbot</em> determina su comportamiento en distintas situaciones y requiere una planificación cuidadosa. Por lo anterior, en primer lugar, se presentan los parámetros generales; en segundo lugar, los parámetros específicos relacionados con el flujo conversacional y los canales de comunicación.

    Separador
    #t_1_1.titulo-segundo.color-acento-contenido(data-aos="fade-left")
      h2 1.1 Parámetros generales del #[em chatbot]

    p.mb-4 Los parámetros generales son los elementos que cualquier <em>chatbot</em> debe tener configurados, independientemente de la plataforma o del sector en el que se utilice. Estos parámetros constituyen la base mínima funcional del sistema y contribuyen a mantener una experiencia coherente para el usuario.
    p.mb-4 Entre los principales parámetros se encuentran los siguientes, con su debida ejemplificación:
    .BGF02.px-5.p-5.mb-4
      LineaTiempoC.color-acento-botones(text-small)
        .row.align-items-center(titulo="a.")
          .col-lg-6.mb-4.mb-lg-0
            figure
              img(src="@/assets/curso/temas/t1/img2.png" alt="")
          .col-lg-6
            h5 Mensaje de bienvenida
            p.mb-4 Se configura al inicio del flujo para identificar el <em>chatbot</em>, comunicar sus capacidades principales y orientar al usuario sobre las opciones disponibles. Debe ser breve y coherente con la interacción.
            .tarjeta.bgwhite.shadow-sm.p-4
              p.mb-0 «¡Hola! Soy Pipo, el asistente virtual de la pizzería. Puedo ayudarte con el menú, el estado de tu pedido o información sobre nuestros horarios».
        .row.align-items-center(titulo="b.")
          .col-lg-6.mb-4.mb-lg-0
            figure
              img(src="@/assets/curso/temas/t1/img3.png" alt="")
          .col-lg-6
            h5 Mensaje de despedida
            p.mb-4 Permite cerrar la conversación de manera cordial, confirmar la finalización de la interacción y dejar abierta la posibilidad de una nueva consulta o interacción con el <em>chatbot</em>.
            .tarjeta.bgwhite.shadow-sm.p-4
              p.mb-0 «¡Gracias por comunicarte con nosotros! Esperamos atenderte nuevamente. ¡Que tengas un buen día!».
        .row.align-items-center(titulo="c.")
          .col-lg-6.mb-4.mb-lg-0
            figure
              img(src="@/assets/curso/temas/t1/img4.png" alt="")
          .col-lg-6
            h5 Mensaje de respaldo
            p.mb-4 Se configura para responder cuando el <em>chatbot</em> no comprende la solicitud del usuario. Debe ofrecer una alternativa que permita continuar la interacción o solicitar atención humana.
            .tarjeta.bgwhite.shadow-sm.p-4
              p.mb-0 «No logré comprender tu solicitud. Puedes escribir nuevamente tu pregunta o seleccionar una de las opciones disponibles. Si lo prefieres, puedo comunicarte con un asesor».
        .row.align-items-center(titulo="d.")
          .col-lg-6.mb-4.mb-lg-0
            figure
              img(src="@/assets/curso/temas/t1/img5.png" alt="")
          .col-lg-6
            h5 Tiempo de espera
            p.mb-4 Define el periodo de inactividad antes de cerrar una conversación. Su configuración depende del tipo de servicio y de las características de la interacción.
            .tarjeta.bgwhite.shadow-sm.p-4
              p.mb-0 «Han pasado 5 minutos sin recibir una respuesta. Cerraré esta conversación por ahora. Cuando necesites ayuda nuevamente, estaré disponible para atenderte».
        .row.align-items-center(titulo="e.")
          .col-lg-6.mb-4.mb-lg-0
            figure
              img(src="@/assets/curso/temas/t1/img6.png" alt="")
          .col-lg-6
            h5 Reglas de escalamiento
            p.mb-4 Establecen las condiciones para transferir la conversación a un agente humano. Pueden activarse por una solicitud directa del usuario o cuando el sistema identifica dificultades para continuar la interacción.
            .tarjeta.bgwhite.shadow-sm.p-4
              p.mb-0 Si el usuario escribe «Quiero hablar con un asesor» o si el <em>chatbot</em> no logra interpretar la solicitud después de varios intentos, se activa la transferencia.

    p.mb-0 En conjunto, los parámetros generales permiten establecer las condiciones básicas para el funcionamiento del <em>chatbot</em> y orientar su comportamiento durante la interacción. Una configuración adecuada de los mensajes, los tiempos de espera y las reglas de escalamiento contribuye a mantener conversaciones claras y coherentes, además de facilitar la atención de situaciones que requieren una respuesta diferente a la prevista. Estos elementos constituyen la base para avanzar hacia la configuración del flujo conversacional y su posterior verificación.

    Separador
    #t_1_2.titulo-segundo.color-acento-contenido(data-aos="fade-left")
      h2 1.2 Configuración del flujo y de los canales

    .bloque-texto-g.bloque-texto-g--inverso.color-primario.p-3.p-sm-4.p-md-5.mb-4
      .bloque-texto-g__img(:style="{'background-image': `url(${require_src('@/assets/curso/temas/t1/img7.png')})`}")
      .bloque-texto-g__texto.p-4
        p.mb-0 Adicionalmente a los parámetros generales, existen configuraciones específicas relacionadas con el funcionamiento del flujo y con los canales por los cuales se accede al <em>chatbot</em>. Estos parámetros se ajustan según las necesidades particulares de cada proyecto y pueden modificarse a lo largo del ciclo de vida del <em>chatbot</em>. Su adecuada configuración permite adaptar la interacción, establecer condiciones de operación, incorporar funcionalidades adicionales y mantener el sistema preparado para posteriores ajustes.
    .titulo-pastilla1.mt-4(data-aos="fade-down")
      img(src="@/assets/curso/icon.svg" alt="")
      span Configuración de la interacción
    p.mb-4 La configuración de la interacción reúne los elementos que permiten adaptar el comportamiento del <em>chatbot</em> a las características del usuario y a las condiciones en las que se desarrolla la conversación. En este grupo se consideran la información que el sistema puede conservar durante el diálogo, las condiciones regionales, los medios de acceso y las características lingüísticas de la interacción. Entre los principales aspectos se encuentran:
    TabsC.color-acento-botones.mb-4
      .py-4.py-md-5.px-4.bg02(titulo="Variables del usuario")
        .row.justify-content-center.align-items-center
          .col-lg-7.mb-4.mb-lg-0
            figure
              img(src="@/assets/curso/temas/t1/img8.png" alt="")
          .col-lg-5
            p.mb-0 Son los datos que el <em>chatbot</em> conserva durante la conversación, como el nombre, el número de documento, la ciudad o el correo electrónico. Estas variables permiten personalizar las respuestas y evitar solicitar información que el usuario ya proporcionó. Por ejemplo: «Gracias, Andrés. Hemos registrado tu solicitud y enviaremos la respuesta al correo electrónico proporcionado».
      .py-4.py-md-5.px-4.bg02(titulo="Idioma y zona horaria")
        .row.justify-content-center.align-items-center
          .col-lg-7.mb-4.mb-lg-0
            figure
              img(src="@/assets/curso/temas/t1/img9.png" alt="")
          .col-lg-5
            p.mb-0 Definen la configuración regional del <em>chatbot</em> y permiten adaptar la interacción a las características de los usuarios. Cuando una organización atiende diferentes regiones, estos parámetros ayudan a evitar confusiones relacionadas con el idioma o los horarios. Por ejemplo: un <em>chatbot</em> que atiende usuarios en Colombia y México puede mostrar los horarios de atención correspondientes a cada zona.
      .py-4.py-md-5.px-4.bg02(titulo="Canales de comunicación")
        .row.justify-content-center.align-items-center
          .col-lg-7.mb-4.mb-lg-0
            figure
              img(src="@/assets/curso/temas/t1/img10.png" alt="")
          .col-lg-5
            p.mb-0 Determinan los medios mediante los cuales los usuarios pueden acceder al <em>chatbot</em>. En esta configuración se habilitan los canales seleccionados para el proyecto y se incorporan las credenciales necesarias para su funcionamiento. Por ejemplo: un mismo <em>chatbot</em> puede configurarse para atender consultas desde un sitio <em>web</em>, WhatsApp, Messenger, Instagram o Telegram.
      .py-4.py-md-5.px-4.bg02(titulo="Horarios de atención")
        .row.justify-content-center.align-items-center
          .col-lg-7.mb-4.mb-lg-0
            figure
              img(src="@/assets/curso/temas/t1/img11.png" alt="")
          .col-lg-5
            p.mb-0 Permiten establecer comportamientos diferentes según el momento en que se realiza la consulta. Aunque el <em>chatbot</em> puede permanecer disponible de manera continua, algunas funciones, como la transferencia a un agente humano, pueden limitarse al horario laboral. Por ejemplo: «En este momento nuestros asesores no están disponibles. El horario de atención es de lunes a viernes, de 8:00 a. m. a 5:00 p. m. Puedes dejar tus datos y nos comunicaremos contigo».
      .py-4.py-md-5.px-4.bg02(titulo="Configuración multilingüe")
        .row.justify-content-center.align-items-center
          .col-lg-7.mb-4.mb-lg-0
            figure
              img(src="@/assets/curso/temas/t1/img12.png" alt="")
          .col-lg-5
            p.mb-0 Permite adaptar las respuestas a las características lingüísticas del público atendido. Cada idioma activo requiere revisar las intenciones, las frases de entrenamiento y las respuestas utilizadas en el flujo para mantener una interacción adecuada. Por ejemplo: un <em>chatbot</em> configurado en español e inglés puede presentar el saludo y las opciones iniciales según el idioma seleccionado por el usuario.

    p.mb-4 Estos elementos deben configurarse de manera coherente con las características del público, los canales disponibles y el propósito del <em>chatbot</em>. Su definición inicial también puede revisarse posteriormente cuando los resultados de las pruebas o las necesidades del servicio indiquen la conveniencia de realizar ajustes.
    .titulo-pastilla1.mt-4(data-aos="fade-down")
      img(src="@/assets/curso/icon.svg" alt="")
      span Configuraciones de operación y seguridad
    p.mb-4 Una vez establecidos los elementos que intervienen directamente en la interacción, la configuración debe contemplar las condiciones bajo las cuales opera el <em>chatbot</em> y las medidas necesarias para proteger al usuario, la información y las acciones que puede ejecutar. Estos aspectos permiten establecer el nivel de automatización, controlar las operaciones que requieren confirmación, proteger los datos y conservar la configuración del sistema para su recuperación. Entre ellos se encuentran:
    SlyderB.bg03.p-4.p-md-5.mb-4(:datos="datosOperacion")

    p.mb-4 La aplicación de estas configuraciones permite establecer condiciones de operación más seguras y controladas. Además, facilita que el sistema pueda mantenerse y recuperarse ante situaciones imprevistas sin perder el trabajo realizado durante su configuración.
    .titulo-pastilla1.mt-4(data-aos="fade-down")
      img(src="@/assets/curso/icon.svg" alt="")
      span Opciones avanzadas de configuración
    .row.align-items-center.mb-4
      .col-auto.mb-4.mb-md-0.d-none.d-lg-block
        img.tema1-icono(src="@/assets/curso/temas/t1/img18.svg" alt="")
      .col-md
        p.mb-0 Una vez establecidos los parámetros básicos de interacción, operación y seguridad, algunas plataformas profesionales ofrecen funcionalidades avanzadas que permiten adaptar el comportamiento del <em>chatbot</em> a necesidades específicas. Estas opciones pueden utilizarse cuando el proyecto requiere respuestas diferenciadas según el horario, la ubicación, el idioma, los grupos de usuarios o la interacción con sistemas externos.
    p.mb-4 Entre las principales funcionalidades se encuentran los horarios diferenciados, la geolocalización, la internacionalización, las pruebas A/B y los eventos personalizados. Para facilitar la identificación de su utilidad y aplicación práctica, la siguiente tabla relaciona cada opción con su función y presenta un caso de uso típico:
    .titulo-sexto.color-acento-contenido.mb-3.mt-4
      h5 Tabla 1.
      span Opciones avanzadas de configuración del #[em chatbot]
    .tabla-a.color-acento-contenido.mb-4
      table
        thead
          tr
            th(scope="col") <strong>Opción</strong>
            th(scope="col") <strong>Función</strong>
            th(scope="col") <strong>Caso de uso típico</strong>
        tbody
          tr
            td Horario diferenciado.
            td Comportamiento distinto según día u hora.
            td Mostrar promociones de almuerzo solo en horas de mediodía.
          tr
            td Geolocalización.
            td Personalización según ubicación del usuario.
            td Recomendar la sucursal más cercana al usuario.
          tr
            td Internacionalización.
            td Idioma adaptado automáticamente.
            td Saludar en español o inglés según el dispositivo.
          tr
            td Pruebas A/B.
            td Comparar variaciones del <em>chatbot</em>.
            td Probar dos mensajes de bienvenida con grupos distintos.
          tr
            td Eventos personalizados.
            td Activar acciones desde sistemas externos.
            td Notificar al usuario cuando llega su pedido.

    p.mb-4 El uso adecuado de estas opciones puede potenciar la eficacia del <em>chatbot</em>, pero requiere una planificación cuidadosa y, en muchos casos, talento técnico especializado. Las pequeñas y medianas empresas pueden comenzar con configuraciones básicas e incorporar progresivamente funcionalidades avanzadas a medida que aumentan sus necesidades, su madurez técnica y el volumen de uso. Esta aproximación permite evitar complejidad innecesaria al inicio del proyecto y aprovechar el aprendizaje obtenido durante cada etapa.
    .titulo-pastilla1.mt-4(data-aos="fade-down")
      img(src="@/assets/curso/icon.svg" alt="")
      span Gestión y documentación de la configuración
    p.mb-4 La configuración del <em>chatbot</em> no termina con su puesta en funcionamiento. Durante su ciclo de vida pueden surgir ajustes, actualizaciones o cambios derivados de los resultados obtenidos, las necesidades del servicio o la incorporación de nuevas funcionalidades. Por ello, es necesario establecer criterios para gestionar las modificaciones y conservar información sobre las decisiones adoptadas.
    p.mb-4 En cuanto a la actualización de la configuración, es importante diferenciar entre cambios menores y cambios mayores:
    .tarjeta--container.row.mb-4
      .col-md-6.tarjeta.bg01.p-4.p-lg-5
        .row.justify-content-center.mb-4
          .col-5.col-lg-4
            figure
              img(src="@/assets/curso/temas/t1/img19.svg" alt="")
        h5.text-center Cambios menores
        p.mb-0 Corresponden a ajustes en mensajes específicos, modificaciones de tiempos de espera o correcciones ortográficas. Pueden aplicarse directamente al ambiente de producción después de una validación rápida.
      .col-md-6.tarjeta.bg05.p-4.p-lg-5
        .row.justify-content-center.mb-4
          .col-5.col-lg-4
            figure
              img(src="@/assets/curso/temas/t1/img20.svg" alt="")
        h5.text-center Cambios mayores
        p.mb-0 Comprenden la incorporación de nuevas intenciones, modificaciones del flujo principal o integración con nuevos sistemas. Requieren pruebas exhaustivas en un ambiente de prueba y revisión antes de su promoción a producción.

    p.mb-4 Esta diferenciación permite mantener la estabilidad del <em>chatbot</em> y, al mismo tiempo, facilitar los ajustes necesarios durante su funcionamiento. Las plataformas profesionales suelen ofrecer mecanismos de control de versiones, que permiten conservar configuraciones anteriores y regresar a una versión estable cuando un cambio introduce problemas inesperados. Esta capacidad de reversión resulta especialmente útil cuando se presentan dificultades después de una actualización.
    .row.justify-content-center.mb-4
      .col-lg-10
        .tarjeta-avatar-b
          .tarjeta-avatar-b__img
            img(src="@/assets/curso/temas/t1/img21.svg" alt="")
          .tarjeta.bg02
            .p-4
              p.mb-0 La documentación de la configuración también forma parte de esta gestión. Deben registrarse los valores asignados a los parámetros, las razones de las decisiones tomadas, las modificaciones realizadas y, cuando sea necesario, las fuentes consultadas para fundamentarlas. Esta información facilita el mantenimiento posterior y permite que nuevos integrantes del equipo comprendan la configuración existente.
    .row.justify-content-center.mb-4
      .col-lg-10
        .bg04.p-4
          p.mb-0 Además, la documentación constituye un insumo importante para el informe técnico final, porque permite disponer de evidencias sobre las configuraciones realizadas, los cambios aplicados y las decisiones tomadas durante el desarrollo del <em>chatbot</em>. De esta manera, el informe no se limita a presentar resultados, sino que puede relacionarlos con el proceso de configuración y ajuste desarrollado.
    p.mb-4 Antes de poner en producción un <em>chatbot</em>, es recomendable realizar una revisión final de los principales elementos configurados. Esta comprobación permite verificar que los parámetros definidos respondan a las condiciones previstas para el funcionamiento del sistema y que los aspectos relacionados con la interacción, la seguridad, los tiempos de respuesta y los canales hayan sido considerados. La siguiente información reúne los aspectos que deben validarse y las preguntas que orientan esta revisión:
    .row.justify-content-center.mb-4.tema1-revision-final
      .col-lg-10
        ImagenInfografica.color-acento-botones.d-none.d-lg-block
          template(v-slot:imagen)
            figure
              img(src="@/assets/curso/temas/t1/img22.svg" alt="")
          .tarjeta.bgwhite.p-4(x="64%" y="22.5%" numero="+")
            h5.mb-4 Mensaje de bienvenida
            p.mb-0 ¿Presenta al <em>chatbot</em>, indica sus capacidades y orienta al usuario sobre cómo proceder?
          .tarjeta.bgwhite.p-4(x="36%" y="30.2%" numero="+")
            h5.mb-4 Mensaje de respaldo
            p.mb-0 ¿Es empático, no culpa al usuario y ofrece alternativas concretas?
          .tarjeta.bgwhite.p-4(x="64%" y="37.9%" numero="+")
            h5.mb-4 Mensaje de despedida
            p.mb-0 ¿Cierra la conversación de forma cordial e invita al usuario a regresar?
          .tarjeta.bgwhite.p-4(x="36%" y="45.6%" numero="+")
            h5.mb-4 Reglas de escalamiento
            p.mb-0 ¿Existe una vía clara para que el usuario hable con un humano cuando lo necesite?
          .tarjeta.bgwhite.p-4(x="64%" y="53.3%" numero="+")
            h5.mb-4 Tiempos de espera
            p.mb-0 ¿Está configurado un tiempo razonable de inactividad antes de cerrar la sesión?
          .tarjeta.bgwhite.p-4(x="36%" y="61%" numero="+")
            h5.mb-4 Privacidad de datos
            p.mb-0 ¿Se evita pedir información sensible directamente en el chat?
          .tarjeta.bgwhite.p-4(x="64%" y="68.7%" numero="+")
            h5.mb-4 Frases de entrenamiento
            p.mb-0 ¿Hay al menos 10 a 15 frases por intención, con variaciones realistas?
          .tarjeta.bgwhite.p-4(x="36%" y="76.4%" numero="+")
            h5.mb-4 Canales activos
            p.mb-0 ¿Están correctamente configurados los canales y sus credenciales?
        figure.d-lg-none
          img(src="@/assets/curso/temas/t1/img22_1.svg" alt="")

    .row.justify-content-center.mb-4
      .col-auto.mb-4.mb-md-0.d-none.d-lg-block
        img.tema1-icono(src="@/assets/curso/temas/t1/img23.svg" alt="")
      .col-lg-11
        .bg04.p-3
          p.mb-0 La revisión de estos aspectos permite identificar posibles ajustes antes de avanzar a la etapa de verificación del funcionamiento. Así, la configuración queda preparada para las pruebas correspondientes y para documentar posteriormente los resultados, hallazgos y mejoras aplicadas al sistema conversacional.
</template>

<script>
export default {
  name: 'Tema1',
  data: () => ({
    datosOperacion: [
      {
        titulo: 'Modo de operación',
        texto:
          'El <em>chatbot</em> puede funcionar en modo automático, donde responde por sí mismo sin intervención humana, o en modo asistido, donde un agente supervisa las respuestas antes de enviarlas. El modo asistido puede utilizarse durante las primeras etapas de implementación, cuando el equipo aún está validando la calidad del sistema, y desactivarse progresivamente a medida que aumenta la confianza en sus respuestas.',
        imagen: '@/assets/curso/temas/t1/img13.png',
        leyendaImagen: '',
      },
      {
        titulo: 'Acciones automáticas',
        texto:
          'Permiten que el <em>chatbot</em> ejecute operaciones a partir de las solicitudes del usuario. Cuando estas acciones pueden tener consecuencias importantes, es conveniente establecer mecanismos de confirmación antes de ejecutarlas y registrar las acciones realizadas en las bitácoras del sistema. Esto facilita su seguimiento, permite identificar posibles errores y aporta información para revisar el funcionamiento del <em>chatbot</em>.',
        imagen: '@/assets/curso/temas/t1/img14.png',
        leyendaImagen: '',
      },
      {
        titulo: 'Seguridad y protección de datos',
        texto:
          'Deben considerarse desde la configuración del <em>chatbot</em>. En Colombia, las organizaciones deben tener en cuenta las disposiciones de la Ley 1581 de 2012 relacionadas con el tratamiento de datos personales. Por ello, se deben establecer mecanismos para informar al usuario sobre el tratamiento de sus datos y, cuando corresponda, permitirle ejercer sus derechos sobre la información proporcionada.',
        imagen: '@/assets/curso/temas/t1/img15.png',
        leyendaImagen: '',
      },
      {
        titulo: 'Protección de información sensible',
        texto:
          'El <em>chatbot</em> no debe solicitar directamente contraseñas, números completos de tarjetas de crédito o claves de seguridad. Cuando sea necesario autenticar al usuario, conviene utilizar canales seguros, como el portal <em>web</em> de la organización o una aplicación móvil con mecanismos adecuados de autenticación. Esta práctica protege la información del usuario y reduce los riesgos asociados con suplantaciones o fraudes.',
        imagen: '@/assets/curso/temas/t1/img16.png',
        leyendaImagen: '',
      },
      {
        titulo: 'Respaldo y recuperación',
        texto:
          'Permiten conservar los elementos principales del <em>chatbot</em> y restaurarlos en caso de pérdida, corrupción o necesidad de migración. Las plataformas profesionales suelen permitir exportar la configuración de los flujos, intenciones, frases de entrenamiento y parámetros. Se recomienda realizar respaldos periódicos y comprobar que puedan restaurarse correctamente.',
        imagen: '@/assets/curso/temas/t1/img17.png',
        leyendaImagen: '',
      },
    ],
  }),
  mounted() {
    this.$nextTick(() => this.$aosRefresh())
  },
  updated() {
    this.$aosRefresh()
  },
}
</script>
