from jinja2 import Template


# Function template ###########################################################

function_template_str = """
---
title: {{ function.name }} ({{ version }})
{% if function.current %}
aliases:
- /language/reference/current/{{ function.name}}
{% endif %}

categories:
{% for category in function.categories %}
- {{ category }}
{% endfor %}
---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

## {{ function.name }}

{{ function.description }}

{% if function.examples %}
### Examples
{% for example in function.examples %}
{% if example.description %}
{{ example.description }}
{% endif %}
    {{ example.assertion }}
{% endfor %}
{% endif %}
"""

function_template = Template(function_template_str)


# Relation  template ##########################################################

relation_template_str = """
---
title: {{ relation.name }} ({{ version}})
{% if relation.current %}
aliases:
- /language/reference/current/{{ relation.name}}
{% endif %}

categories:
{% for category in relation.categories %}
- {{ category }}
{% endfor %}
---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

## {{ relation.name }}

"""

relation_template = Template(relation_template_str)


# Cheatsheet template #########################################################

cheatsheet_template_str = """
---
title: BEL Language Cheatsheet

---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

## BEL Language Cheatsheet (version {{ version }})

### Functions
{% for function in cheatsheet.functions %}

#### {{ function.name }} ({{ function.abbreviation }})
: {{ function.summary}}

{{ function.argument_summary }}
{% for arg_help in function.argument_help_listing %}
* {{ arg_help }}
{% endfor %}
{% endfor %}

### Relations
{% for relation in cheatsheet.relations %}
##### {{ relation.name}} ({{ relation.abbreviation }})
{% endfor %}
"""

cheatsheet_template = Template(cheatsheet_template_str)
