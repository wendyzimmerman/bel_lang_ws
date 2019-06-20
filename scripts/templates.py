from jinja2 import Template

###############################################################################
# Function template ###########################################################
###############################################################################

function_template_str = """---
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

Long form: {{ function.name }}

Short form: {{ function.abbreviation }}

{{ function.description }}

{% if function.examples %}

### Function Signatures
{% for signature in function.signatures %}
##### {{ signature.summary }}
{% for arg in signature.arguments %}
1. {{ arg }}
{% endfor %}
{% endfor %}

### Examples
{% for example in function.examples %}
{% if example.description %}
{{ example.description }}
{% endif %}
    {{ example.assertion }}
{% endfor %}
{% endif %}

---
##### [Request an Edit]({{ issue_url }})
"""

function_template = Template(function_template_str)

###############################################################################
# Relation  template ##########################################################
###############################################################################

relation_template_str = """---
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

Long form: {{ relation.name }}
Short form: {{ relation.abbreviation}}

{{ relation.description }}

---
##### [Request an Edit]({{ issue_url }})
"""

relation_template = Template(relation_template_str)

###############################################################################
# Cheatsheet template #########################################################
###############################################################################

cheatsheet_template_str = """---
title: BEL Language Cheatsheet ({{ version }})
{% if cheatsheet.current %}
aliases:
- /language/reference/current/cheatsheet
{% endif %}
---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

### Functions
Go to: [Relations](#relations)
{% for function in cheatsheet.functions %}

#### {{ function.name }} ({{ function.abbreviation }})

{% for signature in function.signatures %}
##### {{ signature.summary }}
{% for arg in signature.arguments %}
1. {{ arg }}
{% endfor %}
{% endfor %}
{% endfor %}

### Relations
Go to: [Functions](#functions)

{% for relation in cheatsheet.relations %}
##### {{ relation.name}} ({{ relation.abbreviation }})
{% endfor %}

---
##### [Request an Edit]({{ issue_url }})
"""

cheatsheet_template = Template(cheatsheet_template_str)
