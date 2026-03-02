
# Update textů ke cvičením předmětu PRG

## 🌐 Dokumentace online

- GitHub Pages: `https://slytherins-hub.github.io/prg_exercises/`

V repozitáři je připravená dokumentace cvičení 1-4 přes MkDocs a automatický deploy na GitHub Pages.

## Co už je nastavené

- konfigurace dokumentace: `mkdocs.yml`
- zdroj docs: `docs/`
- workflow pro deploy: `.github/workflows/deploy-docs.yml`

## Jak to zapnout na GitHubu

1. Otevři repozitář na GitHubu.
2. Jdi do **Settings → Pages**.
3. V části **Build and deployment** nastav **Source = GitHub Actions**.
4. Hotovo.

Po pushi na `main` (nebo `master`) se automaticky spustí workflow a nasadí web na GitHub Pages.

## Odkaz na web

- Pokud stránka ještě není dostupná, počkej na první úspěšný běh workflow **Deploy docs to GitHub Pages** v záložce **Actions**.

## Jak nasadit (lokálně)

```bash
git add .
git commit -m "Nastavení docs a GitHub Pages"
git push
```

## Jak si to ověřit lokálně

```bash
uv run mkdocs serve
```

Pak otevři: `http://127.0.0.1:8000`

Jednorázový build:

```bash
uv run mkdocs build
```

Výstup je ve složce `site/`.

## Struktura repozitáře

- `docs/` – hlavní zdroj výukových materiálů pro MkDocs
- `mkdocs.yml` – konfigurace webové dokumentace a navigace
- `scripts/` – pomocné skripty pro správu lokálního serveru

## Instalace závislostí

Pro instalaci a update závislostí používej pouze `uv`:

```bash
uv sync
```

Nepoužívej `pip install ...` mimo `uv` workflow.

## Spolehlivý restart lokálního serveru (Windows)

Když zlobí porty nebo běží starý `mkdocs serve`, použij skript:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\restart_mkdocs_server.ps1
```

Co skript udělá:
- ukončí starý `mkdocs serve` na daném portu,
- uvolní port (default `8000`),
- spustí `uv run mkdocs build`,
- spustí `uv run mkdocs serve -a 127.0.0.1:8000` skrytě na pozadí (bez nového okna),
- provede health-check URL.

Užitečné varianty:

```powershell
# jen stop serveru na portu 8000
powershell -ExecutionPolicy Bypass -File .\scripts\restart_mkdocs_server.ps1 -StopOnly

# restart bez buildu
powershell -ExecutionPolicy Bypass -File .\scripts\restart_mkdocs_server.ps1 -NoBuild

# jiný port
powershell -ExecutionPolicy Bypass -File .\scripts\restart_mkdocs_server.ps1 -Port 8123

# krátký stop alias
powershell -ExecutionPolicy Bypass -File .\scripts\stop_mkdocs_server.ps1 -Port 8000
```