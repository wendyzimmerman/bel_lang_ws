from jinja2 import Template

###############################################################################
###############################################################################
# Function template           #################################################
###############################################################################
###############################################################################

function_template_str = """---
{% if function.name == function.abbreviation %}
title: {{ function.name }} v.{{ template_version }}
{% else %}
title: {{ function.name }} [{{ function.abbreviation }}] v.{{ template_version }}
{% endif %}

summary: {{ function.summary }}
{% if function.current %}
aliases:
- /language/reference/{{ version }}/{{ function.name}}
{% endif %}
hidden: true
tags:
{% for category in function.categories %}
- {{ category }}
{% endfor %}
---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

**Long form**: {{ function.name }}()  **Short form**: {{ function.abbreviation }}()

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
###############################################################################
# Relation template           #################################################
###############################################################################
###############################################################################

relation_template_str = """---
{% if relation.name == relation.abbreviation %}
title: {{ relation.name }} v.{{ template_version}}
{% else %}
title: {{ relation.name }} [{{ relation.abbreviation}}] v.{{ template_version}}
{% endif %}
{% if relation.current %}
aliases:
- /language/reference/{{ version }}/{{ relation.name}}
{% endif %}
hidden: true
summary: {{ relation.summary }}
tags:
{% for category in relation.categories %}
- {{ category }}
{% endfor %}
---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

**Long form**: {{ relation.name }}  **Short form**: {{ relation.abbreviation}}

{{ relation.description }}

---
##### [Request an Edit]({{ issue_url }})
"""

relation_template = Template(relation_template_str)

###############################################################################
###############################################################################
# Cheatsheet template           #################################################
###############################################################################
###############################################################################

cheatsheet_template_str = """---
title: Cheatsheet {{ template_version }}
{% if cheatsheet.current %}
aliases:
- /language/reference/{{ version }}/cheatsheet
{% endif %}
---
<!-- COMPUTER GENERATED PAGE!!! DO NOT EDIT DIRECTLY  -->
<!--    must be changed in scripts/templates.py which is processed by scripts/update_refs.py -->

### Functions
Go to: [Relations](#relations)
{% for function in cheatsheet.functions %}

{% if function.name == function.abbreviation %}
#### {{ function.name }}()
{% else %}
#### {{ function.name }}(), {{ function.abbreviation }}()
{% endif %}

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
{% if relation.name == relation.abbreviation %}
##### **{{ relation.name}}**
{% else %}
##### **{{ relation.name}}, {{ relation.abbreviation }}**
{% endif %}
{{ relation.summary }}
{% endfor %}

---
##### [Request an Edit]({{ issue_url }})
"""

cheatsheet_template = Template(cheatsheet_template_str)


###############################################################################
###############################################################################
# Function Section template                            ########################
###############################################################################
###############################################################################

function_section_template_str = """---
title: "Functions"
date: 2019-04-26T19:14:49-04:00
draft: false
weight: 2
---

{% raw %}
{{% children showhidden="true" description="true" sort="name"  %}}
{% endraw %}

---
##### [Request an Edit]({{ issue_url }})
"""

function_section_template = Template(function_section_template_str)

###############################################################################
###############################################################################
# Relation Section template           #########################################
###############################################################################
###############################################################################

relation_section_template_str = """---
title: "Relations"
date: 2019-04-26T19:14:49-04:00
draft: false
weight: 3
---

{% raw %}
{{% children showhidden="true" description="true" sort="name"  %}}
{% endraw %}
---
##### [Request an Edit]({{ issue_url }})
"""

relation_section_template = Template(relation_section_template_str)


###############################################################################
###############################################################################
# Version Section Template          ###########################################
###############################################################################
###############################################################################

version_section_template_str = """---
{% if template_version == "current" %}
title: Current ({{ version }})
{% else %}
title: {{ template_version }}
{% endif %}

date: 2019-04-26T19:14:49-04:00
draft: false
weight: {{ weight }}
---

{{ changes }}

---
##### [Request an Edit]({{ issue_url }})
"""

version_section_template = Template(version_section_template_str)

###############################################################################
###############################################################################
# Reference section template           ########################################
###############################################################################
###############################################################################

reference_section_template_str = """---
title: "Reference Section"
date: 2019-04-26T19:14:49-04:00
draft: false
weight: 2
---

### Versions

---
##### [Request an Edit]({{ issue_url }})
"""

reference_section_template = Template(reference_section_template_str)
