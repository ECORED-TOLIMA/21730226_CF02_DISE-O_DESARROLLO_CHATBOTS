"""Preparación reproducible del CF02 desde sus Word oficiales.

Ejecutar solo para regenerar la base textual, antes de la maquetación visual:
python scripts/prepare-cf02.py
No ejecutar sobre temas ya maquetados: reemplaza las cinco vistas de temas.
"""
from pathlib import Path
import html
import json
import re
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
      'dgm': 'http://schemas.openxmlformats.org/drawingml/2006/diagram',
      'mc': 'http://schemas.openxmlformats.org/markup-compatibility/2006'}


def write(path, text):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding='utf-8')


def dumps(value):
    return json.dumps(value, ensure_ascii=False, indent=2)


def clean_choices(node):
    # Choice y Fallback representan el mismo cuadro: conservar solo Choice.
    for parent in list(node.iter()):
        for child in list(parent):
            if child.tag == '{' + NS['mc'] + '}AlternateContent':
                choice = child.find('mc:Choice', NS)
                if choice is None:
                    choice = child.find('mc:Fallback', NS)
                index = list(parent).index(child)
                parent.remove(child)
                if choice is not None:
                    for item in reversed(list(choice)):
                        parent.insert(index, item)


def plain(node):
    return ''.join(t.text or '' for t in node.findall('.//w:t', NS)).strip()


def inline(node):
    result = []
    def visit(el):
        tag = el.tag.split('}')[-1]
        if tag in ('drawing', 'pict', 'txbxContent'):
            return
        if tag == 'r':
            value = ''.join(html.escape(c.text or '', quote=False) if c.tag.endswith('}t')
                            else '<br>' if c.tag.endswith('}br') else ' ' if c.tag.endswith('}tab') else ''
                            for c in el)
            if not value:
                return
            for key, markup in [('i', 'em'), ('b', 'strong')]:
                prop = el.find('w:rPr/w:' + key, NS)
                if prop is not None and prop.get('{' + NS['w'] + '}val') not in ('0', 'false', 'off'):
                    value = f'<{markup}>{value}</{markup}>'
            result.append(value)
        else:
            for child in el:
                visit(child)
    visit(node)
    return ''.join(result).strip()


def pug(value):
    # El HTML inline preserva cursivas; escapar la interpolación propia de Pug.
    return value.replace('#{', '&#35;{').replace('!{', '&#33;{').replace('\n', ' ')


def paragraphs(node):
    text = inline(node)
    values = [text] if text else []
    for box in node.findall('.//w:txbxContent', NS):
        values += [inline(p) for p in box.findall('w:p', NS) if inline(p)]
    return list(dict.fromkeys(values))


def view(name, title, content, number=None, icon=None):
    lines = ['<template lang="pug">', '.curso-main-container.pb-3', '  BannerInterno',
             '  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5',
             '    .titulo-principal.color-acento-contenido', '      .titulo-principal__numero']
    if number:
        lines += [f'        span {number}']
    else:
        lines += ['        span', f'          i.{icon or "fas.fa-info"}']
    lines += [f'      h1 {title}', ''] + ['    ' + x if x else '' for x in content]
    return '\n'.join(lines) + f'\n</template>\n\n<script>\nexport default {{\n  name: {json.dumps(name)},\n}}\n</script>\n'


