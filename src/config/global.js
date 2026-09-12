export default {
  global: {
    Name: 'Configuración, creación, verificación y documentación de flujos conversacionales.',
    Description:
      'Este componente aborda la configuración de parámetros y la creación de flujos conversacionales en <em>chatbots</em> simples; presenta el procedimiento para verificar y ajustar su funcionamiento; y orienta al aprendiz en la elaboración de informes técnicos que documenten los resultados, hallazgos y mejoras aplicadas al sistema conversacional.',
    imagenBannerPrincipal: '@/assets/curso/portada/banner-principal.png',
    fondoBannerPrincipal: '@/assets/curso/portada/fondo-banner-principal.png',
    imagenesDecorativasBanner: [
      {
        clases: ['banner-principal-decorativo-1', 'd-none', 'd-lg-block'],
        imagen: '@/assets/curso/portada/banner-principal-decorativo-1.svg',
      },
      {
        clases: ['banner-principal-decorativo-2', 'd-none', 'd-lg-block'],
        imagen: '@/assets/curso/portada/banner-principal-decorativo-2.svg',
      },
    ],
  },
  menuPrincipal: {
    menu: [
      {
        nombreRuta: 'inicio',
        icono: 'fas fa-home',
        titulo: 'Volver al inicio',
      },
      {
        nombreRuta: 'introduccion',
        icono: 'fas fa-info-circle',
        titulo: 'Introducción',
        desarrolloContenidos: true,
      },
      {
        nombreRuta: 'tema1',
        numero: '1',
        titulo: 'Configuración de los parámetros de la conversación',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '1.1',
            titulo: 'Parámetros generales del <em>chatbot</em>',
            hash: 't_1_1',
          },
          {
            numero: '1.2',
            titulo: 'Configuración del flujo y de los canales',
            hash: 't_1_2',
          },
        ],
      },
      {
        nombreRuta: 'tema2',
        numero: '2',
        titulo: 'Creación del flujo de conversación',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '2.1',
            titulo: 'Buenas prácticas de construcción',
            hash: 't_2_1',
          },
          {
            numero: '2.2',
            titulo: 'Ejemplo integrador para la atención al cliente',
            hash: 't_2_2',
          },
        ],
      },
      {
        nombreRuta: 'tema3',
        numero: '3',
        titulo: 'Verificación del funcionamiento del <em>chatbot</em>',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '3.1',
            titulo: 'Procedimiento de verificación',
            hash: 't_3_1',
          },
          {
            numero: '3.2',
            titulo: 'Indicadores de desempeño y casos de prueba',
            hash: 't_3_2',
          },
        ],
      },
      {
        nombreRuta: 'tema4',
        numero: '4',
        titulo: 'Ajuste de los flujos de conversación',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '4.1',
            titulo: 'Análisis de hallazgos y priorización',
            hash: 't_4_1',
          },
          {
            numero: '4.2',
            titulo: 'Iteración y mejora continua del chatbot',
            hash: 't_4_2',
          },
        ],
      },
      {
        nombreRuta: 'tema5',
        numero: '5',
        titulo: 'Concepto y características del informe técnico',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '5.1',
            titulo: 'Estructura y contenido del informe del chatbot',
            hash: 't_5_1',
          },
        ],
      },
    ],
    subMenu: [
      {
        icono: 'fas fa-sitemap',
        titulo: 'Síntesis',
        nombreRuta: 'sintesis',
        desarrolloContenidos: true,
      },
      {
        nombreRuta: 'actividad',
        icono: 'far fa-question-circle',
        titulo: 'Actividad didáctica',
        desarrolloContenidos: true,
      },
      {
        nombreRuta: 'glosario',
        icono: 'fas fa-sort-alpha-down',
        titulo: 'Glosario',
      },
      {
        icono: 'fas fa-book',
        titulo: 'Referencias bibliográficas',
        nombreRuta: 'referencias',
      },
      {
        icono: 'fas fa-file-pdf',
        titulo: 'Descargar PDF',
        download: 'downloads/21730226_CF02_CFA.pdf',
      },
      {
        icono: 'fas fa-download',
        titulo: 'Descargar material',
        download: 'downloads/material.zip',
      },
      {
        icono: 'far fa-registered',
        titulo: 'Créditos',
        nombreRuta: 'creditos',
      },
    ],
  },
  glosario: [
    {
      termino: 'Ajuste',
      terminoHtml: '<strong>Ajuste</strong>',
      significado:
        'corrección aplicada al flujo conversacional o a la configuración del <em>chatbot</em> a partir de hallazgos identificados.',
    },
    {
      termino: 'Bitácora de pruebas',
      terminoHtml: '<strong>Bitácora de pruebas</strong>',
      significado:
        'registro detallado de las pruebas ejecutadas con sus resultados y hallazgos asociados.',
    },
    {
      termino: 'Caso de prueba',
      terminoHtml: '<strong>Caso de prueba</strong>',
      significado:
        'escenario concreto con un mensaje hipotético del usuario y la respuesta esperada del <em>chatbot</em>.',
    },
    {
      termino: 'Ciclo plan-do-check-act',
      terminoHtml:
        '<strong>Ciclo <em>plan-do-</em></strong><strong><em>check</em></strong><strong><em>-</em></strong><strong><em>act</em></strong><strong></strong>',
      significado:
        'metodología iterativa de mejora basada en cuatro fases: planificación, ejecución, verificación y actuación.',
    },
    {
      termino: 'Indicador clave de desempeño',
      terminoHtml: '<strong>Indicador clave de desempeño</strong>',
      significado:
        'métrica cuantitativa que mide un aspecto específico del funcionamiento del <em>chatbot</em>.',
    },
    {
      termino: 'Mejora continua',
      terminoHtml: '<strong>Mejora continua</strong>',
      significado:
        'práctica de ciclos cortos de medición, análisis y ajuste para mantener el <em>chatbot</em> relevante en el tiempo.',
    },
    {
      termino: 'Prueba beta',
      terminoHtml: '<strong>Prueba beta</strong>',
      significado:
        'fase de pruebas con un grupo reducido de usuarios reales antes del lanzamiento masivo.',
    },
    {
      termino: 'Prueba de carga',
      terminoHtml: '<strong>Prueba de carga</strong>',
      significado:
        'pruebas que simulan la interacción simultánea de cientos o miles de usuarios para validar el desempeño bajo presión.',
    },
    {
      termino: 'Resumen ejecutivo',
      terminoHtml: '<strong>Resumen ejecutivo</strong>',
      significado:
        'síntesis del informe técnico que presenta los puntos clave en un máximo de una página.',
    },
    {
      termino: 'Testing conversacional',
      terminoHtml:
        '<strong><em>Testing</em></strong> <strong>conversacional</strong><strong></strong>',
      significado:
        'disciplina que combina pruebas de <em>software</em> con metodologías de experiencia de usuario aplicadas a <em>chatbots</em>.',
    },
    {
      termino: 'Trazabilidad',
      terminoHtml: '<strong>Trazabilidad</strong>',
      significado:
        'propiedad por la cual cada afirmación del informe puede rastrearse hasta su fuente original.',
    },
    {
      termino: 'Verificación',
      terminoHtml: '<strong>Verificación</strong>',
      significado:
        'proceso estructurado de pruebas que valida que un <em>chatbot</em> responda correctamente en distintos escenarios.',
    },
  ],
  referencias: [
    {
      referencia:
        'ICONTEC. (2018). NTC 1486: Documentación. Presentación de tesis, trabajos de grado y otros trabajos de investigación. Instituto Colombiano de Normas Técnicas.',
      link: '',
    },
    {
      referencia:
        'ISTQB. (2023). Foundation Level Syllabus. International Software Testing Qualifications Board.',
      link: '',
    },
    {
      referencia: 'Landbot. (2024). Documentación oficial de Landbot.',
      link: '',
    },
    {
      referencia: 'Microsoft. (2024). Bot Framework Documentation.',
      link: '',
    },
    {
      referencia:
        'MinTIC. (2023). Lineamientos para la implementación de asistentes virtuales en entidades públicas. Ministerio de Tecnologías de la Información y las Comunicaciones de Colombia.',
      link: '',
    },
    {
      referencia: 'OpenAI. (2024). GPT models documentation.',
      link: '',
    },
    {
      referencia:
        'Pérez, M. (2021). Diseño de <em>chatbots</em>: una guía práctica para crear conversaciones efectivas. Anaya Multimedia.',
      link: '',
    },
    {
      referencia:
        'Pressman, R. y Maxim, B. (2020). Ingeniería de <em>software</em>: un enfoque práctico (9.ª ed.). McGraw-Hill.',
      link: '',
    },
    {
      referencia: 'Rasa Technologies. (2024). Rasa Open Source Documentation.',
      link: '',
    },
    {
      referencia:
        'Sommerville, I. (2021). Software Engineering (10.ª ed.). Pearson.',
      link: '',
    },
  ],
  creditos: [
    {
      titulo: 'ECOSISTEMA DE RECURSOS EDUCATIVOS DIGITALES',
      autores: [
        {
          nombre: 'Claudia Johanna Gómez Pérez ',
          cargo:
            'Profesional G06. Responsable Ecosistema Virtual de Recursos Educativos Digitales',
          centro: 'Centro Agroturístico - Regional Santander',
        },
        {
          nombre: 'Diana Rocío Possos Beltrán',
          cargo: 'Responsable de línea de producción ',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
      ],
    },
    {
      titulo: 'CONTENIDO INSTRUCCIONAL',
      autores: [
        {
          nombre: 'Solanlly Sánchez Melo',
          cargo: 'Experta temática',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Andrés Felipe Velandia Espitia',
          cargo: 'Evaluador instruccional',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
      ],
    },
    {
      titulo: 'DISEÑO Y DESARROLLO DE RECURSOS EDUCATIVOS DIGITALES',
      autores: [
        {
          nombre: 'Oscar Ivan Uribe Ortiz ',
          cargo: 'Diseñador de contenidos digitales',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Jose Yobani Penagos Mora',
          cargo: 'Diseñador de contenidos digitales',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Veimar Celis Meléndez',
          cargo: 'Desarrollador <em>full stack</em>',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Gilberto Junior Rodríguez Rodríguez',
          cargo: 'Animador y productor audiovisual',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
      ],
    },
    {
      titulo: 'VALIDACIÓN RECURSO EDUCATIVO DIGITAL',
      autores: [
        {
          nombre: 'María Fernanda Pineda Mora',
          cargo: 'Evaluadora de contenidos inclusivos y accesibles',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Javier Mauricio Oviedo',
          cargo: 'Validador y vinculador de recursos educativos digitales',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
      ],
    },
  ],
  creditosAdicionales: {
    imagenes:
      'Fotografías y vectores tomados de <a href="https://www.freepik.es/" target="_blank">www.freepik.es</a>, <a href="https://www.shutterstock.com/" target="_blank">www.shutterstock.com</a>, <a href="https://unsplash.com/" target="_blank">unsplash.com </a>y <a href="https://www.flaticon.com/" target="_blank">www.flaticon.com</a>',
    creativeCommons:
      'Licencia creative commons CC BY-NC-SA<br><a href="https://creativecommons.org/licenses/by-nc-sa/2.0/" target="_blank">ver licencia</a>',
  },
}
