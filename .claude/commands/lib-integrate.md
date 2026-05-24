---
description: Librarian INTEGRATE mode — vault-on kívüli mappa felmérése, javaslat-generálás importálható tartalmakra. Csak read-only, soha nem mozgat.
id: a46f76ea-fdca-47ff-9e80-9cb8a8d51200
index_schema_version: 1
---

A felhasználó **vault-on kívüli mappát** szeretne felmérni a Librariannal, hogy javaslatot kapjon mi érdemes a vault-ba beolvasztani, hová.

**$ARGUMENTS** — külső mappa abszolút útvonala. Példák:
- `~/Documents/Obsidian_old` → konkrét régi mappa
- `~/Downloads` → friss letöltések felmérése
- `~/Documents ~/Desktop` → több hely egyszerre (több külső scope egymás után)
- üres → default trio: `~/Documents`, `~/Downloads`, `~/Desktop`

**Tennivaló:**

1. Parsold az $ARGUMENTS-et. Ha üres, használd a default triót.
2. **Privacy alapelv (kötelező):** sose enged `~/Library`, `~/Pictures`, `~/Photos`, `~/Movies`, `~/Music`, `*.git/`, `node_modules/`, `*.app/`, `~/.ssh`, `~/.aws`, `~/.config` mélységű olvasást. Ha az $ARGUMENTS ezekre mutat, állj le és kérdezz vissza.
3. Hívd meg a Librariant **`subagent_type: librarian`**-nal integrate módban:
   - `mode: integrate`
   - `external_scope: <abs path(s)>`
   - `file_types: [md, txt]` (default v0.4-ben)
4. A subagent **olvas** a külső mappákban, **soha nem mozgat / nem ír** oda. Csak a vault-ban hoz létre egy javaslat-fájlt.
5. Output: `0. Ideas Vault/00_INTEGRATE_PROPOSALS.md` — strukturált lista az összes találatról confidence score-ral (H/M/L) és javasolt vault-célútvonallal
6. A summary-ben emeld ki: hány fájlt vizsgált, hány high-confidence javaslat, melyek a legtipikusabb cél-domain-ek

**Soha nem mozgat magától.** A felhasználó áttekinti az `00_INTEGRATE_PROPOSALS.md`-et, dönt, és **utána** indítunk tidy vagy manuális mozgatást a kiválasztott fájlokra.
