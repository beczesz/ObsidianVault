---
description: Maestro TEAM-INTRODUCE mode — új agent szervezése a családba. Canonical + registration scaffold + AGENTS_INDEX + BDOS/CLAUDE.md bejegyzés + (opcionális) slash-command csomag. Confirmation kötelező.
id: 95500d01-90b8-49cb-9377-a257872eb6a6
index_schema_version: 1
---

A felhasználó új agentet vezet be a BDOS családba.

**$ARGUMENTS** — kötelező: név + description + modes. Példák:
- `--name=scribe --description="Tartalom-szerkesztő agent — markdownt gondoz, headert javít" --modes=write,review,publish`
- `--name=validator --description="..." --modes=check,review --slash_prefix=val --position="Second opinion / cross-check"`

**Tennivaló:**

1. Parsold az $ARGUMENTS-ből: `--name=` (kötelező, lowercase slug), `--description=` (kötelező, egy mondat), `--modes=` (kötelező, vesszős lista), opcionális `--slash_prefix=` (default: name első 3-4 karaktere), `--position=` (kötelező — egymondatos szerep).
2. Ha bármelyik kötelező hiányzik, kérdezz vissza.
3. Hívd meg a Maestro-t **`subagent_type: maestro`** **team-introduce módban**:
   - Validálja: név unique-e a családban (nincs ütközés), modes lista nem üres, position értelmes.
   - Generál scaffold-ot:
     - `00_Prompts/BDOS/agents/<name>.md` v0.1 — frontmatter + §1 Identity + §2 Mission + §3 Constraints + §4 Modes placeholderekkel + §5 Anti-patterns + §6 Changelog
     - `.claude/agents/<name>.md` — registration thin pointer (canonical-ra mutat)
     - AGENTS_INDEX entry hozzáadás az "Active agents" szekció végére (az utolsó aktív agent után)
     - BDOS/CLAUDE.md táblába új sor
     - (Opcionális, ha kérted) `<slash_prefix>-<mode>.md` slash command minden mode-ra
4. **Confirmation gate KÖTELEZŐ** — Maestro mutatja a fájl-listát + a kulcs tartalmi mezőket (§1 Identity + §4 Modes vázlat), vár igen/yes válaszra.
5. Apply: létrehoz minden fájlt.
6. Végén javaslat: a scaffold csak indító keret — az új agent canonical-jának Identity/Mission/Modes szekcióit a user / Maestro további iterációval töltsd fel részletesen (a Heraldnál ezt csináltuk manuálisan; ez a parancs a szerkezeti vázat adja, a tartalmat te + a következő ülés tölti).

**Megjegyzés:** ez az automatizált változata annak, amit Heraldnál kézzel csináltunk. Új agentnek mindig ezzel kezdjünk, hogy a struktúra konzisztens maradjon a családban.
