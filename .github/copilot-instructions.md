# Copilot Instructions for prg-pokus

## Big picture
- Repo je primárně obsahový: výukové materiály BPC-PRG v Markdownu pro začátečníky (medicína/bioinženýrství).
- Aktuální zdroj pravdy je složka `docs/`.
- Cvičení 1-5 jsou rozdělená po stránkách ve složkách `docs/cviceni_01` až `docs/cviceni_05`.

## Co upravovat
- Výukový obsah upravuj primárně v `docs/`.
- `osnova.md` ber jako orientační kurikulární kontext (nemusí být 1:1 synchronní s texty cvičení).
- V kořeni repozitáře udržuj konzistentní popis v `README.md` (online odkaz, lokální workflow, struktura).
- Při přesunech/mazání obsahu vždy zkontroluj a aktualizuj `mkdocs.yml` (zejména `docs_dir` a `nav`).

## Styl a didaktický pattern (povinné)
- Piš česky a neformálně na „ty“.
- Drž strukturu cvičení: `## ÚVOD` → `### Co se v tomto cvičení naučíte?` → `## CÍL ...`.
- Udržuj tok „motivace → koncept → příklad → procvičení“ (viz stránky v `docs/cviceni_01/`).
- Používej medicínské/bio kontexty (BMI, vitální funkce, pacient, DNA, senzory), ne generické `foo/bar` ukázky.
- Zachovávej formáty bloků `💡 Tip`, `⚠️ Pozor`, `📘 Co je...?`, sekce `📝 ÚKOL` a `💻 Zkus`.

### Formátové značky (konzistence napříč cvičeními)
- Emoji značky ber jako **součást formátu**, ne jen dekoraci v textu.
- Používej jednotně:
	- Úkoly: `**📝 ÚKOL ...**` (nebo sekční nadpis `## 📝 ...` tam, kde jde o celou sekci).
	- Bonusy: `## 🌟 BONUSOVÉ ÚKOLY` a jednotlivé položky `**🌟 BONUS ...**`.
	- Tipy/poznámky: vždy jako blockquote `> **💡 Tip:** ...` (analogicky `> **💡 Poznámka:** ...`, `> **💡 Nápověda:** ...`).
- Nepoužívej volné varianty typu `💡 **Tip:** ...` bez blockquote nebo `> 💡 **Tip:** ...`.

## Lokální workflow
- Pro Python a nástroje používej `uv` (ne holé `python`): `uv sync`, `uv run <prikaz>`, `uv add <balicek>`.
- Instalace závislostí vždy přes `uv` (`uv sync` / `uv add`), nikdy přes přímé `pip install`.
- Respektuj `requires-python = ">=3.13"` v `pyproject.toml`.
- Náhled dokumentace lokálně: `uv run mkdocs serve` (zdroj docs je `docs/`).
- Jednorázový build: `uv run mkdocs build` (výstup do `site/`).
- Po každé změně v dokumentaci (`docs/`, `mkdocs.yml`, `docs/assets/`) vždy:
  1) spusť build `uv run mkdocs build`,
  2) restartuj lokální server skriptem `scripts/restart_mkdocs_server.ps1`,
  aby byl náhled na `http://127.0.0.1:8000/` vždy aktuální.
- Po úpravách Markdownu kontroluj render ve VS Code Markdown Preview (nadpisy, tabulky, relativní odkazy, fenced code blocks).

## Kódování souborů (kritické)
- Všechny textové soubory v repu (`.md`, `.yml`, `.py`, `.toml`) ber jako UTF-8.
- Při práci v PowerShellu vždy explicitně nastav kódování i při čtení i při zápisu:
  - čtení: `Get-Content -Encoding utf8`
  - zápis: `Set-Content -Encoding utf8` (nebo `Out-File -Encoding utf8`)
- Nepoužívej hromadné přepisování celého souboru přes shell, pokud stačí cílená změna.
- Pro menší/konkrétní editace preferuj `apply_patch`, aby se minimalizovalo riziko rozbití diakritiky.
- Po větší textové úpravě udělej rychlou kontrolu mojibake:
  - `rg -n "Ã|Ä|Å|Â|â€|Ă|Ĺ|ď¸|đź" docs .github`
- Pokud se mojibake objeví, nepokračuj v dalších editacích, nejdřív oprav kódování.

## CI/deploy a integrace
- GitHub Actions workflow `.github/workflows/deploy-docs.yml` nasazuje GitHub Pages při pushi na `main`/`master`.
- CI build aktuálně instaluje jen `mkdocs` a spouští `mkdocs build`; nepředpokládej zde test runner.
- `mkdocs.yml` je navázaný na kompletní obsah ve `docs/`.

## Konvence v ukázkách kódu
- Preferuj čitelné názvy proměnných pro začátečníky (`vek`, `teplota`, `pacienti`) a `snake_case`.
- U funkcí drž docstringy se sekcemi `Args:` a `Returns:` (viz materiály v `docs/cviceni_03/`).
- Vysvětluj bezpečné vzory explicitně (např. konkrétní `except ValueError`, validace vstupu ve `while`), ne „holé“ `except:`.

## Co nedělat
- Neformalizuj tón do „Zkuste...“; drž přímé „Zkus...“.
- Nevytvářej novou aplikační architekturu (`src/`, frameworky) bez jasného důvodu — tohle není aplikační repo.
- Nepřebírej zastaralý obsah bez ověření proti aktuálním souborům v `docs/`.
