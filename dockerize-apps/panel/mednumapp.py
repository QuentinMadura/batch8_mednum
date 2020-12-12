import panel as pn
import numpy as np
import holoviews as hv
import numpy as np
import panel as pn
from panel.widgets.select import AutocompleteInput
import param
from mednum.config import *
from mednum.loaders import read_merged_data
import geoviews as gv

# from mednum.controlers.autocomplete import AppAuto
from mednum.indicators.panels import TopIndicators, Indicators
from pathlib import Path
import mednum

css_mednum = [str(Path(__file__).parent / "statics" / "css" / "mednum.css")]

css = [
    "https://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css",
    css_mednum[0],
]
js = {
    "$": "https://code.jquery.com/jquery-3.4.1.slim.min.js",
    "DataTable": "https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js",
}

pn.extension(css_files=css_mednum)


template = """
{% extends base %}

<!-- goes in body -->
{% block postamble %}
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
{% endblock %}

<!-- goes in body -->
{% block contents %}
{{ app_title }}
<p>This is a Panel app with a custom template allowing us to compose multiple Panel objects into a single HTML document.</p>
<br>
<div class="container-fluid">
<div class="row">
    <div class="col-sm-2">
          {{ embed(roots.sidebar)}}
    </div>
        <div class="col-sm-8 ml-auto">
      <div class="row">
      {{ embed(roots.top)}}
      </div>
      <div class="row">
          {{ embed(roots.main)}}
      </div>
    </div>
  </div>
</div>


{% endblock %}
"""

tmpl = pn.Template(template)
tmpl.add_variable("app_title", "<h1>Custom Template App</h1>")

mednumapp = mednum.MedNumApp(name="Sélection")

# Top indicator
tmpl.add_panel("sidebar", mednumapp.lat_widgets)
tmpl.add_panel("top", pn.Row(mednumapp.top_panel, sizing_mode="stretch_width")),
tmpl.add_panel(
    "main",
    mednumapp.tabs_view,
)

tmpl.servable()
