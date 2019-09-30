# TODO
# actually format correctly
# things are higgedly-piggedy

from jinja2 import Environment, PackageLoader, select_autoescape
import io
from generate_lists import get_all_lists

env = Environment(
    loader=PackageLoader(__name__, 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

out = io.open('webpage/ayymd.html', mode='w', encoding='utf-8')

allLists = get_all_lists()

out.write(template.render(allLists=allLists))

out.close()