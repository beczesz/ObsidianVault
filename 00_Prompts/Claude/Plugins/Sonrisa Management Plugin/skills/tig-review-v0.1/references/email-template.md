# TIG Confirmation Email Template

## Subject Format

```
Banfi Istvan - [HONAP] havi orak visszaigazolasa - [PROJEKT NEV]
```

Example: `Banfi Istvan - 2026. marcius havi orak visszaigazolasa - Cloud Platform Services`

## Body Template (Hungarian)

```
Szia [AM NEV],

Banfi Istvan [HONAP] havi teljesitmenyigazolasat szeretnem lezarni. A kimutatas szerint a Te projektedre ([PROJEKT NEV]) [X] orat dolgozott ebben a honapban.

Kerlek nezd at, es ha rendben van, erositsd meg nekem egy rovid valaszban.

Ha barmi elterest latsz, jelezd es egyeztetunk.

Koszonom,
Szabolcs
```

## Multi-Project Email

When there are multiple projects, create one email per project to the respective AM. If a single AM owns multiple projects, they can be combined into one email listing all projects with their hours.

## CC Rules

- Always CC Finance (Szellar Tamara: szellar.tamara@sonrisa.hu)
- CC the PM if the project has one (Nagy Sandor: nagy.sandor.pm@sonrisa.hu)

## Gmail Draft Creation

Use the Gmail MCP `gmail_create_draft` tool:
- to: AM email address
- cc: PM + Finance emails (comma-separated)
- subject: formatted as above
- body: formatted as above with actual values filled in