def prepare():
    archive = zipfile.ZipFile(ROOT / 'fuentes/21730226_CF02_DI.docx')
    doc = ET.fromstring(archive.read('word/document.xml'))
    clean_choices(doc)
    body = list(doc.find('w:body', NS))
    rels = {r.get('Id'): r.get('Target') for r in ET.fromstring(archive.read('word/_rels/document.xml.rels'))}
    comments = ET.fromstring(archive.read('word/comments.xml'))
    alts = [plain(c).split('Texto alternativo:', 1)[1].strip() for c in comments if 'Texto alternativo:' in plain(c)]
    metadata = [plain(p) for p in body[6].findall('.//w:p', NS) if plain(p)]
    title = metadata[metadata.index('NOMBRE DEL COMPONENTE FORMATIVO') + 1]
    description = metadata[metadata.index('BREVE DESCRIPCIÓN') + 1]
    themes, current = [], None
    audit = {'source': '21730226_CF02_DI.docx', 'themes': [], 'pending': ['Video oficial', 'Pódcast oficial']}

    def table_lines(table):
        rows = []
        for row in table.findall('w:tr', NS):
            rows.append(['<br>'.join(inline(p) for p in c.findall('w:p', NS) if inline(p)) for c in row.findall('w:tc', NS)])
        lines = ['.tabla-a.color-acento-contenido.mb-4', '  table']
        # Las dos tablas sin rótulo numerado son colecciones sin cabecera.
        header = rows and re.sub('<[^>]+>', '', rows[0][0]).strip() in ['Opción', 'Elemento', 'Indicador', 'Tipo de prueba', 'Tipo de ajuste', 'Fuente', 'Característica', 'Audiencia']
        if header:
            lines += ['    thead', '      tr'] + ['        th(scope="col") ' + pug(c) for c in rows[0]]
        lines += ['    tbody']
        for row in rows[1:] if header else rows:
            lines += ['      tr'] + ['        td ' + pug(c) for c in row]
        return lines, rows

    for index in range(50, 476):
        block = body[index]
        np = block.find('w:pPr/w:numPr', NS)
        num = np.find('w:numId', NS).get('{' + NS['w'] + '}val') if np is not None else None
        level = np.find('w:ilvl', NS).get('{' + NS['w'] + '}val') if np is not None else None
        texts = paragraphs(block)
        if num == '1' and level == '0':
            current = {'title': plain(block), 'number': len(themes) + 1, 'subs': [], 'lines': [], 'source': []}
            themes.append(current)
            continue
        if current is None:
            continue
        lines = current['lines']
        if num == '1' and level == '1':
            sub = {'number': f'{current["number"]}.{len(current["subs"]) + 1}', 'title': plain(block)}
            sub['hash'] = 't_' + sub['number'].replace('.', '_')
            current['subs'].append(sub)
            if lines and lines[-1].startswith('p.mb-4 '):
                lines[-1] = lines[-1].replace('p.mb-4', 'p.mb-0', 1)
            lines += ['', 'Separador', f'#{sub["hash"]}.titulo-segundo.color-acento-contenido(data-aos="fade-left")', f'  h2 {sub["number"]} {sub["title"]}', '']
        elif block.tag.endswith('}tbl') and index == 175:
            # El Word utiliza una tabla de maquetación para este texto narrativo.
            for p in block.findall('.//w:tc/w:p', NS):
                text = inline(p)
                if text:
                    lines += ['p.mb-4 ' + pug(text)]
                    current['source'].append({'index': index, 'html': text})
        elif block.tag.endswith('}tbl'):
            rendered, rows = table_lines(block)
            lines += rendered + ['']
            current['source'].append({'index': index, 'table': rows})
        else:
            for text in texts:
                raw = html.unescape(re.sub('<[^>]*>', '', text))
                if '21730226_CF02_Guion_' in raw:
                    lines += ['//- Pendiente de incorporar el pódcast oficial 21730226_CF02_Guion_Podcast_01.']
                    continue
                match = re.match(r'(Tabla|Figura) (\d+)\.\s*(.*)', raw)
                if match:
                    lines += ['.titulo-sexto.color-acento-contenido.mb-3.mt-4', f'  h5 {match[1]} {match[2]}.', f'  span {match[3]}']
                elif num and len(raw) < 110 and not raw.endswith('.'):
                    lines += ['h5.mt-4 ' + pug(text)]
                elif num:
                    lines += ['ul.lista-ul.mb-4', '  li', '    i.fas.fa-angle-right', '    span ' + pug(text)]
                else:
                    lines += ['p.mb-4 ' + pug(text)]
                current['source'].append({'index': index, 'html': text})
            # Figuras originales de referencia; las imágenes decorativas
            # se asociarán con los recursos exportados en la maquetación por bloques.
            if index in [165, 226, 260, 270, 331, 469]:
                blip = block.find('.//a:blip', NS)
                if blip is not None:
                    target = rels[blip.get('{' + NS['r'] + '}embed')]
                    dest = f'src/assets/curso/temas/t{current["number"]}/fuente-{index}.png'
                    (ROOT / dest).write_bytes(archive.read('word/' + target))
                    fig_nums = {165: 1, 226: 2, 260: 3, 270: 4, 331: 5, 469: 6}
                    alt = next((a for a in alts if a.startswith('Figura ' + str(fig_nums.get(index, 0)) + ' ')), '')
                    lines += ['.row.justify-content-center.mb-4', '  .col-12', '    figure', f'      img(src="@/{dest[4:]}" alt={json.dumps(alt, ensure_ascii=False)})']
            if index == 440:
                # El comentario editorial contiene el texto completo del recurso.
                comment = next(plain(c) for c in comments if '1. PortadaTítulo, autor' in plain(c))
                entries = re.findall(r'(\d)\. (.*?)(?=\d\. |$)', comment.split('Textos:', 1)[1])
                labels = ['Portada', 'Resumen Ejecutivo', 'Introducción', 'Metodología', 'Desarrollo', 'Resultados', 'Hallazgos y ajustes', 'Conclusiones y recomendaciones', 'Anexos']
                for (number, entry), label in zip(entries, labels):
                    assert entry.startswith(label)
                    text = entry[len(label):].strip()
                    lines += [f'h5.mt-4 {number}. {label}', 'p.mb-4 ' + pug(html.escape(text))]
                    current['source'].append({'index': index, 'html': text, 'heading': label})
            for diagram in block.findall('.//dgm:relIds', NS):
                path = rels[diagram.get('{' + NS['r'] + '}dm')]
                if path.endswith('data2.xml'):
                    # Plan/Do/Check/Act ya están desarrollados a continuación.
                    continue
                data = ET.fromstring(archive.read('word/' + path))
                for p in data.findall('.//a:p', NS):
                    text = ''.join(t.text or '' for t in p.findall('.//a:t', NS)).strip()
                    if text:
                        rich = ''
                        for run in p.findall('a:r', NS):
                            value = html.escape(''.join(t.text or '' for t in run.findall('a:t', NS)))
                            prop = run.find('a:rPr', NS)
                            if prop is not None and prop.get('i') == '1':
                                value = '<em>' + value + '</em>'
                            rich += value
                        lines += ['p.mb-4 ' + pug(rich.strip() or html.escape(text))]
                        current['source'].append({'index': index, 'diagram': text})
    for theme in themes:
        # Separador ya aporta la transición vertical; ignorar líneas vacías y comentarios.
        for i, line in enumerate(theme['lines']):
            if line == 'Separador':
                j = i - 1
                while j >= 0 and not theme['lines'][j].strip():
                    j -= 1
                if j >= 0 and theme['lines'][j].startswith('p.mb-4 '):
                    theme['lines'][j] = theme['lines'][j].replace('p.mb-4', 'p.mb-0', 1)
                elif j >= 0 and theme['lines'][j].lstrip().startswith('img('):
                    while j >= 0 and not theme['lines'][j].startswith('.row'):
                        j -= 1
                    if j >= 0:
                        theme['lines'][j] = theme['lines'][j].replace('.mb-4', '.mb-0')
        last = len(theme['lines']) - 1
        while last >= 0 and (not theme['lines'][last].strip() or theme['lines'][last].startswith('//-')):
            last -= 1
        if last >= 0 and theme['lines'][last].startswith('p.mb-4 '):
            theme['lines'][last] = theme['lines'][last].replace('p.mb-4', 'p.mb-0', 1)
        if theme['lines'] and theme['lines'][-1].startswith('p.mb-4 '):
            theme['lines'][-1] = theme['lines'][-1].replace('p.mb-4', 'p.mb-0', 1)
        write(f'src/views/Tema{theme["number"]}.vue', view(f'Tema{theme["number"]}', theme['title'], theme['lines'], theme['number']))
        audit['themes'].append({k: v for k, v in theme.items() if k != 'lines'})

    glossary = []
    for row in body[503].findall('w:tr', NS)[1:]:
        cells = row.findall('w:tc', NS)
        term_html = '<br>'.join(inline(p) for p in cells[0].findall('w:p', NS)).replace(':', '')
        glossary.append({'termino': plain(cells[0]).rstrip(':'), 'terminoHtml': term_html,
                         'significado': '<br>'.join(inline(p) for p in cells[1].findall('w:p', NS) if inline(p))})
    references = []
    for p in body[507:517]:
        links = [rels.get(h.get('{' + NS['r'] + '}id'), '') for h in p.findall('.//w:hyperlink', NS)]
        references.append({'referencia': inline(p), 'link': next((v for v in links if v.startswith('http')), '')})
    config_path = ROOT / 'src/config/global.js'
    config = config_path.read_text(encoding='utf-8')
    config = re.sub(r"Name:\s*(?:'[^']*'|\"[^\"]*\"),", lambda _: 'Name: ' + json.dumps(title, ensure_ascii=False) + ',', config, count=1)
    config = re.sub(r"Description:\s*(?:'[^']*'|\"[^\"]*\"),", lambda _: 'Description: ' + json.dumps(description, ensure_ascii=False) + ',', config, count=1)
    menu = [{'nombreRuta': 'inicio', 'icono': 'fas fa-home', 'titulo': 'Volver al inicio'},
            {'nombreRuta': 'introduccion', 'icono': 'fas fa-info-circle', 'titulo': 'Introducción', 'desarrolloContenidos': True}]
    for t in themes:
        menu.append({'nombreRuta': f'tema{t["number"]}', 'numero': str(t['number']), 'titulo': t['title'], 'desarrolloContenidos': True,
                     'subMenu': [{'numero': s['number'], 'titulo': s['title'], 'hash': s['hash']} for s in t['subs']]})
    start = config.index('    menu: [')
    end = config.index('\n    subMenu: [', start) + 1
    config = config[:start] + '    menu: ' + dumps(menu) + ',\n' + config[end:]
    start = config.index('  glosario: [')
    end = config.index('  creditos: [')
    config = config[:start] + '  glosario: ' + dumps(glossary) + ',\n  referencias: ' + dumps(references) + ',\n' + config[end:]
    # Los paquetes finales se habilitan cuando existan, al finalizar la maquetación.
    config = re.sub(r"      \{\s*icono: 'fas fa-(?:file-pdf|download)',\s*titulo: 'Descargar (?:PDF|material)',\s*download: 'downloads/(?:dist.pdf|material.zip)',\s*\},\n", '', config)
    write('src/config/global.js', config)
    write('src/config/titulo.js', 'module.exports = ' + json.dumps(title, ensure_ascii=False) + '\n')
    router_path = ROOT / 'src/router/index.js'
    router = router_path.read_text(encoding='utf-8')
    marker = '      children: ['
    start = router.index(marker) + len(marker)
    end = router.index('\n      ],', start)
    routes = ''.join(f"\n        {{ path: 'tema{t['number']}', name: 'tema{t['number']}', component: () => import('../views/Tema{t['number']}.vue') }}," for t in themes)
    write('src/router/index.js', router[:start] + routes + router[end:])

    intro = ['p.mb-4 ' + pug(inline(body[31]))]
    intro += ['.row.justify-content-center.mb-4', '  .col-lg-10', '    .tarjeta--container.row']
    diagram = ET.fromstring(archive.read('word/diagrams/data1.xml'))
    diagram_texts = [''.join(t.text or '' for t in p.findall('.//a:t', NS)).strip() for p in diagram.findall('.//a:p', NS)]
    diagram_texts = [t for t in diagram_texts if t]
    ordered = diagram_texts[-1:] + diagram_texts[:-1]
    for i, text in enumerate(ordered):
        intro += [f'      .col-md.tarjeta.color-{"secundario" if i == 0 else "primario"}.p-3', '        p.mb-0.text-center ' + pug(html.escape(text))]
    intro += ['p.mb-4 ' + pug(inline(body[33])), '.intro-decisiones.p-4.mb-4', '  .row.justify-content-center.align-items-center', '    .col-lg-7.mb-4.mb-lg-0', '      .tarjeta.bg-white.shadow-sm.p-4', '        ul.lista-ul.mb-0']
    for p in body[34:39]:
        intro += ['          li.mb-2', '            i.fas.fa-comment', '            span ' + pug(inline(p))]
    intro += ['    .col-lg-3.col-8', '      figure', '        img(src="@/assets/curso/temas/intro/img1.svg" alt="")', 'p.mb-4 ' + pug(inline(body[39])), '.row.justify-content-center.mb-4', '  .col-lg-10', '    .cajon.color-primario.p-4', '      p.mb-0 ' + pug(inline(body[40])), 'p.mb-4 ' + pug(inline(body[41])), 'p.mb-0 ' + pug(inline(body[42])), '//- Incorporar aquí el video oficial 21730226_CF02_Guion_LIT_Video_01 cuando esté disponible.']
    intro[-2] = intro[-2].replace('p.mb-0', 'p.mb-4', 1)
    intro[-1] = '//- Video de muestra conservado por indicación del usuario; pendiente reemplazo por el oficial.'
    intro += ['.video', '  iframe(width="560" height="315" src="https://www.youtube.com/embed/vdPrCjWJSHo?si=X4NxENRo3LLXAua_" title="Video de introducción" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen)']
    write('src/views/Introduccion.vue', view('Introduccion', 'Introducción', intro))
    synthesis_alt = next(a for a in alts if a.startswith('En la síntesis'))
    synthesis = ['p.mb-4 ' + pug(inline(p)) for p in body[477:479]]
    synthesis += ['.row.justify-content-center.mb-4', '  .col-12', '    figure', f'      img(src="@/assets/curso/sintesis.svg" alt={json.dumps(synthesis_alt, ensure_ascii=False)})', '.row.justify-content-center', '  .col-auto', '    a.anexo.mb-0(:href="obtenerLink(\'/downloads/Sintesis.pdf\')" target="_blank" rel="noopener")', '      .anexo__icono', '        img(src="@/assets/bullets/icono-pdf.svg" alt="")', '      .anexo__texto', '        p Anexo. Síntesis']
    write('src/views/Sintesis.vue', view('Sintesis', 'Síntesis', synthesis, icon='fas.fa-sitemap'))

    with zipfile.ZipFile(ROOT / 'fuentes/21730226_CF02_AD.docx') as activity_zip:
        activity_doc = ET.fromstring(activity_zip.read('word/document.xml'))
    clean_choices(activity_doc)
    questions, fields, current_q = [], {}, None
    for row in activity_doc.findall('.//w:tr', NS):
        cells = row.findall('w:tc', NS)
        values = ['<br>'.join(inline(p) for p in cell.findall('w:p', NS) if inline(p)) for cell in cells]
        labels = [plain(cell) for cell in cells]
        if not labels:
            continue
        key = labels[0]
        if re.fullmatch(r'Pregunta \d+', key):
            qid = int(key.split()[-1])
            current_q = {'id': qid, 'texto': values[1], 'imagen': f'@/assets/actividad/imagen{(qid - 1) % 10 + 1}.png', 'barajarRespuestas': True, 'opciones': []}
            questions.append(current_q)
        elif key.startswith('Opción ') and current_q:
            current_q['opciones'].append({'id': key[7], 'texto': values[1], 'esCorrecta': len(labels) > 2 and labels[2].strip().lower() == 'x'})
        elif key.startswith('Comentario respuesta') and current_q:
            current_q['mensaje_correcto' if key.endswith(' correcta') else 'mensaje_incorrecto'] = values[1]
        elif len(values) > 1:
            fields[key] = values[-1]
    assert len(questions) == 20
    assert all(len(q['opciones']) == 4 and sum(o['esCorrecta'] for o in q['opciones']) == 1 for q in questions)
    quiz = {'tema': fields['Nombre de la Actividad'], 'titulo': 'Conociendo el desarrollo de chatbots y soluciones conversacionales.',
            'introduccion': '<b>Objetivo:</b> ' + fields['Objetivo de la actividad'] + '<br><br>' + fields['Instrucciones para el aprendiz'],
            'barajarPreguntas': True, 'titulo_aprobado': '¡BUEN TRABAJO!', 'titulo_reprobado': 'VUELVA A INTENTARLO.', 'preguntas': questions,
            'mensaje_final_aprobado': fields['Mensaje cuando supera el 70 % de respuestas correctas'],
            'mensaje_final_reprobado': fields['Mensaje cuando el porcentaje de respuestas correctas es inferior al 70 %']}
    write('src/config/actividad.json', dumps(quiz) + '\n')
    write('src/views/Actividad.vue', '''<template lang="pug">
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
''')
    audit.update({'glossary': len(glossary), 'references': len(references), 'questions': len(questions)})
    write('fuentes/cf02-extraccion.json', dumps(audit) + '\n')
    print(f'Preparados {len(themes)} temas, {sum(len(t["subs"]) for t in themes)} subtemas, {len(glossary)} términos, {len(references)} referencias y {len(questions)} preguntas.')


if __name__ == '__main__':
    prepare()
